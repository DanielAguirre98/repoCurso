#Escribir un programa que almacene la cadena de 
# caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta 
# mayúsculas y minúsculas.

contraseña=input("Ingrese su contraseña: ")

intento=input("Introduzca su contraseña: ")

if (contraseña==intento):
    print("Las contraseñas coinciden")
else:
    print("NO MANSO!")


#Escribir un programa que pida al usuario dos números y muestre por 
# pantalla su división. Si el divisor es cero el programa debe mostrar un error.    

num1=int(input("Ingrese un numero: "))
num2=int(input("Ingrese el segundo numero: "))

resultado=num1/num2

if (resultado!=0):
    print(resultado)
else:
    print("Error")

#otro

mate=int(input("Ingrese un numero par"))

if (mate%2==0):
    print("correcto, es par")
else:
    print("Incorrecto, es impar")
    alan di