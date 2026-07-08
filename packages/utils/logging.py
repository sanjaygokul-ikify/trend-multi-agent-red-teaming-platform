import logging

class Logging:
    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)

    def info(self, message: str):
        self.logger.info(message)