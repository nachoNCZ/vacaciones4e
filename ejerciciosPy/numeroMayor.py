n1 = int(input("Ingresa el primer numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} es mayor que {n2} y {n3}")

elif n2 > n1 and n2 > n3:
    print(f"{n2} es mayor que {n1} y {n3}")

else: print(f"{n3} es mayor que {n1} y {n2}")