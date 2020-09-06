import json


class dataHandler:
    cid = 0
    advert_id = 0
    value_dict = {}
    type_list = []
    advertId_list = []
    teacherId_list = []
    clabelId_list = []
    admin_info_dict = {}
    def __init__(self):
        self.value_list = []

    @classmethod
    def getCid(cls):
        return cls.cid

    def str_to_dict(self, text):
        if text:
            dict_text = json.loads(text)
            return dict_text
        else:
            return None
    """
        :param data:字典嵌套列表
        :param pidList:返回的值
        :return:列表
    """
    def traverse_get_list_from_dict(self, data):
        if isinstance(data, list):
            for i in data:
                if isinstance(i, dict):
                    self.traverse_get_list_from_dict(i)
        if isinstance(data, dict):
            for key, value in data.items():
                if "pid" == key:
                    self.value_list.append(value)
                elif "clabelId" == key:
                    self.clabelId_list.append(value)
                elif "cId" == key:
                    self.value_list.append(value)
                elif "ctypeId" == key:
                    self.value_dict["ctypeId"] = value
                elif "teacherId" == key:
                    self.teacherId_list.append(value)
                elif "type" == key:
                    self.type_list.append(value)
                elif "advertId" == key:
                    self.advertId_list.append(value)
                elif "adminId" == key:
                    self.admin_info_dict[key] = value
                elif "chineseName" == key:
                    self.admin_info_dict[key] = value
                elif "phone" == key:
                    self.admin_info_dict[key] = value
                elif "roleId" == key:
                    self.admin_info_dict[key] = value
                elif "status" == key:
                    self.admin_info_dict[key] = value
                elif "userName" == key:
                    self.admin_info_dict[key] = value
                else:
                    self.traverse_get_list_from_dict(value)
        # if getlist:
        #     print("getList:%d", len(getlist))
        return set(self.value_list)#去掉重复的元素
    @classmethod
    def get_value_dict(cls):
        return cls.value_dict

    @classmethod
    def get_type_list(cls):
        return cls.type_list

    @classmethod
    def get_advertId_list(cls):
        return cls.advertId_list

    @classmethod
    def get_teacherId_list(cls):
        return set(cls.teacherId_list)

    @classmethod
    def get_clabelId_list(self):
        return self.clabelId_list

    @classmethod
    def get_admin_info_dict(self):
        return self.admin_info_dict


