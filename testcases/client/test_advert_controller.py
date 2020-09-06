

import allure

from common.basic_handler import Basic
from config.global_config import GlobalConfig
from util.data_handler import dataHandler


@allure.feature("客户端用户相关接口")
class TestAdvertController:
    index_content_list = []
    @allure.story("根据广告位置获取广告的接口")
    def test_get_index_advert(self):

        for advert_index in GlobalConfig.adver_index_list:
            # print(advert_index)
            params = "position="+str(advert_index)
            api_info = Basic().get_api_by_name("get_index_advert",customize_params=params)
            content = Basic().send_request(**api_info)
            assert content.status_code == 200
            # print(content.text)
            self.index_content_list.append(dataHandler().str_to_dict(content.text))

    @allure.story("根据id获取广告详情的接口")
    def test_get_id_advert(self):
        # print(self.index_content_list)
        for content in self.index_content_list:
            dataHandler().traverse_get_list_from_dict(content)
        advertId_list = dataHandler.get_advertId_list()
        for advertId in advertId_list: # 23
            params = "advertId=" + str(advertId)
            api_info = Basic().get_api_by_name("get_id_advert", customize_params=params)
            content = Basic().send_request(**api_info)
            assert content.status_code == 200