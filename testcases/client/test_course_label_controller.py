import allure
import pytest

from common.basic_handler import Basic
from testcases.client.test_course_controller import TestCourseController
from util.data_handler import dataHandler


@allure.feature("客户端用户相关接口")
class TestCourseLabelController:
    course_list_dict = {}
    @allure.story("获取所有课程标签的接口")
    def test_case_get_course_list(self):
        api_info = Basic().get_api_by_name("get_course_label_listall")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200
        # print(content.text) # 包含clabelId
        TestCourseLabelController.course_list_dict = dataHandler().str_to_dict(content.text)
    @allure.story("获取课程标签的接口")
    def test_case_get_course(self):
        pidList = dataHandler().traverse_get_list_from_dict(TestCourseLabelController.course_list_dict)

        for pid in pidList:
            param_pid = "pid="+str(pid)
            # print(param_pid)
            api_info = Basic().get_api_by_name("get_course_label_list", customize_params=param_pid)
            content = Basic().send_request(**api_info)
            # print(content.text)
            assert content.status_code == 200

    @allure.story("免费微课和K12教辅直播")
    def test_case_get_course_video(self):
        clabelid_list = dataHandler.get_clabelId_list()
        ctypeId = dataHandler.get_value_dict()["ctypeId"]
        # print(ctypeId)
        for clabelId in clabelid_list:
            label_list = []
            label_list.append(clabelId)
            # print(label_list)
            customize_body = {"ctypeId": ctypeId, "labels": label_list, "pageNum": 0, "pageSize": 0, "type": 0}
            api_info = Basic().get_api_by_name("get_course_video", customize_body=customize_body)
            # print(api_info)
            content = Basic().send_request(**api_info)
            assert content.status_code == 200
