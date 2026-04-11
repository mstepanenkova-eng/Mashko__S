from functools import wraps


def singledispatch(f):
    type_to_function = {}

    @wraps(f)
    def wrapper(*args, **kwargs):
        if not args:
            return f(*args, **kwargs)

        arg_type = type(args[0])
        if arg_type in type_to_function:
            return type_to_function[arg_type](*args, **kwargs)
        else:
            return f(*args, **kwargs)

    def register(f):
        name = f.__code__.co_varnames[0]
        typ = f.__annotations__.get(name)
        type_to_function[typ] = f
        return f

    wrapper.register = register

    return wrapper


@singledispatch
def f(x):
    print('no')
    return x

@f.register
def _(x: int):
    print(f'im int: {x}')



@f.register
def _(x: str):
    print(f'im str: {x}')



if __name__ == '__main__':
    f('hgjf')

