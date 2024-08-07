import time


def speed_calc_decorator(function):
    def wrapper_func():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} - {end_time - start_time}")

    return wrapper_func


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        a = i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        a = i * i


fast_function()
slow_function()
