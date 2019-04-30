# utf-8
import unittest
import json
import HTMLTestRunner
from mock import mock
from Run import RunMain
from mock_fun import mock_main

class TestMethod(unittest.TestCase):

    '''   
    @classmethod
    def setUpClass(cls):
        print('类执行之前的方法')
    
    @classmethod
    def tearDownClass(cls):
        print('类执行之后的方法')
    '''

    def setUp(self):
        pass


    def test_case1(self):
        url1='http://127.0.0.1:8000/login/'
        url2 = 'https://api.douban.com/v2/book/30163860'
        data1 = {
            'username': 'xiaohuan',
            'password': 123456
        }
        # mock_data = mock.Mock(return_value=data1)
        # Run.RunMain = mock_data
        response = mock_main(RunMain, url1, data1, data1)

        # response = Run.RunMain(url1, data1)
        self.assertEqual(response['username'], 'xiaohuan', 'test is failed')

        # 模拟URL2，get请求
        '''
        response = Run.RunMain(url2)
        res_dict = json.loads(response.res)
        self.assertEqual(res_dict['price'], '39.00元', '失败')
        self.assertEqual(res_dict['price'], '9.00元', '失败')
        '''
        # global a

    def test_case2(self):
        pass
        # a = 2
        # print(a)

    @unittest.skip('test_case3')
    def test_case3(self):
        pass
        
    def tearDown(self):
        print('over')

'''
# 方案一
if __name__ == '__main__':
    unittest.main()
'''

if __name__ == '__main__':
    filename = r'D:\python_files\interface\report\report.html'
    fp = open(filename, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_case1'))
    suite.addTest(TestMethod('test_case2'))
    # runner = HTMLTestRunner.HTMLTestRunner(fp, title='this is a report')
    # runner.run(suite)
    unittest.TextTestRunner().run(suite)

