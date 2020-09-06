import allure

from common.basic_handler import Basic
from util.data_handler import dataHandler


@allure.feature("客户端用户相关接口")
class TestEduTeacherController:
    @allure.story("根据id获取老师课程列表的接口")
    def test_case_get_teacher_course_list(self):
        teacherId_list = dataHandler.get_teacherId_list()
        for teacherId in teacherId_list:
            customize_body = {"pageNum": 1, "pageSize": 10, "teacherId": teacherId}
            api_info = Basic().get_api_by_name("get_teacher_course_list")
            content = Basic().send_request(**api_info,customize_body=customize_body)
            assert content.status_code == 200

    @allure.story("根据id获取老师详情的接口")
    def test_case_get_teacher_details(self):
        teacherId_list = dataHandler.get_teacherId_list()
        for teacherId in teacherId_list:
            params = "teacherId="+str(teacherId)
            api_info = Basic().get_api_by_name("get_teacher_details", customize_params=params)
            content = Basic().send_request(**api_info)
            assert content.status_code == 200

