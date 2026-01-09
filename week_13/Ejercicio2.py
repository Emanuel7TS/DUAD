def validate_numeric_params(test_func):
    def wrapper(*args, **kwargs):
        for item in args:
            if not isinstance(item,(int,float)):
                raise TypeError ("All parameters must be numbers") # me gusta aprender cosas nuevas y acabo de descubrir esta funcion de isinstance

        for item in kwargs.values():
            if not isinstance(item,(int,float)):
                raise TypeError ("All parameters must be numbers") # y presiento que en el futuro va a ser muy util. 

        result = test_func(*args, **kwargs)
        return result

    return wrapper

@validate_numeric_params
def test_func(a,b):
    print("validated")
    return (a+b)

test_func(1,2)
test_func(2,"hola")