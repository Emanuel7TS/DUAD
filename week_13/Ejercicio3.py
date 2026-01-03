from datetime import date

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age


def require_adult_user(func):
    def wrapper(*args, **kwargs):
        user = args[0]

        if not isinstance(user, User):
            raise TypeError("First argument must be a User")

        if user.age < 18:
            raise PermissionError("User must be at least 18 years old")

        return func(*args, **kwargs)

    return wrapper


@require_adult_user
def access_system(user):
    return "Access granted"

adult = User(date(2000, 5, 10))   # mayor de 18
minor = User(date(2010, 5, 10))   # menor de 18

print(access_system(adult))
print(access_system(minor))