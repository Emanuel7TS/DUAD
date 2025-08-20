class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self,product):
        self.products.append(product)
        print("Product added succesfully")

    def show_products(self):
        for product in self.products:
            print(product)

    def get_total_from_inventory(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity

        return total
    

gamer_inv = Inventory()

product1 = Product("XBOX Controller", 50, 2)
product2 = Product("Pc", 5000, 1)
product3 = Product("Mouse", 25, 1)

gamer_inv.add_product(product1)
gamer_inv.add_product(product2)
gamer_inv.add_product(product3)

print(len(gamer_inv.products))
Inventory.show_products(gamer_inv)

print(gamer_inv.get_total_from_inventory())