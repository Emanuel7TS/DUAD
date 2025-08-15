"""2 Dado el nombre y apellido de un empleado, y el dominio .com
de una empresa, genere su
email usando el formato
<nombre>.<apellido>@<dominio_de_empresa>.com."""


name = ""
last_name = ""
domain_name = ""

name = str(input("type your name: "))
last_name = str(input("type your last name: "))
domain_name = str(input("type your company's domain: "))

print("Your new email is " + name + last_name + "@" + domain_name + ".com")