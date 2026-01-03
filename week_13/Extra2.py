user_logged_in = True


def requires_login(func):
    def wrapper(*args, **kwargs):
        if not user_logged_in:
            raise PermissionError("User not authenticated")
        return func(*args, **kwargs)
    return wrapper


@requires_login
def show_user():
    print("Showing user profile")


user_logged_in = True
show_user()

user_logged_in = False

try:
    show_user()
except PermissionError as error:
    print("ERROR:", error)