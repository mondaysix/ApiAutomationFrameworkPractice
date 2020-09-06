# coding:utf-8

from config.global_config import GlobalConfig
from util import helper
import json
import csv
import re
import requests


class Basic(GlobalConfig):

    @property
    def get_api_list(self):
        """

        :return: 返回以api_name为键，api对应信息为值的字典
        """
        api_all = {}
        api_list_path = self.root_path + "/api_list/" + self.client_or_server + "/" + self.client_or_server + "_apis.csv"
        try:
            with open(api_list_path, 'r') as csv_f:  # , encoding='UTF-8'
                content = csv.DictReader(csv_f)
                data = {row.pop("api_name"): row for row in content}  # 取出每行数据，以每行数据第一个单元格作为key，剩下的作为value
                api_all.update(data)
            return api_all
        except FileNotFoundError:
            print(api_list_path, "File Not Found!")

    @staticmethod
    def customize_api_params(params):
        if params:
            if isinstance(params, str):
                params = helper.cn_trans_en(params)
                params = json.loads(params)#用于将str转换为dict
        else:
            params = dict()
        return params

    @staticmethod
    def customize_api_header(header):
        if header:
            header = eval(header)
            try:
                header["Authorization"] = GlobalConfig.cookies
            except KeyError:
                return -1
        else:
            header = dict()
            header["Authorization"] = GlobalConfig.cookies
        return header

    @staticmethod
    def customize_api_body(body):
        if body:
            body = json.dumps(body)  # 用于将dict类型的数据转成str
        else:
            body = dict()
        return body

    def get_api_by_name(self, api_name, customize_params=None, customize_body=None):
        """

        :param api_name: 传入指定api_list中对应的api_name
        :param customize_params: 传入指定api_list中特定的params
        :param customize_body: 传入指定api_list中特定的body
        :return: 整个api相关信息，包含uri，params，body等
        """
        api_info = self.get_api_list[api_name]
        header = api_info["header"]
        params = api_info["params"]
        body = api_info["body"]
        # 确保api的params合规范
        if customize_params:
            # print(customize_params)
            api_info["params"] = customize_params
        else:
            api_info["params"] = self.customize_api_params(params)

        # 确保api的header合规范
        api_info["header"] = self.customize_api_header(header)
        # 确保body符合规范
        if customize_body:
            # print(customize_body)
            api_info["body"] = self.customize_api_body(customize_body)
        else:
            api_info["body"] = body
        return api_info

    def send_request(self, uri_id=None, **api_info):
        uri = api_info["uri"]
        method = api_info["method"]
        header = api_info["header"]
        params = api_info["params"]
        body = api_info["body"]
        matching_regex = re.search(r"{.*}", uri)
        if matching_regex:
            if uri_id:
                replace_params = matching_regex.group()
                uri = uri.replace(replace_params, str(uri_id))
        url = self.base_url + uri
        # body2="{\"pageNum\": \"1\",\"pageSize\": \"10\",\"userId\":\"15\",\"state\":\"0\"}"
        if method in ("POST", "post"):
            resp = requests.post(url, headers=header, params=params, data=body)
        elif method in ("GET", "get"):
            resp = requests.get(url, headers=header, params=params)
        elif method in ("PUT", "put"):
            pass
        elif method in ("DELETE", "delete"):
            pass
        else:
            print("!!!!!Other api method does not support!!!!!")
            return -1
        return resp
