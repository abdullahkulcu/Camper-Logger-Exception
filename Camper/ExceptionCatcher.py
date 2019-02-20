def exception_catcher(*args, default=None, callback=None, error_callback=None, log_path=None, record=True):
    def wrapper(func):
        from .Log import CamperLogger
        logger = CamperLogger('camper_exception', log_path=log_path, record=record)
        try:
            return func(*args)
        except Exception as e:
            err = " Path : {path} \n" \
                  " Function : {func} \n" \
                  " Error: {error}".format(
                path=str(func.__code__.co_filename),
                func=func.__name__,
                error=e
            )
            if error_callback is not None:
                error_callback(e)
            logger.error(err)
            if callback is not None:
                return callback(default)
            return default

    return wrapper
