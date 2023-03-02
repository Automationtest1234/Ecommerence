import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="newfiles.log",
                            format='%(asctime)s %(message)s',
                            filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
