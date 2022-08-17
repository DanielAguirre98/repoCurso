""""nombre=input("Ingresa tu nombre: ")

tascani=["Dani","Ale","Angel","Bichi"]

if nombre==tascani[0]:
    print("Bienvenido Daniel")
elif nombre==tascani[1]:
    print("Bienvenido Alejandro")
elif nombre==tascani[2]:
    print("Bienvenido Angel")
elif nombre==tascani[3]:
    print("Bienvenido Bichii!")
else:
    print("No estas en el sistemas")
"""

hace=["Dani","Angelismo del mal","Ale"]

turno=int(input("Ingresa un numero del 1 al 3: "))

if turno==1:
    print("Sortea los rubros para: ", hace[0])
elif turno==2:
    print("Sortea los rubros para: ", hace[1])
elif turno==3:
    print("Se sortea los rubros para ", hace[2])
else:
    print("Dije del 1 al 3!")


rubros=["Camisas","Jeans","Remeras","Buzos","Calzado","Accesorios","Sweaters","Campera de tela","Pantalones","Joggers","young",]
numero=int(input("Ingresa un numero del 1 al 10"))
te_toca=rubros

if numero <= 3 and numero >=0:
   te_toca=rubros[0:4]
   print("Te toca: ", te_toca)
elif numero >=4 and numero <=7:
    te_toca=rubros[4:8]
    print("Te toca: ", te_toca)
elif numero >=7 and numero <=10:
    te_toca=rubros[8:11]
    print("Te toca: ", te_toca)
else:
    print("Dije un numero del 1 al 10!")    