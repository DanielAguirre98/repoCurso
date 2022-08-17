#ejercicio1

area={}

def area_rectangulo(base,altura):
    area=base*altura
    return area


print(area_rectangulo(15, 10))

#-----------------------------------------#
#ejercicio 2
def area_circulo(radiox):
    radiox=((radiox**2)*3.14159)
    return radiox

print(area_circulo(5))

#-----------------------------------------#
#ejercicio3

def relacion(num1,num2):
    if num1>num2:
        resultado=1
        return resultado
    elif num1<num2:
        resultado=-1
        return resultado
    else:
        resultado=0
        return resultado

print(relacion(10,5))
print(relacion(5, 10))
print(relacion(5, 5))

#------------------------------------------#
#ejercicio 4

def intermedio(number1,number2):
    resulta3=((number1+number2)/2)
    return resulta3

print(intermedio(-12, 24))

#----------------------------------------#
#ejercicio6

#Por ejemplo:

#pares, impares = separar([6,5,2,1,7])
#print(pares)   # valdría [2, 6]
#print(impares)  # valdría [1, 5, 7]

lista=[6,5,2,1,7]
lista.sort()
print(lista)

#---------------#
pares=[]
impares=[]

def separar(args):
    for i in lista:
        if (i%2==0):
            pares.append(i)
        else:
            impares.append(i)
    
    return pares, impares

print(separar(lista))