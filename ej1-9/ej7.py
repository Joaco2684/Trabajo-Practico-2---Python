text = """ La brecha salarial alcanzó el 27,7%: las mujeres ocupadas
debieron trabajar 8 días y 10 horas más que los varones ocupados para
ganar lo mismo que ellos en un mes. """

cant_may = sum(1 for letra in text if letra.isupper())
cant_min = sum(1 for letra in text if letra.islower())
cant_no = sum(1 for letra in text if not letra.isalpha() and not letra.isspace())
cant_letras = sum(1 for letra in text if letra.isalpha())

print(cant_may)
print(cant_min)
print(cant_no)
print(cant_letras)
