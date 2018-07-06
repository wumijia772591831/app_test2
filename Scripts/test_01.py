import allure,pytest
class Test:

    @allure.step(title="第一个测试")
    def test_01(self):
        assert True

    @allure.step(title="第二个测试")
    def test_02(self):
        assert False

    def test_03(self):
        allure.attach("这是描述","这是具体描述内容")
        assert True