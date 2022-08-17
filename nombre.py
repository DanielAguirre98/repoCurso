nombre=input("Ingresa tu nombre: ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")


telefono=input("Ingresa un numero de telefono con fotmato +xx-xxxxxxxxx-xx: ")

print("El numero de telefono es: " + telefono[4:-3])

frase=input("Ingresa una frase: ")

print("La frase invertida es: " + frase[::-1])