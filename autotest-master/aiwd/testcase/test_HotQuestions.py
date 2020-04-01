import allure
from aiwd.api.HotQuestions import getHotQuestions
from aiwd.util.ConnectMysql import mysql_query

@allure.feature('热门问题')
class TestClass:

    @allure.story('正常case')
    def test_success(self):
        response = getHotQuestions()
        print(response)
        assert response['code'] == 1
        assert response['errorMessage'] == 'OK'
        category1 = str(response['data'][0]['category'])
        sql1 = "select count(*) from t_question where is_hot = '1' and category = '" + category1 + "'"
        assert len(response['data'][0]['questions']) == mysql_query(sql1, 'mysql', 'rjhy_ai')[0]
        category2 = str(response['data'][0]['category'])
        sql2 = "select count(*) from t_question where is_hot = '1' and category = '" + category2 + "'"
        assert len(response['data'][0]['questions']) == mysql_query(sql2, 'mysql', 'rjhy_ai')[0]
        category3 = str(response['data'][0]['category'])
        sql3 = "select count(*) from t_question where is_hot = '1' and category = '" + category3 + "'"
        assert len(response['data'][0]['questions']) == mysql_query(sql3, 'mysql', 'rjhy_ai')[0]