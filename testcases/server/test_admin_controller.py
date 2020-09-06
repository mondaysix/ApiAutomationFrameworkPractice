# coding:utf-8

from config.global_config import GlobalConfig
from common.basic_handler import Basic
import allure

from util.data_handler import dataHandler


@allure.feature("后台管理员相关接口")
class TestAdminController:
    cookies = GlobalConfig.cookies
    base_url = GlobalConfig.base_url
    admin_info = {}
    # @allure.story("获取某管理员信息")
    # def test_case_1_get_admin_info(self):
    #     api_info = Basic().get_api_by_name("get_admin_by_id")
    #     content = Basic().send_request(**api_info)
    #     print(content.text)
    #     assert content.status_code == 200

    @allure.story("通过ID获取管理员信息")
    def test_case_1_get_admin_by_id(self):
        admin_id = "1"
        api_info = Basic().get_api_by_name("get_admin_by_id")
        response = Basic().send_request(admin_id, **api_info)
        assert response.status_code == 200
        content_dict = dataHandler().str_to_dict(response.text)
        dataHandler().traverse_get_list_from_dict(content_dict)
        TestAdminController.admin_info = dataHandler.get_admin_info_dict()
        # print(TestAdminController.admin_info)

    @allure.story("获取管理员列表")
    def test_case_2_get_admin_list(self):
        # print(self.admin_info)
        customize_admin_info = self.admin_info
        customize_admin_info["pageNum"] = 1
        customize_admin_info["pageSize"] = 10
        api_info = Basic().get_api_by_name("get_admin_list",customize_body=customize_admin_info)
        content = Basic().send_request(**api_info)
        assert content.status_code == 200
        # print(content.text)

    @allure.story("管理员登录")
    def test_case_3_admin_login(self):
        body = {"username": "admin", "password": "123456"}
        api_info = Basic().get_api_by_name("get_admin_login", customize_body=body)
        content = Basic().send_request(**api_info)
        assert content.status_code == 200

