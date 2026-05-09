from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
#
# print(config.get("basic info","browserName"))
# print(config.get("basic info","URL"))
# print(config.get("mobile","executionOS"))
class ConfigReader:
    def readConfig(self,section,key):
        config = ConfigParser()
        config.read("testData/config.ini")
        return config.get(section,key)

# print(readConfig("basic info","URL"))
# print(readConfig("basic info","browserName"))
# print(readConfig("mobile","executionOS"))