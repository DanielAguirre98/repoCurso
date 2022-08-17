#Escribe un programa que le pregunte al usuario numeros hasta que ingrese el 0, cuando lo haga muestre por 
#pantalla la suma de todos los numeros ingresados:

numero=int(input("Ingresa un numero a sumar o ingresa 0 para salir del programa: "))
#aca declaro una variable numero para guardar el mismo.

suma=0
#aca declado una variable que empieze en 0

while (numero!=0):   #mientras que numero sea distinto de 0:
    suma=suma+numero  #suma que empezo en 0 le sumo lo que el usuario ingreo en numero
    print("El conteo es de: ", suma)  # imprimo un mensansaje por pantalla para llevar el conteo
    numero=int(input("Ingrese un numero a sumar o ingrese 0 para salir del programa: ")) #vuelvo a preguntarle al usuario si quiere sumar otro numero o quiere salir
else: #si oprime 0 sale del bucle
    print("Usted salio del programa con la suma de: ", suma) #imprimo un mensaje por pantalla para que muestre la suma de todos los numeros que ingreso


c=-3
while True:
    c=c+1
    if c==2:
        print("Ahora que c vale 2 salimos")
        break
    print("c vale ", c)


n=0
while n<10:
    n=n+1
    if n == 2:
        pass
    print("n vale: ", n)


lista=[1,2,3]

consulta=int(input("Ingresa un valor para saber si esta en la lista: "))

for consulta in lista:
    print("soy el elemento: ", lista)
else:
    print("No estoy")