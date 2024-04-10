article = """título: Experiences in Developing a Distributed Agent-
based Modeling Toolkit with Python Version 3
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented
details of large-scale complex systems. However, the specialized
knowledge required for developing such ABMs creates barriers to wider
adoption and utilization. Here we present our experiences in
developing an initial implementation of Repast4Py, a Python-based
distributed ABM toolkit. We build on our experiences in developing ABM
toolkits, including Repast for High Performance Computing (Repast
HPC), to identify the key elements of a useful distributed ABM
toolkit. We leverage the Numba, NumPy, and PyTorch packages and the
Python C-API to create a scalable modeling system that can exploit the
largest HPC resources and emerging computing architectures. """

index_resume = article.find("resumen:")
title = article[len("titulo:"):index_resume-2].strip()
resume = article[index_resume + len("resumen:"):].strip()

if (len(title.split())) <= 10:
    print("OK")
else:
    print("not OK")
    
cant_facil=0
cant_aceptable=0
cant_dificil = 0
cant_muydificil=0

for oracion in resume.split("."):
    words = len(oracion.split())
    if words < 12:
        cant_facil += 1
    elif 13<=words<=17:
        cant_aceptable+=1
    elif 18<=words<=25:
        cant_dificil+=1
    else:
        cant_muydificil+=1

print("Cantidad de oraciones: ", cant_facil,cant_aceptable,cant_dificil, cant_muydificil)





