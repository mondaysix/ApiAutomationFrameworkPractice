import allure

from common.basic_handler import Basic


@allure.feature("后台管理员相关接口")
class TestInfoController:
    # @allure.story("新增资讯")
    # def test_case_1_add_information(self):
    #     body = {
    #         "introduction": "新增内容成功了",
    #         "photo": "string",
    #         "source": "测试来源",
    #         "text": "string",
    #         "title": "测试2"
    #     }
    #     api_info = Basic().get_api_by_name("add_information",customize_body=body)
    #     content = Basic().send_request(**api_info)
    #     print(content.text)
    #     assert content.status_code == 200

    @allure.story("根据id查询资讯")
    def test_case_2_get_information_by_id(self):
        params = "informationId=15"
        api_info = Basic().get_api_by_name("get_information_by_id", customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200

    @allure.story("根据id删除资讯")
    def test_case_3_del_information_by_id(self):
        params = "informationId=15"
        api_info = Basic().get_api_by_name("del_information_by_id", customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200

    @allure.story("修改资讯状态")
    def test_case_3_del_information_by_id(self):
        params = "informationId=16&&status=2"
        api_info = Basic().get_api_by_name("update_information_status_by_id", customize_params=params)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        assert content.text == "{\"code\":1000,\"msg\":\"修改成功\"}"

    @allure.story("编辑资讯内容")
    def test_case_3_del_information_by_id(self):
        body = {
            "informationId": 16,
            "introduction": "string",
            "photo": "no",
            "source": "no",
            "text": "wu",
             "title": "change test"
        }
        api_info = Basic().get_api_by_name("update_information_info_by_id", customize_body=body)
        content = Basic().send_request(**api_info)
        print(content.text)
        assert content.status_code == 200
        # assert content.text == "{\"code\":1000,\"msg\":\"修改成功\"}"