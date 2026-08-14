class Category():
    def __init__(self,name):
        clean_name = name.strip().lower()
        if clean_name.isalpha():
            self.name = clean_name
        else:
            raise ValueError("Category name cannot be empty, have numbers or simbols.")

class Movement():

    def __init__(self, name, value, type, category):
        self.name = name.strip().lower()
        
        try:
            self.value = float(value)
        except ValueError:
            raise ValueError("Value must be a valid number.")

        if self.value < 0:
            raise ValueError("Value must be a positive number.")
        
        self.type = type
        self.category = category

class FinanceManager():
    def __init__(self):
        self.categories = {}
        self.movements = []
        self.valid_types = ["income","expense"]
        self.data_loaded = False

    def add_category(self,name):
        category = Category(name)
        if category.name in self.categories:
            raise ValueError("Category already exist")
        self.categories[category.name] = category
        return category

    def add_movement(self,name,value,type,category):
        if category not in self.categories.values():
            raise ValueError("Category does not exist")
        if type not in self.valid_types:
            raise ValueError("Please selelct a type")
        else:
            movement = Movement(name,value,type,category)
            self.movements.append(movement)
        return movement

    def get_total_by_type(self,movement_type):
        if movement_type not in self.valid_types:
            raise ValueError("type does not exist")
        total_type = 0
        for movement in self.movements:
            if movement.type == movement_type:
                total_type += movement.value
        return total_type
    
    def get_balance(self):
        total_income = self.get_total_by_type("income")
        total_expense = self.get_total_by_type("expense")
        return total_income - total_expense