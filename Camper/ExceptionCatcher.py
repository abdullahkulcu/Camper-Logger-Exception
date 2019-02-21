import requests
import asyncio


class CamperException:
    def __init__(self):
        pass

    @staticmethod
    @asyncio.coroutine
    def __post_error_message(url, message, extra):
        try:
            body = {"error": message, "extra": extra}
            requests.post(
                url=url,
                json=body
            )
        except Exception as e:
            from .Log import CamperLogger
            logger = CamperLogger('camper_exception', record=True)
            logger.error(e)

    @classmethod
    def exception_catcher(cls, **kwargs):
        default = kwargs.get('default')
        default_callback = kwargs.get('callback')
        error_callback = kwargs.get('error_callback')
        log_path = kwargs.get('log_path')
        record = kwargs.get('record')
        post_endpoint = kwargs.get('post_endpoint')
        extra_data = kwargs.get('extra')

        def wrapper(func):
            def run_func(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    from .Log import CamperLogger
                    logger = CamperLogger('camper_exception', log_path=log_path, record=record)
                    err = " Path : {path} \n" \
                          " Function : {func} \n" \
                          " Error: {error}".format(
                        path=str(func.__code__.co_filename),
                        func=func.__name__,
                        error=e
                    )
                    if post_endpoint is not None and type(post_endpoint) == str and len(post_endpoint) > 0:
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(
                            cls.__post_error_message(url=post_endpoint, message=str(e), extra=extra_data))
                        loop.close()
                    if error_callback is not None:
                        error_callback(e)
                    logger.error(err)
                    if default_callback is not None:
                        return default_callback(default)
                    return default

            return run_func

        return wrapper
