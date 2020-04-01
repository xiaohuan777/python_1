import allure
from aiwd.api.QueryAiInfotByAppCode import getQueryAiInfotByAppCode
from aiwd.util.ConnectMysql import mysql_query

@allure.feature('AI介绍页、欢迎语')
class TestClass:

    @allure.story('正常case')
    def test_success(self):
        response = getQueryAiInfotByAppCode()
        print(response)
        assert response['code'] == 1
        assert response['errorMessage'] == 'OK'
        id = str(response['data']['id'])
        sql = "select * from t_ai_info where id = '" + id + "'"
        result = mysql_query(sql, 'mysql', 'rjhy_ai')
        assert response['data']['headImage'] == result[5]
        assert response['data']['greetings'] == result[4]
        assert response['data']['info'] == result[6]
        assert response['data']['status'] == 0