from collections import Counter 

frase = input("Ingrese una frase: ").lower()
palabra = input("Ingrese una palabra: ").lower()

print("Resultado: ", frase.split().count(palabra))

