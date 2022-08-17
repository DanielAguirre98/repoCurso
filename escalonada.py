camisas=[]

while(True):
    nombre=input("Ingresar camisas: ")
    if(nombre!="Basta"):
        camisas.append(nombre)
        continue
    else:
        print("terminado el rubro camisas")
        print(camisas)
    break    


