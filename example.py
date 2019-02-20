from Camper.ExceptionCatcher import exception_catcher
from Camper.Log import CamperLogger

logger = CamperLogger(__name__, debug=True, record=True)


def ptask(value):
    print(value)


def error_task(err):
    logger.warning(message=err)


@exception_catcher(default=1, callback=ptask, error_callback=error_task, record=True)
def example():
    a = 1 / 0
    print(a)


if __name__ == "__main__":
    example
