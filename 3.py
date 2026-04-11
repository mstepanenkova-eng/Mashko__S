def wraps(f):
    def dec(wrapper):
        def wrapper(*args, **kwargs):
            return wrapper(*args, **kwargs)

        wrapper.__name__ = f.__name__
        wrapper.__doc__ = f.__doc__
        wrapper.__module__ = f.__module__
        return wrapper

    return dec

def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(f'{f.__name__}', f'arguments: {args}, kwargs: {kwargs}, res: {res}')
        return res
    return wrapper


@trace
def anekdot():
    """Папа подари мне парту"""
    print('hi!')
    return None

if __name__ == '__main__':
    print(anekdot.__name__)
    print(anekdot.__doc__)