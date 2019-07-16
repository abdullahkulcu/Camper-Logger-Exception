import logging
import colorlog
from .Static import *
from Camper.ExceptionCatcher import CamperException


def error_handler(err):
    print(err)


class CamperLogger:

    @CamperException.exception_catcher(error_callback=error_handler)
    def __init__(self, logger_name, **kwargs):
        self.name = logger_name
        self.debug = kwargs.get('debug')
        self.log_path = kwargs.get('log_path')
        self.record = kwargs.get('record')
        self.logger = None
        self.__init_logger()

    @CamperException.exception_catcher(error_callback=error_handler)
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

    @CamperException.exception_catcher(error_callback=error_handler)
    def warning(self, message, file_name="app-warning"):
        if self.logger is not None and message is not None:
            if self.record:
                file_name = "app-warning" if file_name is None or file_name == "" else file_name
                file_name = file_name.replace(".", "")
                fh = logging.FileHandler(self.log_path + (file_name + '.log'))
                fh.setLevel(logging.WARNING)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.warning(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.warning(message)

    @CamperException.exception_catcher(error_callback=error_handler)
    def error(self, message, file_name="app-error"):
        if self.logger is not None and message is not None:
            if self.record:
                file_name = "app-error" if file_name is None or file_name == "" else file_name
                file_name = file_name.replace(".", "")
                fh = logging.FileHandler(self.log_path + (file_name + '.log'))
                fh.setLevel(logging.ERROR)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.error(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.error(message)

    @CamperException.exception_catcher(error_callback=error_handler)
    def info(self, message, file_name="app-info"):
        if self.logger is not None and message is not None:
            if self.record:
                file_name = "app-info" if file_name is None or file_name == "" else file_name
                file_name = file_name.replace(".", "")
                fh = logging.FileHandler(self.log_path + (file_name + '.log'))
                fh.setLevel(logging.INFO)
                formatter = logging.Formatter(log_format)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)
                self.logger.info(message)
                self.logger.removeHandler(fh)
            else:
                self.logger.info(message)
