from warnings import warn
import warnings
from functools import wraps

def depr_v2(text):
    def depr(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            warnings.warn(text)
            return f(*args, **kwargs)

        return wrapper
    return depr

@depr_v2("NOOOOOOOOOOOOOO")
def f(x):
    return x


if __name__ == '__main__':
    print(f(67))
