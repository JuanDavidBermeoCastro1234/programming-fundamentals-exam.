voltaje=float(input("ingrese un voltaje por favor: "))
voltaje2=float(input("ingrese un voltaje distinto al primero por favor: "))
voltaje3=float(input("ingrese un voltaje distinto a los otros dos por favor: "))

promedio=voltaje+voltaje2+voltaje3/3

if promedio<115:
    print(f"VOLTAJE CORRECTO {promedio:.2f}")
elif promedio>115<220:
    print(f"ALTO VOLTAJE {promedio:.2f}")
elif promedio>220:
    print(f"PELIGRO {promedio:.2f}")
