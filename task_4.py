from functools import wraps


x = 10
def valid():
    if x > 0:
        return True
    else:
        return False


def val_checker(val):
    def _val_checker(func):
        @wraps(func)
        def wrapped(arg):
            if val == True:
                res = func(arg)
                print(res)
            else:
                raise ValueError(f'wrong val {arg}')

        return wrapped

    return _val_checker


@val_checker(val=valid())
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    calc_cube(x)


