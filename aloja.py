"""usuario="Daniel"
contraseña=1234

intento_usuario=input("Ingrese el usuario: ")
intento_contraseña=int(input("Ingrese su contraseña: "))

if intento_usuario==usuario and intento_contraseña==contraseña:
    print("Sesion iniciada")
else:
    print("Los datos son incorrectos")
"""
remeras=("Bronzon", "Borex", "Borja")
jeans=("Dark", "Tukeno", "Tendra")
calzado=("Farah negro", "Farah blanco", "Fae Plus")
camperas=("Rust negro", "Rust azul", "Racol Rojo", "Raznik")

print("Que desea comprar?: ")
respuesta=int(input("1. remeras, 2. jeans, 3.calzado, 4. caperas"))

if respuesta==1:
    print(remeras)
elif respuesta==2:
    print(jeans)
elif respuesta==3:
    print(calzado)
elif respuesta==4:
    print(camperas)
else:
    print("No tenemos disponible")

if respuesta==1:
    print("Que remera desea comprar?")
elif respuesta==2:
    print("Que jean desea comprar?")
elif respuesta==3:
    print("Que calzado desea comprar?")
elif respuesta==4:
    print("Que campera desea comprar?")
else:
    print("No tenemos disponible")

orden=input("Seleccione la remera: ") 

if orden=="Bronzon":
    print("La remera seleccionada es: "+ orden)
    metodo=input(("Como desea abonar? "))

else:
    print("Articulo no disponible :C")

if metodo=="efectivo":
    print("El valor seria $7500")
elif metodo=="Tarjeta":
    print("En cuantas cuotas desea hacer el pago? ")
    cuotas=int(input("3 o 6 sin interes"))
    if cuotas==3 or cuotas==6:
        print("se realizo el pago en "+ str(cuotas) + " sin interes")
    else:
        print("Cuotas no disponibles")

