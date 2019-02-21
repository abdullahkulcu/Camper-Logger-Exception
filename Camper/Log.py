import logging
import colorlog
from .Static import *


class CamperLogger:

    def __init__(self, logger_name, **kwargs):
        self.name = logger_name
        self.debug = kwargs.get('debug')
        self.log_path = kwargs.get('log_path')
        self.record = kwargs.get('record')
        self.logger = None
        self.__init_logger()

    def __init_logger(self):
        colorlog.basicConfig(format=colorlog_format)
        self.logger = logging.getLogger(self.name)
        if self.debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        if self.log_path is None or self.log_path == '' or type(self.log_path) != str:
            self.log_path = './'
        elif not self.log_path.endswith('/'):
            self.log_path += '/'

    def warning(self, message):
        if self.logger is not None and message is not None:
            if self.record is not None and self.record:
                fh = logging.FileHandler(self.log_path + 'app-warning.log')
                fh.setLevel(logging.WARNING)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.warning(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.warning(message)

    def error(self, message):
        if self.logger is not None and message is not None:
            if self.record is not None and self.record:
                fh = logging.FileHandler(self.log_path + 'app-error.log')
                fh.setLevel(logging.ERROR)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.error(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.error(message)

    def info(self, message):
        if self.logger is not None and message is not None:
            if self.record is not None:
                fh = logging.FileHandler(self.log_path + 'app-info.log')
                fh.setLevel(logging.INFO)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.info(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.info(message)
