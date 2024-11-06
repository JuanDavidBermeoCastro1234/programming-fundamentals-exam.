voltaje=float(input("por favor ingrese el voltaje: "))
voltaje2=float(input("por favor ingrese el voltaje: "))
voltaje3=float(input("por favor ingrese el voltaje: "))
voltaje4=float(input("por favor ingrese el voltaje: "))
voltaje5=float(input("por favor ingrese el voltaje: "))

promedio= voltaje+voltaje2+voltaje3+voltaje4 /5

if promedio<220:
    print(f"voltaje {promedio:.2f} correcto ")
else :
    print("alto voltaje ") 