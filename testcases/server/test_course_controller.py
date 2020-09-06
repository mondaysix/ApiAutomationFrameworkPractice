import allure

from common.basic_handler import Basic


@allure.feature("后台管理员相关接口")
class TestCourseController:
    @allure.story("获取课程类型")
    def test_case_2_get_course_list_type(self):
        api_info = Basic().get_api_by_name("get_course_list_type")
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200

    # @allure.story("新增课程表")
    # def test_case_1_add_course(self):
    #     body = {}
    #     body["cid"] = 1646
    #     body["counselorId"] = 16
    #     body["courseResourceDtos"]=[{"cid": 100, "cresId": 10, "date": "2020-09-05", "endTime": "2020-09-05T23:59:01.367Z",
    #          "liveStream": "string", "name": "string","sort": 0,"startTime": "2020-09-05T23:59:01.367Z",
    #          "state": 0, "videoUrl": "string"}]
    #     body["ctypeId"] = 103
    #     api_info = Basic().get_api_by_name("add_course", customize_body=body)
    #     print(api_info)
    #     content = Basic().send_request(**api_info)
    #     print(content.text)
    #     assert content.status_code == 200


