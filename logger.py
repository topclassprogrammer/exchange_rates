import logging
from datetime import datetime

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'

class Logger:
    def __init__(self):
        self.format = LOG_FORMAT
        self.level = LOG_LEVEL
        self.logger = logging.getLogger()
        self.logger.setLevel(self.level)
        formatter = logging.Formatter(self.format)
        file_handler = logging.FileHandler(f'{datetime.today().date()}.log')  # Сохранение в файл. Если нужно, чтобы только выводилось в консоль, то нужно вместо logging.FileHandler(...) создавать logging.StreamHandler()
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)


logger = Logger().logger
