def bold(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'

    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return '<b>' + func(*args, **kwargs) + '</b>'

    return wrapper


@italic
@bold
def foo(arg):
    return f"Test {arg}"


print(foo(1))
