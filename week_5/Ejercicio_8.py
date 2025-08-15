"""
3. Cree un programa que use una lista para eliminar keys de un diccionario.
"""

user_info = { 
"name": "Emanuel",
"Last name": "Hasbun",
"number" : "5012-4740",
"email": "EmanuelH@lyfter.DEV",
"position": "Student",
"status" : "available",
}

kill_list = ["number","email"]
data_deleted_list = []

for key in kill_list:
    if key in user_info:
        deleted_value = user_info.pop(key)  
        data_deleted_list.append((key, deleted_value))


print (user_info)
print("")
print(data_deleted_list)