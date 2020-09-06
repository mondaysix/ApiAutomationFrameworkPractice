import allure

from common.basic_handler import Basic
from config.global_config import GlobalConfig
from util.data_handler import dataHandler


@allure.feature("客户端用户相关接口")
class TestCourseController:
    @allure.story("获取课程详情的接口")
    def test_case_get_course_details(self):
        params = "cId="+str(GlobalConfig.cId)+"&&userId="+str(GlobalConfig.userId)
        api_info = Basic().get_api_by_name("get_course_details", customize_params=params)
        content = Basic().send_request(**api_info)
        assert content.status_code == 200
        TestCourseController.content_dict = dataHandler().str_to_dict(content.text)# 返回内容中有需要的ctypeId和teacherId
        # print(content.text)
    @allure.story("课程列表关键字搜索")
    def test_case_get_course_search(self):
        dataHandler().traverse_get_list_from_dict(TestCourseController.content_dict)
        value_dict = dataHandler.get_value_dict()
        # print(value_dict)
        ctypeId = value_dict["ctypeId"] # 2
        date = "2020-08-31"
        keyword = "学科"
        pageNum = 1
        pageSize = 10
        customize_body = {"ctypeId": ctypeId,"date": date,"keyword": keyword,"pageNum": pageNum,"pageSize": pageSize}
        api_info = Basic().get_api_by_name("get_course_search", customize_body=customize_body)
        # print(api_info)
        content = Basic().send_request(**api_info)
        assert content.status_code == 200
        # print(content.text)


