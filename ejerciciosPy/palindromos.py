palabra = input("Ingresa la palabra: ")
Palabralimpio = palabra.lower().replace(" ", "")
invertirPalabra = Palabralimpio[::-1]

if Palabralimpio == invertirPalabra:
    print(f"La frase {palabra} es palindromo")
else: print(f"la frase {palabra} no es un palindromo")