#coding = utf-8
import configparser
cf = configparser.ConfigParser()
cf.read("D:\python\selenium_item\config\LocalElement.ini")
print(cf.get('RegisterElement', 'user_email'))

class ReadIni():
    def __init__(self, file_name=None, node=None):
        if file_name = None:
            file_name = "D:\python\selenium_item\config\LocalElement.ini"
        if node = None:
            self.node = 'RegisterElement'
        else:
            self.node = node
        self.cf = cf.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self):
        self.cf.get(self.node, 'user_email')


if __name__ = '__main__':
    read_init = ReadIni()
    