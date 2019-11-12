# coding:utf-8

# 封装定位方式
class GetByLocal():
    def __init__(self, driver):
        self.driver = driver

    def get_by_ele(self, key):
        # name=email
        by = key.split('=')[0]
        by_value = key.split('=')[1]
        if by == 'id':
            return self.driver.find_element_by_id(by_value)
        elif by == 'name':
            return self.driver.find_element_by_name(by_value)
        elif by == 'classname':
            return self.driver.find_element_by_class_name(by_value)
        elif by == 'link_text':
            return self.driver.find_element_by_link_text(by_value)
        elif by == 'partial_link_text':
            return self.driver.find_element_by_partial_link_text(by_value)
        elif by == 'tagname':
            return self.driver.find_element_by_tag_name(by_value)
        elif by == 'css_selector':
            return self.driver.find_element_by_css_selector(by_value)
        else:
            return self.driver.find_element_by_xpath(by_value)

