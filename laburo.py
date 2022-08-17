print("Hola mundo")

def suma(num1,num2):
	resultado= num1+num2
	print(resultado)

print(suma(2,6))

lista1=["daniel", 5, "aguirre", 24]

print(lista1[0:4])

"""
operadores

>	mayor que
<	menor que
>=	mayor o igual que
<=	menor o igual que
==	igual
!=	diferente que

operadores logicos:
and, or, y not
and: va a devolver true siempre y cuando, todas las condiciones se cumplan
or: va a devolver  true si alguna de las condiciones se cumplen
not: negamos un valor booleano, simplemente negamos un valor booleano, es decir lo cambia
si un valor es true, con not lo cambiamos a false





"""
#not

numero1=10
numero2=20

resultado=numero1 < numero2 and True
print(resultado)


edad = input("Ingresa tu edad: ")
edad = int(edad)

if edad >= 18:
	print("Sos mayor de edad")


