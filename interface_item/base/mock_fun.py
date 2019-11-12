# coding:utf-8

from mock import mock

def mock_main(mock_method, url, request_data, response_data):
    mock_data = mock.Mock(return_value=response_data)
    mock_method = mock_data
    res = mock_method(url, request_data)
    return res
