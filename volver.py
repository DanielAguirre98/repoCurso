palabra=input("Ingresa una palabra: ")

contador=0

while(contador<10):
    print(palabra)
    contador=contador+1

#-------------------------------------------------------#

edad=int(input("Ingresa tu edad: "))

contador=0

while(contador<=edad):
    print(f"Has cumplido {contador}.")
    contador=contador+1

#-------------------------------------------------------#


dato1=int(input("Ingresa un numero entero positivo: "))

for i in range(1,dato1+1,2):
    print(i, end=",")
    

#----------------------#

numero2=int(input("Ingresa un numeroo:: "))

for j in range(numero2 -1,-1,-1 ):
    print(j, end=",")

#-------------------------#

tabla=int(input("Ingresa que tabla queres: "))

a=0

while(a<11):
    print(f"el resultado de {tabla} * {a} es: {tabla * a}")
    a=a+1



contraseña="aloja"

prueba=input("Ingresa la contra: ")

while(prueba!=contraseña):
    print("La contraseña es incorrecta.")
    prueba=input("Ingresa la contraseña: ")
    
else:
    print("Contraseña correcta")


numeroPrimo=int(input("Ingresa un numero: "))

while(numeroPrimo%1!=0 or numeroPrimo%numeroPrimo!=numeroPrimo):
    print("No es primo.")
    numeroPrimo=int(input("Ingresa un numero primo: "))
else:
    print("Es primo!")