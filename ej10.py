import modulos

names = """Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, 
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
0]

stats = modulos.generate_structure(names,goals,goals_avoided,assists)

name_scorer, goals_scorer = modulos.get_name_goals_scorer(stats)
print("Nombre del goleador: ",name_scorer)
print("Cantidad de goles del goleador: ",goals_scorer)

name_influential = modulos.get_name_influential(stats)
print("Nombre jugador más influyente: ",name_influential)

prom_goals_team = modulos.get_prom_goals(goals)
print("Promedio de goles por partido del equipo: ",prom_goals_team)

prom_goals_scorer = goals_scorer / 25
print("Promedio de goles de ", name_scorer, " (goleador/a): ",prom_goals_scorer)