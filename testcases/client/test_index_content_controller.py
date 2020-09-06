import allure

from common.basic_handler import Basic


@allure.feature("客户端用户相关接口")
class TestIndexContentController:
    @allure.story("获取首页展示内容1")
    def test_case1_get_home_page_content(self):
        api_info = Basic().get_api_by_name("get_home_page_content")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200

    @allure.story("获取首页展示内容2")
    def test_case2_get_home_page_content(self):
        api_info = Basic().get_api_by_name("get_home_page_content2")
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200