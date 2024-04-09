texto = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. 
Es un lenguaje interpretado, dinámico y multiplataforma.

Su sintaxis en particular es bastante clara y legible, lo que lo hace ideal para proyectos con una base de código extensa y para colaboración en equipos de desarrollo. 
Además, su gran cantidad de bibliotecas y su amplia comunidad de desarrolladores hacen de Python una excelente opción para una variedad de aplicaciones, desde desarrollo web hasta análisis de datos y aprendizaje automático."""
vocales = ("a","e","i","o","u")

lineas = texto.split("\n")
for linea in lineas:
    palabras = linea.split()
    if len(palabras) > 0:
        if palabras[1][0].lower() in vocales:
            print(linea)
