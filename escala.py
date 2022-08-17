#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima
#por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


nombre=input("Ingresa tu nombre: ")
numero=int(input("Ingrese un numero entero: "))

print((nombre + "\n")* numero)





#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por 
#pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
#otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los 
#apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

completo=input("Ingrese su nombre completo: ")

print(completo.upper())
print(completo.lower())
print(completo.title())

#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
#introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
#mayúsculas y <n> es el número de letras que tienen el nombre.

nombre2=input("Ingresa tu nombre: ")

print(f"{nombre2.title()}, Tiene: {len(nombre2)} letras")


#Ejercicio4
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es
#el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
#el número de teléfono sin el prefijo y la extensión.

numero=input("Ingresa tu numero de telefono en el siguiente formato +xx-xxxxxxxxx-xx: ")

print(f"Tu numero es: {numero[4:13]}")

#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola
#y muestre por pantalla la frase invertida.

frase=input("Ingresa una frase: ")

print(frase[::-1])




