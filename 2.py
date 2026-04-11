from functools import wraps
from warnings import warn

def mock(return_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return return_value

        return wrapper

    return decorator


@mock(return_value='pomogite')
def g(x):
    return x


if __name__ == '__main__':
    print(g(5))
