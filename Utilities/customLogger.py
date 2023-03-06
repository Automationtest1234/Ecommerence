import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        handler = logging.FileHandler('D:\\Ecommerence\\Logs\\automation.log')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
