import allure, pytest
class Test_001:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="第一个测试方法")
    def test_001_1(self):
        allure.attach("test_001_1","这是test_001_1的步骤描述")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="第二个测试方法")
    def test_002_2(self):
        allure.attach("test_001_2", "这是test_001_2的步骤描述")
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="第三个测试方法")
    def test_003_3(self):
        allure.attach("test_003_3", "这是test_003_3的步骤描述")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="第四个测试方法")
    def test_004_4(self):
        allure.attach("test_004_4", "这是test_004_4的步骤描述")
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="第四个测试方法")
    def test_005_5(self):
        allure.attach("test_005_4", "这是test_005_4的步骤描述")
        assert 0