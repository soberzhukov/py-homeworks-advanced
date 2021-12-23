import logging
from generator import read_file


def parametrized_logging_decorator(path):
    default_path = 'info.log'
    if path:
        default_path = path
    logging.basicConfig(
        filename=default_path,
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )

    def logging_decorator(old_function):

        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            logging.debug(
                f'Имя функции: {old_function.__name__} c '
                f'аргументами: {[*args]}, {dict(**kwargs)}. '
                f'Результат: {result}'
            )

            return result

        return new_function

    return logging_decorator


function = parametrized_logging_decorator(path=False)(read_file)

for i in function('diff.txt'):
    print(i)
