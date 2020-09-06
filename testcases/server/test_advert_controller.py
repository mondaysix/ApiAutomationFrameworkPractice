import allure

from common.basic_handler import Basic
from util.data_handler import dataHandler


@allure.feature("后台管理员相关接口")
class TestAdvertController:
    advert_id = 0
    @allure.story("新增广告")
    def test_case_1_add_advert(self):
        body = {"advertId": 814, "link": "123456", "linkContent": "123456",
                "linkId": "123456", "photo": "123456", "position": 1,
                "title": "123456", "type": 1}
        api_info = Basic().get_api_by_name("add_advert_edu_teacher", customize_body=body)
        content = Basic().send_request(**api_info)
        # print(content.text)
        dataHandler().traverse_get_list_from_dict(dataHandler().str_to_dict(content.text))
        advertId_list = dataHandler.get_advertId_list()
        # print(advertId_list)
        TestAdvertController.advert_id = advertId_list[0]
        assert content.status_code == 200

    @allure.story("根据id查询广告")
    def test_case_2_find_advert_by_id(self):
        param = "advertId="+str(self.advert_id)
        api_info = Basic().get_api_by_name("find_advert_by_id",customize_params=param)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200

    @allure.story("根据id修改广告信息")
    def test_case_3_update_advert_by_id(self):
        body = {"advertId": self.advert_id, "link": "customize_link", "linkContent": "customize_content",
                "linkId": "1", "photo": "photo", "position": 2,
                "title": "mytitle", "type": 2}
        api_info = Basic().get_api_by_name("update_advert_by_id", customize_body=body)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200

    @allure.story("根据id和status修改广告状态")
    def test_case_4_update_advert_by_status(self):
        param= "advertId="+str(self.advert_id)+"&&status="+str(2)
        api_info = Basic().get_api_by_name("update_advert_by_status", customize_params=param)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        assert content.text == "{\"code\":1000,\"msg\":\"修改成功\"}"

    @allure.story("根据id删除广告")
    def test_case_5_del_advert_by_id(self):
        param = "advertId="+str(self.advert_id)
        # print(param)
        api_info = Basic().get_api_by_name("del_advert_by_id", customize_params=param)
        content = Basic().send_request(**api_info)
        # print(content.text)
        assert content.status_code == 200
        assert content.text == "{\"code\":1000,\"msg\":\"删除成功\"}"
