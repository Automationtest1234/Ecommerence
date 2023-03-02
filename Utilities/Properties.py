import configparser

config = configparser.ConfigParser()
config.read(".\\Configurations\\config.ini")


class Config:
    @staticmethod
    def BaseURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def GetUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common info', 'password')
        return password

