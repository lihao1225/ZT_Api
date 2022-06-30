"""
Author: lihao
Time: 2022/6/2

"""
import os

import allure
import pytest

from common.ddt_util import read_test_yaml
from common.handle_path import YAML_DATA
from common.request_util import RequestUtil
from hotloads.debug_talk import DebugTalk


@allure.epic('业务中台-从erp拉取数据到中台数据库相关接口')
@allure.feature("md_erp_stream_provider(批发业务拉取服务)")
class Test_Md:

    @pytest.mark.parametrize('case_info', read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/get_token.yaml')))
    @allure.story('登录接口')
    @allure.severity(allure.severity_level.BLOCKER)
    # @pytest.mark.flaky(reruns=2,reruns_delay=2)
    @pytest.mark.run(order=1)
    def test_login(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("erp拉取采购数据接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/pull_purchasing_data.yaml')))
    def test_pull_purchasing_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("erp拉取发票接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/pull_invoice_data.yaml')))
    @pytest.mark.run(order=2)
    def test_pull_invoice_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("erp拉取进销接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/pull_out_and_put_into_storage.yaml')))
    def test_pull_out_and_put_into_storage(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story('erp拉取销售数据接口')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/pull_sale_data.yaml')))
    def test_pull_sale_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("erp按照日期拉取采购数据接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/pull_purchasing_day_data.yaml')))
    def test_pull_purchasing_day_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story('erp按照日期拉取销售/采购出入库数据接口')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(
                                 os.path.join(YAML_DATA, 'wholesale_business/pull_out_and_put_into_storage_day.yaml')))
    def test_pull_out_and_put_into_storage_day(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story('erp按日期拉取数据接口')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/pull_sale_day_data.yaml')))
    def test_pull_sale_day_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("erp按日拉取发票数据接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info',
                             read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/pull_invoice_day_data.yaml')))
    def test_pull_invoice_day_data(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)
    #
    # # @allure.story('推送U8C客商关系为空接口')
    # # @allure.severity(allure.severity_level.NORMAL)
    # # @pytest.mark.parametrize('case_info',
    # #                          read_test_yaml(os.path.join(YAML_DATA, 'wholesale_business/push_u8c_customer_null.yaml')))
    # # def test_push_u8c_customer_null(self, case_info):
    # #     allure.dynamic.title(case_info['name'])
    # #     RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发采购票折数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_purchasing_ticket_discount.yaml')))
    def test_push_u8c_purchasing_ticket_discount(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发采购出库数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_procurement_of_outbound.yaml')))
    def test_push_u8c_procurement_of_outbound(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发采购入库数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_procurement_warehousing.yaml')))
    def test_push_u8c_procurement_warehousing(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发销售出库X12数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_sales_of_outbound_X12.yaml')))
    def test_push_u8c_sales_of_outbound_X12(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发销售入库X24数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_sales_of_outbound_X24.yaml')))
    def test_push_u8c_sales_of_outbound_X24(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发销售出库X31数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_sales_of_outbound_X31.yaml')))
    def test_push_u8c_sales_of_outbound_X31(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发销售入库X41数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_sales_of_outbound_X41.yaml')))
    def test_push_u8c_sales_of_outbound_X41(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)


    @allure.story("推送批发销售出库X12和X31凭证数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_credentials_sale_X12andX31.yaml')))
    def test_push_u8c_credentials_sale_X12andX31(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)


    @allure.story("推送批发销售入库X24和X41凭证数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_credentials_sale_X24andX41.yaml')))
    def test_push_u8c_credentials_sale_X24andX41(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)

    @allure.story("推送批发销售发票数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_sales_invoice.yaml')))
    def test_push_u8c_sales_invoice(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)


    @allure.story("推送批发采购发票数据到U8C接口")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('case_info', read_test_yaml(
        os.path.join(YAML_DATA, 'wholesale_business/push_u8c_procurement_invoice.yaml')))
    def test_push_u8c_procurement_invoice(self, case_info):
        allure.dynamic.title(case_info['name'])
        RequestUtil(DebugTalk()).standard_yaml_testcase(case_info)