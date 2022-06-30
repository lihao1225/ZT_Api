"""
Author: lihao
Time: 2022/6/2

"""
import json
import os
import re
import traceback

import jsonpath
import requests

from common.assert_utils import assert_result
from common.handle_path import DIR
from common.jiemi_utils import decrypt
from common.logger_util import info_log, error_log
from common.yaml_util import YamlUtil
from hotloads.debug_talk import DebugTalk


class RequestUtil():

    def __init__(self, obj):
        self.request = requests.session()
        self.obj = obj

    def standard_yaml_testcase(self, caseinfo):
        try:
            info_log('-----------------接口测试开始----------------')
            caseinfo_keys = caseinfo.keys()
            # 在YAML用例里面必须包含一级关键字：name,request,validates
            if 'name' in caseinfo_keys and 'request' in caseinfo_keys and 'validate' in caseinfo_keys:
                request_keys = caseinfo['request'].keys()
                info_log(f'接口名称：{caseinfo["name"]}')
                if 'method' in request_keys and 'url' in request_keys and 'base_url' in request_keys:
                    # 发送请求
                    base_url = caseinfo['request'].pop('base_url')
                    url = caseinfo['request'].pop('url')
                    method = caseinfo['request'].pop('method')
                    res = self.send_all_request(method, base_url, url, **caseinfo['request'])
                    #对返回解决进行解密操作
                    data = jsonpath.jsonpath(res.json(), '$..data')[0]
                    password = DebugTalk().read_config('password')
                    jiemi_res = decrypt(data, password)
                    res_text = res.text
                    #将返回文本信息转为为字典格式
                    dic_res_text = json.loads(res_text)
                    #把解密的结果进行替换
                    dic_res_text['data'] = jiemi_res
                    #转换为字符串后除去str中的\\
                    res_text = json.dumps(dic_res_text,ensure_ascii=False).replace('\\','')
                    status_code = res.status_code
                    res_json = ''
                    try:
                        res_json = res.json()
                        res_json['data'] = jiemi_res
                    except:
                        error_log('返回结果不是json格式')
                    if 'extract' in caseinfo.keys():
                        for key, value in caseinfo["extract"].items():
                            if "(.*?)" in value or "(.+?)" in value:
                                zz_value = re.search(value, res_text)
                                if zz_value:
                                    data = {key: zz_value.group(1)}
                                    YamlUtil(os.path.join(DIR, 'extract.yaml')).write_yaml(data)
                                else:
                                    info_log("extract提取中间变量，正则有误或者是接口返回有误！")
                            else:
                                js_value = jsonpath.jsonpath(res_json, value)
                                if js_value:
                                    data = {key: js_value[0]}
                                    YamlUtil(os.path.join(DIR, 'extract.yaml')).write_yaml(data)
                                else:
                                    info_log("extract提取中间变量，JSONPATH有误或者是接口返回有误！")
                    # 断言
                    # 预期结果
                    yq_result = caseinfo['validate']
                    info_log(f"预期结果：{yq_result}")
                    if yq_result:
                        sj_result = res_json
                        info_log(f"实际结果:{sj_result}")
                        all_flag = assert_result(yq_result, sj_result, status_code)
                        if all_flag == 0:
                            info_log("断言成功")
                            info_log("接口测试成功")
                            info_log("----------------接口测试结束------------------\n")
                        else:
                            info_log("断言失败")
                            info_log("----------------接口测试结束------------------\n")
                    else:
                        info_log(f"实际结果：{res_json}")
                        info_log("无须进行断言")
                        info_log("----------------接口测试结束------------------\n")

                else:
                    error_log("request下面必须包含有method，url,base_url 这三个二级关键字")
            else:
                error_log("在YAML用例里面必须包含有一级关键字：name,request,validate")
        except Exception as e:
            error_log(f"标准化测试用例报错{str(traceback)}")
            raise e

    def send_all_request(self, method, base_url, url, **kwargs):
        try:
            info_log(f'接口请求方式：{method}')
            # method统一小写
            method = str(method).lower()
            url = self.replace_get_value(base_url + url)
            info_log(f"请求路径：{url}")
            # headers,params.data.json通过${变量名}取值
            for key, value in kwargs.items():
                if key in ['headers', 'params', 'data', 'json']:
                    kwargs[key] = self.replace_get_value(value)
                    info_log(f'请求{key}参数：{kwargs[key]}')
                elif key == 'files':
                    for file_key, file_value in value.items():
                        value[file_key] = open(file_value, 'rb')

            res = self.request.request(method, url, **kwargs)

            return res
        except Exception as e:
            error_log(f'发送请求报错：{str(traceback.format_exc())}')
            raise e

    def replace_get_value(self, data):
        try:
            if data:
                # 保存出入的数据类型
                data_type = type(data)
                # 把不同的数据类型转换为字符串，因为只有字符串才能进行替换
                if isinstance(data, list) or isinstance(data, dict):
                    str_data = json.dumps(data)
                else:
                    str_data = str(data)
                for i in range(1, str_data.count("${") + 1):
                    if '${' in str_data and '}' in str_data:
                        start_index = str_data.index("${")
                        end_index = str_data.index('}', start_index)
                        old_value = str_data[start_index:end_index + 1]
                        # 反射getattr:通过【类的对象】和【方法名】字符串调用方法
                        function_name = old_value[2:old_value.index('(')]
                        # 调用反射方法
                        arg_value = old_value[old_value.index('(') + 1:old_value.index(')')]
                        # 调反射犯法
                        if arg_value != "":
                            # 含有参数传参
                            all_args_value = arg_value.split(",")
                            new_value = getattr(self.obj, function_name)(*all_args_value)
                        else:
                            # 没有参数传参
                            new_value = getattr(self.obj, function_name)()
                        # 把旧的表达式替换成新的
                        if (isinstance(new_value, int) or isinstance(new_value, float)):
                            str_data = str_data.replace('"' + old_value + '"', str(new_value))
                        else:
                            str_data = str_data.replace(old_value, str(new_value))
                # 还原数据
                if isinstance(data, list) or isinstance(data, dict):
                    data = json.loads(str_data)
                else:
                    data = data_type(str_data)
                return data
            else:
                return data
        except Exception as e:
            error_log(f'数据替换错误：{str(traceback.format_exc())}')
            raise e
