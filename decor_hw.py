from datetime import datetime
from math import pow
import requests, os

LOG_FILE = 'decor_logs.txt'
BASE_PATH = os.getcwd()
FULL_PATH_TOLOG = os.path.join(BASE_PATH,LOG_FILE)
URL = 'https://dzen.ru/?clid=2270456&win=558&yredirect=true'

def logger(func):
    def wrapper(*args):
        date_time = datetime.now()
        func_name = func.__name__
        result = func(*args)
        with open(FULL_PATH_TOLOG, 'a', encoding='utf-8') as f:
            f.write(f'Дата/время: {date_time}\n'
                    f'Имя функции: {func_name}\n'
                    f'Аргументы: {args}\n'
                    f'Результат: {result}\n')
        return result
    return wrapper


def logger_parametrized(path):
    def decor(func):
        def wrapper(*args):
            date_time = datetime.now()
            func_name = func.__name__
            result = func(*args)
            with open(path, 'a', encoding='utf-8') as f:
                f.write(f'Дата/время: {date_time}\n'
                        f'Имя функции: {func_name}\n'
                        f'Аргументы: {args}\n'
                        f'Результат: {result}\n')
            return result
        return wrapper
    return decor



@logger
def inside_counter(a,b):
    return pow(a,b)

@logger_parametrized(FULL_PATH_TOLOG)
def get_req(URL):
    resp = requests.get(URL)
    return resp.status_code


if __name__ == '__main__':
    print(inside_counter(2,4))
    get_req(URL)
    
