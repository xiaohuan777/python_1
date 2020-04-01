import allure
from aiwd.api.Chat import postChat

@allure.feature('AI机器人聊天')
class TestClass:

    @allure.story('正常case_个股地区')
    def test_success(self):
        response = postChat('张江高科属于什么地区')
        print(response)
        assert response['code'] == 0
        assert response['errorMessage'] == 'OK'


