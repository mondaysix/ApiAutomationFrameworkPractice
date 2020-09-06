import allure

from common.basic_handler import Basic
from util.data_handler import dataHandler


@allure.feature("后台管理员相关接口")
class TestTeacherController:
    teacher_id = 0
    # @allure.story("新增老师信息")
    # def test_case_1_add_teacher(self):
    #     body = {
    #         "advertPhoto": "string",
    #         "detailIntruduction": "string",
    #         "educationalBackground": 3,
    #         "graduatedSchool": "Gongye大学",
    #         "headPhoto": "string",
    #         "name": "wuming",
    #         "phone": "12937890789",
    #         "positional": "中级",
    #         "recommend": 1,
    #         "sex": 2,
    #         "summary": "英语课程，来这"
    #     }
    #     api_info = Basic().get_api_by_name("add_teacher", customize_body=body)
    #     content = Basic().send_request(**api_info)
    #     print(content.text)
    #     dataHandler().traverse_get_list_from_dict(dataHandler().str_to_dict(content.text))
    #     teacher_id_list = dataHandler.get_teacherId_list()
    #     TestTeacherController.teacher_id = teacher_id_list[0]
    #     # print(teacher_id_list)
    #     assert content.status_code == 200
    @allure.story("根据id查询老师")
    def test_case_2_get_teacher_by_id(self):
        params = "teacherId=25"#+str(self.teacher_id)
        api_info = Basic().get_api_by_name("get_teacher_by_id",customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        # assert content.text == "{\"code\":1000,\"msg\":\"查询成功\"}"
    @allure.story("根据id删除老师")
    def test_case_3_del_teacher_by_id(self):
        params = "teacherId=25"#+str(self.teacher_id)
        api_info = Basic().get_api_by_name("del_teacher_by_id", customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        assert content.text == "{\"code\":1000,\"msg\":\"删除老师成功\"}"
    @allure.story("启用或者停用老师")
    def test_case_4_update_teacher_status_by_id(self):
        params = "teacherId=25"+"&&status=1"
        api_info = Basic().get_api_by_name("update_teacher_status_by_id", customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        assert content.text == "{\"code\":1000,\"msg\":\"修改成功\"}"

    @allure.story("后台修改老师资料")
    def test_case_5_update_teacher_info_by_id(self):
            body = {
                "teacherId": 25,
                "advertPhoto": "string",
                "detailIntruduction": "string",
                "educationalBackground": 3,
                "graduatedSchool": "Gongye大学2",
                "headPhoto": "string",
                "name": "xiaozheng",
                "phone": "12937890734",
                "positional": "中级",
                "recommend": 0,
                "sex": 1,
                "summary": "英语课程，来这ba"
            }
            api_info = Basic().get_api_by_name("update_teacher_info_by_id", customize_body=body)
            content = Basic().send_request(**api_info)
            # print(content.text)
            assert content.status_code == 200
