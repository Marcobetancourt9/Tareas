import math
print("Vamos a hacer resolvente para hallar los dos valores de x")
a=int(input("introduce el valor de a "))
b=int(input("introduce el valor de b "))
c=int(input("introduce el valor de c "))
discriminante= (b**2)-(4*a*c)
discriminante2= float(discriminante)
raiz= math.sqrt(discriminante2)
denominador= 2*a
x1=-b+raiz
x2=-b-raiz
if discriminante2>=0:
    print("x1=", x1/denominador)
    print("x2=", x2/denominador)
else:
    print("La ecuacion no tiene solucion")