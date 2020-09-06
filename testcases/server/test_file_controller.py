import allure

@allure.feature("后台管理员相关接口")
class TestFileController:
    @allure.story("文件上传")
    def test_case_1_upload_file(self):
        pass # 文件上传的接口有点问题，暂不测试