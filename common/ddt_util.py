"""
Author: lihao
Time: 2022/6/1

"""
import json
import traceback

import yaml

from common.logger_util import error_log


def read_test_yaml(yaml_path):
    try:
        with open(yaml_path, 'r', encoding="utf-8") as f:
            case_info = yaml.load(f, Loader=yaml.FullLoader)
            if len(case_info) >= 2:
                return case_info
            else:
                if 'parameterize' in dict(*case_info).keys():
                    new_case_info = parameterize_ddt(*case_info)
                    return new_case_info
                else:
                    return case_info

    except Exception as e:
        error_log(f'读取测试用例yaml文件报错：{str(traceback.format_exc())}')
        raise e


def parameterize_ddt(case_info):
    try:
        # 将参数转化为字符串
        case_str = json.dumps(case_info)
        # 获取数据列表
        data_list = case_info['parameterize']
        length_success = True
        key_list = len(data_list[0])
        # 校验参数华的数据是否有误
        for param in case_info['parameterize']:
            if len(param) != key_list:
                length_success = False
                error_log(f'此条数据有误{param}')
                continue
        # 替换后的数据list
        new_caseinfo = []
        if length_success:
            # 行数据
            for x in range(1, len(data_list)):
                case_info_raw = case_str
                # 遍历出每一行的数据
                for y in range(0, len(data_list[x])):
                    if isinstance(data_list[x][y], int) or isinstance(data_list[x][y], float):
                        case_info_raw = case_info_raw.replace('"$ddt{' + data_list[0][y] + '}"', str(data_list[x][y]))
                    else:
                        case_info_raw = case_info_raw.replace("$ddt{" + data_list[0][y] + "}", str(data_list[x][y]))

                new_caseinfo.append(json.loads(case_info_raw))
        return new_caseinfo
    except Exception as e:
        error_log(f'数据驱动进行替换报错：{str(traceback.format_exc())}')
        raise e
