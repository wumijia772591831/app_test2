import allure,pytest
class Test:

    @allure.step(title="第一个测试")
    def test_01(self):
        assert True

    @allure.step(title="第二个测试")
    def test_02(self):
        assert False
