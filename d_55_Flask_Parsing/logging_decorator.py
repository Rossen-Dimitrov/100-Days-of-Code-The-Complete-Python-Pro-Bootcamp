inputs = eval(input())


# TODO Create logging_decorator() function

def logging_decorator(fn):
    def wrapper(*args):
        print(f"You called {fn.__name__}{args}")
        print(f"It returned: {fn(*args)}")
    return wrapper


@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
