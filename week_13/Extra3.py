from datetime import datetime

def log_call(func):
    def wrapper(*args, **kwargs):

        name = func.__name__
        execution_moment = datetime.now()
        result = (func(*args, **kwargs))
        print(f"func: {name} - args: {args,kwargs} - date: {execution_moment} - result: {result}")

        return result
    return wrapper

def validate_numbers(func):
    def wrapper(*args, **kwargs):
        for item in args:
            if not isinstance(item,(int,float)):
                raise TypeError ("All parameters must be numbers")

        for item in kwargs.values():
            if not isinstance(item,(int,float)):
                raise TypeError ("All parameters must be numbers")
            
        return func(*args, **kwargs)

    return wrapper

@validate_numbers
@log_call
def multiply(a, b):
    return a * b

multiply(5,6)