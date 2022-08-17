numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))

print(f"La division entre los dos numeros da un cociente de: {numero1/numero2} y el resto es de: {numero1%numero2}")


crear_Usuario=input("Crear nombre de usuario: ")
crear_Pass=input("Crear Contraseña: ")

dinero=20000

intentos=3

while (intentos<=3):
    usuario=input("Ingresa el nombre de usuario: ")
    contra=input("Ingresa la contraseña: ")
    if (usuario==crear_Usuario and contra==crear_Pass):
        dineroN=int(input("Cuanto dinero desea sacar? "))
        dinero=dinero-dineroN
        print(f"Le queda {dinero} disponible.")
    else:
        continue

    intentos+=1
