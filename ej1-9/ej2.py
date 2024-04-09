from collections import Counter 

text = """Python es un lenguaje de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código.​
Se trata de un lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. 
Es un lenguaje interpretado, dinámico y multiplataforma.

Su sintaxis en particular es bastante clara y legible, lo que lo hace ideal para proyectos con una base de código extensa y para colaboración en equipos de desarrollo. 
Además, su gran cantidad de bibliotecas y su amplia comunidad de desarrolladores hacen de Python una excelente opción para una variedad de aplicaciones, desde desarrollo web hasta análisis de datos y aprendizaje automático."""

words = [word for word in text.split() if len(word) > 4]
print(Counter(words).most_common(1)[0][0])