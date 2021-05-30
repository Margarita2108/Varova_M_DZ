from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapped(*args):
        print(func.__name__, end=': ')
        for arg in args:
            res = (arg, ': ', type(arg), func(arg), type(func(arg)))
            print(res, end=',')
    return wrapped


@type_logger
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    calc_cube(1, 3.5, -5)
