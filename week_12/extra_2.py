from abc import ABC, abstractmethod

class User(ABC):  
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        self._name = name

    def get_role(self):
        return "admin"

    def has_permission(self, permission):
        return True   


class RegularUser(User):
    def __init__(self, name):
        self._name = name

    def get_role(self):
        return "regular"

    def has_permission(self, permission):
        return permission == "read"   


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")
user3 = RegularUser("Emanuel")

print(user3.has_permission("write"))
print(user1.has_permission("delete"))
print(user2.has_permission("delete"))
print(user2.has_permission("read"))
