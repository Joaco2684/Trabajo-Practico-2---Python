def generate_structure(names,goals,goals_avoided,assists):
    return tuple(zip(names.replace(" ", "").replace("\n","").split(","),goals,goals_avoided,assists))

def get_name_goals_scorer(stats):
    player_scorer = max(stats, key=lambda x: x[1])
    return player_scorer[0],player_scorer[1]
    
def get_points(player):
    values = {'goals': 1.5, 'avoided': 1.25, 'assist': 1}
    return player[0], player[1] * values['goals'] + player[2] * values['avoided'] + player[3] * values['assist']
    
def get_name_influential(stats):
    points = map(get_points,stats)
    player_max_points = max(points, key=lambda x:x[1])
    return player_max_points[0]

def get_prom_goals(goals):
    return sum(goals) / 25

