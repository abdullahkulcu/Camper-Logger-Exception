from Camper.ExceptionCatcher import CamperException
from Camper.Log import CamperLogger

logger = CamperLogger(logger_name=__name__, debug=True, record=True)


def ptask(value):
    logger.warning("coming:" + str(value), file_name="DAWDW")


def error_task(err):
    logger.warning(message=err)


catch = CamperException(sentry_dns="https://b76a7c54e65d4f2d8bbb8bcb6a66b3d2@sentry.io/1505962").exception_catcher(
    default="test", record=False, callback=ptask, error_callback=error_task)


@catch
def example(value, callback):
    print(None["1"])


example(0, "dwdwd")
