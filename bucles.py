numero=int(input("Ingresa un numero entero positivo: "))

if type(numero)==int and numero>1:
    for i in range(numero, -1, -1):
        print(i, end=",")
        
else:
    print("No es un entero positivo")



class Persona:
    trabaja="24hs"
    edad="Entre 18 y 36 años"
    def __init__(self, nombre, experiencia):
        self.nombre=nombre
        self.experiencia=experiencia

    def LaDelCovid(self):
        print("Tiro la del covid.")
    
trabajador=Persona("Ale", "1 año")

print(f"Su nombre es: {trabajador.nombre} y trabaja: {trabajador.trabaja}, y tiene {trabajador.edad}")
trabajador.LaDelCovid()

trabajador2=Persona("Angelito", "patriki")
print(f"Su nombre es: {trabajador2.nombre}, experiencia{trabajador2.experiencia}, y tiene {trabajador2.edad} y  NO ")
trabajador2.LaDelCovid()



class Jeans:
    temporada="Invierno 22"
    def __init__(self, nombre, precio):
        self._nombre=nombre
        self._precio=precio
        print(f"Jean: {nombre}, y esta: {precio}")
    def __str__(self):
        return(f"Si entra en la promo: {self._nombre}")    
  


tyfox=Jeans("Tyfox", "20.500")
terra=Jeans("Terra", "16.500")















































