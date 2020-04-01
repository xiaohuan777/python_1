import allure
import re, json, random
from aiwd.api.QuestionsPages import getQuestionsPages
from aiwd.util.ConnectMysql import mysql_query
from aiwd.util.ReFind import reFind

@allure.feature('问题列表')
class TestClass:

    def commonAssert(self, response, pattern):
        assert response['code'] == 1
        assert response['errorMessage'] == 'OK'
        assert len(response['data']['list']) > 0
        items_f = reFind(pattern, json.dumps(response))
        assert len(items_f) == len(response['data']['list'])
        list_one = random.choice(response['data']['list'])
        id = list_one['id']
        sql = "select * from t_question where id = '" + str(id) + "'"
        result = mysql_query(sql, 'mysql', 'rjhy_ai')
        assert list_one['isExample'] == result[4]
        assert list_one['isHot'] == result[5]
        assert list_one['isKeyword'] == result[6]
        assert list_one['name'] == result[7]
        assert list_one['category'] == result[9]

    @allure.story('正常case(默认不传参)')
    # 显示15条
    def test_success_noparams(self):
        response = getQuestionsPages()
        print(response)
        assert response['code'] == 1
        assert response['errorMessage'] == 'OK'
        sql = "select count(*) from t_question"
        assert response['data']['totalNumber'] == mysql_query(sql, 'mysql', 'rjhy_ai')[0]
        assert len(response['data']['list']) == 15

    @allure.story('正常case(展示isHot热门问题)')
    def test_success_isHot(self):
        response = getQuestionsPages(isHot=1)
        print(response)
        self.commonAssert(response, '"isHot": 1')

    @allure.story('正常case(展示isKeyword关键问题)')
    def test_success_isKeyword(self):
        response = getQuestionsPages(isKeyword=1)
        print(response)
        self.commonAssert(response, '"isKeyword": 1')

    @allure.story('正常case(展示isExample示例问题)')
    def test_success_isExample(self):
        response = getQuestionsPages(isExample=1)
        print(response)
        self.commonAssert(response, '"isExample": 1')

    @allure.story('正常case(展示category为股票)')
    def test_success_category_stock(self):
        response = getQuestionsPages(category='stock')
        print(response)
        self.commonAssert(response, '"category": "stock"')

    @allure.story('正常case(展示category为板块)')
    def test_success_category_plate(self):
        response = getQuestionsPages(category='plate')
        print(response)
        self.commonAssert(response, '"category": "plate"')

    @allure.story('正常case(展示category为大盘)')
    def test_success_category_index(self):
        response = getQuestionsPages(category='index')
        print(response)
        self.commonAssert(response, '"category": "index"')

    @allure.story('正常case(展示1条数据)')
    def test_success_category_stock(self):
        response = getQuestionsPages(pageSize=1)
        print(response)
        self.commonAssert(response, '"category"')

    @allure.story('正常case(展示第二页数据)')
    def test_success_category_stock(self):
        response = getQuestionsPages(pageSize=1, pageNo=2)
        print(response)
        self.commonAssert(response, '"category"')
        sql = 'select id from t_question ORDER BY id desc limit 1,1'
        result = mysql_query(sql, 'mysql', 'rjhy_ai')
        assert response['data']['list'][0]['id'] == result[0]