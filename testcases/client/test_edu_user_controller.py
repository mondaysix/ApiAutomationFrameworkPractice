# coding:utf-8

import allure
from common.basic_handler import Basic


@allure.feature("客户端用户相关接口")
class TestEduUserController:

    @allure.story("查询用户信息接口")
    def test_case_1_get_edu_user_info(self):
        api_info = Basic().get_api_by_name("get_user_list")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200#查看响应码

    @allure.story("查询用户信息接口")
    def test_case_2_get_edu_user_info(self):
        api_info = Basic().get_api_by_name("get_edu_user_info")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200  # 查看响应码

    @allure.story("查询用户昵称和头像的接口")
    def test_case__get_edu_user_name_photo(self):
        api_info = Basic().get_api_by_name("get_edu_user_name_photo")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200  # 查看响应码


