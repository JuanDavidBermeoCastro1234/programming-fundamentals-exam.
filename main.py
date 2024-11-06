import math 
lado_del_triangulo=float(input("ingrese el lado del triangulo por favor: "))

area= math.sqrt(3/4*lado_del_triangulo**2)

if area<1000:
    print(f"el area es {area} ")
else :
    print("DATOS NO VALIDOS")