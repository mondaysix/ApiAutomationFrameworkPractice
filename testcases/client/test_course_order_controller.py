import json

import allure

from common.basic_handler import Basic
from config.global_config import GlobalConfig
from util.data_handler import dataHandler


@allure.feature("客户端用户相关接口")
class TestCourseOrderController:
    @allure.story("获取用户的课程订单信息接口")
    def test_case_get_course_order(self):
        api_info = Basic().get_api_by_name("get_mycourse_order")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200
        TestCourseOrderController.course_list_dict = dataHandler().str_to_dict(content.text)
        # print(content.text)
    @allure.story("获取课程订单接口")
    def test_case_course_order(self):
        cid_list = dataHandler().traverse_get_list_from_dict(TestCourseOrderController.course_list_dict)

        for cid in cid_list:  # 73
            # print(cid)
            customize_body = {"cid": cid, "userId": GlobalConfig.userId}
            dataHandler.cId = cid
            # print(dataHandler.getCid())
            # customize_body = "{\"cid\":"+"\""+str(cid)+"\""+",\"userId\":"+"\""+str(15)+"\"}"
            api_info = Basic().get_api_by_name("get_course_order", customize_body=customize_body)
            content = Basic().send_request(**api_info)
            # print(content.text)
            assert content.status_code == 200
