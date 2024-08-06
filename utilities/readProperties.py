import configparser
# from ConfigParser import RawConfigParser
config= configparser.RawConfigParser()

from configparser import ConfigParser
# config=ConfigParser()
config.read("C:\\Users\\91869\\SeleniumPytestwithPOM\\Configurations\\config.ini")
# print(config.get("common_info","username"))

class readConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common_info','baseUrl')
        return url
    @staticmethod
    def getuseremail():
        useremail=config.get('common_info','username')
        return useremail
    @staticmethod
    def getuserpasswd():
        userpass=config.get('common_info','password')
        return userpass
#
# print(readConfig.getApplicationUrl())
# print(readConfig.getuseremail())
# print(readConfig.getuserpasswd())