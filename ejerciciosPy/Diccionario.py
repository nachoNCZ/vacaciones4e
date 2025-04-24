texto = input("Ingresa la palabra o frase: ")
diccionario = {}
cont = 0
for i in texto:
    veces = diccionario.get(i, 0)
    diccionario[i] = veces +1
print(diccionario)