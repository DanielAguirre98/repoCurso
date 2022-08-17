def bisiesto(num1):
    if (num1 % 4 == 0 and(num1 % 100!=0 or num1 %400==0)):
        print("Es bisiesto")
    else:
        print("No es bisiesto") 

bisiesto(2012)
bisiesto(2010)
bisiesto(2000)
bisiesto(1900)
