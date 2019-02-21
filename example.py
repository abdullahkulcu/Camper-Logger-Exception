from Camper.ExceptionCatcher import CamperException
from Camper.Log import CamperLogger

logger = CamperLogger(logger_name=__name__, debug=True, record=True, log_path="/usr/log")


def ptask(value):
    print(value)


def error_task(err):
    logger.warning(message=err)


@CamperException.exception_catcher(default=5, record=False, post_endpoint="https://b03ed604.ngrok.io/create/log",
                                   extra="outbox")
def example(value, callback):
    print(None["1"])


example(0, "dwdwd")
