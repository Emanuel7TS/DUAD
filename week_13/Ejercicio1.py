def print_parameters_and_return(original_function):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        result = original_function(*args, **kwargs)
        print(result)
        return result

    return wrapper

@print_parameters_and_return
def func_to_test():
    return "hi"

func_to_test()