edad=int(input("Ingresa tu edad: "))

if (edad<18):
    print("No podes pasar, sos menor de edad.")
elif(edad>=90):
    print("Edad incorrecta.")
else:
    print("Podes pasar, sos mayor de edad.")


#----------------------------------------------------------------#

contrasenia="ALOJA123"

intento=input("Ingresa la contraseña: ")

intento=intento.upper()

if (intento==contrasenia):
    print("Contraseña correcta")
else:
    print("No papu, ajuera")

#-------------------------------------------------------------------------#

num1=int(input("INGRESA EL PRIMER NUMERILLO: "))
num2=int(input("INGRESA EL SEGUNDO NUMERILLO: "))

if (num2!=0):
    print(f"El resultado de {num1} dividido {num2} es: {num1/num2}")
else:
    print("No se puede dividir por 0 ")

#----------------------------------------------------------------------------#

numero=int(input("Ingresa un numero entero: "))

if (numero%2==0):
    print("Es par")
else: 
    print("Es impar")

#-----------------------------------------------------------------------------#

edades=int(input("Ingresa tu edad: "))
ingreso=int(input("Ingresa tus ingresos mensuales: "))

if(edades>=16 and ingreso>=1000):
    print("Tenes que tributar")
elif(edades>=16 and ingreso<1000):
    print("No cumplis con el ingreso minimo para tributar.")
elif(edades<16 and ingreso>=1000):
    print("No cumplis con la edad necesaria para tributar.")
else:
    print("No cumplis ni con la edad, ni con el ingreso.")

#-------------------------------------------------------------------------------#


sexo=input("Ingresa tu genero M o F: ")
nombre=input("Ingresa tu nombre: ")

if ((sexo=="F" and nombre[0]<="M") or (sexo=="M" and nombre[0]>="N")):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")


#----------------------------------------------------------------------------------#
