"""
# Ejercicio 2
Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre
 si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
"""

user_name =str(input("Type your name: "))
user_last_name =str(input("Type your last name: "))
user_age =int(input("Type your age: "))
user_category_list = ["Baby","Child","Pre-adolescent","Adolescent","Young","Adult","Older"]

if (user_age >0 and user_age <= 2):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[0], "category.")
    
elif (user_age >=3 and user_age <= 9):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[1], "category.")
    
elif (user_age >=10 and user_age <= 12):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[2], "category.") 
    
elif (user_age >=13 and user_age <= 17):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[3], "category.") 

elif (user_age >=18 and user_age <= 25):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[4], "category.") 

elif (user_age >=26 and user_age <= 64):
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[5], "category.") 
    
else:
    print("Hello", user_name, user_last_name + ", you are", user_age, 
      "years old, so you belong to the", user_category_list[6], "category.") 