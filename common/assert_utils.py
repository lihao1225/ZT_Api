"""
Author: lihao
Time: 2022/5/31

"""
import sys
import traceback

import jsonpath

from common.datebase_utils import DateBaseUtil
from common.logger_util import error_log, info_log


def assert_result(yq_result, sj_result, status_code):
    try:
        all_flag = 0

        for yq in yq_result:
            for key, value in yq.items():
                if key == 'codes':
                    flag = codes_assert(value, status_code)
                    all_flag = all_flag + flag
                elif key == 'equals':
                    flag = equals_assert(value, sj_result)
                    all_flag = all_flag + flag
                elif key == 'contains':
                    flag = contains_assert(value, sj_result)
                    all_flag = all_flag + flag
                elif key == 'db_equals':
                    flag = datebase_assert(value, sj_result)
                    all_flag = all_flag + flag
        return all_flag
    except Exception as e:
        error_log(f'断言报错：{str(traceback.format_exc())}')
        raise e


def codes_assert(value, status_code):
    flag = 0
    for assert_key, assert_value in value.items():
        if assert_key == 'status_code':
            if assert_value != status_code:
                flag = flag + 1
                error_log("codes断言失败" + str(assert_key) + "不等于" + str(assert_value) + "")
    return flag


# 相等断言
def equals_assert(value, sj_result):
    flag = 0
    for assert_key, assert_value in value.items():
        lists = jsonpath.jsonpath(sj_result, '$..%s' % assert_key)
        if lists:
            if assert_value not in lists:
                flag += 1
                error_log('equals断言失败' + str(assert_key) + '不等于' + str(assert_value) + "")
        else:
            flag = flag + 1
            error_log("equals断言失败，返回结果中没有" + str(assert_key) + '')
    return flag


# 包含断言
def contains_assert(value, sj_result):
    flag = 0
    if str(value) not in str(sj_result):
        flag = flag + 1
        error_log(f"contains断言失败，返回结果中没有{str(value)}")
    return flag


# 数据库断言
def datebase_assert(value, sj_result):
    flag = 0
    for sql, key in value.items():
        if key not in sj_result:
            flag = flag + 1
            error_log(f'db_equals断言失败：实际结果中不包含{key}')
        else:
            res = None
            try:
                res = DateBaseUtil().find_one(sql)
            except:
                flag = flag + 1
                error_log(f"db_equals断言失败：sql查询异常{sys.exc_info()}")
                if not res:
                    flag = flag + 1
                    error_log("db_datebase断言失败：sql有语法错误或者查询没有结果返回")
                else:
                    if sj_result[key] in res:
                        info_log("断言成功")
                    else:
                        flag = flag + 1
                        error_log("sql查询结果跟实际结果不等")

            return flag
