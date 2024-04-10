palabra = input("Ingrese una palabra: ").lower().strip()
lista = []
for letra in palabra:
    if letra in lista:
        res = "no"
        break
    else:
        if letra.isalpha():
            lista.append(letra)
else:
    res = "Si"

print("Heterogama: ",res)