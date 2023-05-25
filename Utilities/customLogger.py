import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logging.basicConfig(filename="D:\\Ecommerence\\Logs\\automation.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger.setLevel(logging.INFO)
        return logger
