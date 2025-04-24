numeros = [78,45,48,62,6,687,79,72,3,524]
#suma = sum(numeros)
#print(suma, suma/len(numeros))

#Con for
suma = 0
cont = 0
for num in numeros:
    suma += num #Se suman los elementos de la lista
    cont += 1 #Inicializamos el contador en 1 para contar los elementos de la lista

#Creamos otra variable y calculamos el promedio
promedio = suma / cont

print(f"La suma es: {suma}")
print(f"El promedio es: {promedio}")


