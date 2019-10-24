import allure
import pytest


class Test02:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="执行登录")
    def test01(self):
        assert 0
        allure.attach("失败原因：","验证码错误！")
        pass

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="执行退出登录")
    def test02(self):
        allure.attach("失败原因：","密码错误！")
        pass

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        allure.attach("失败原因：","密码错误！")
        pass

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test04(self):
        assert 0
        pass

    def test05(self):
        # 失败截图
        #allure.attach("失败原因：",图片流,图片类型)
        with open("./image/err.png","rb") as f:
            allure.attach("失败原因：",f.read(),allure.attach_type.PNG)
        pass