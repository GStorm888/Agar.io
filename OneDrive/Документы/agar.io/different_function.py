def get_distans(object_pos: list, player_pos: list):
    if object_pos[0] - player_pos[0] < 0: can_eat = True 
    elif object_pos[0] - player_pos[0] > 0: can_eat = False
    if object_pos[1] - player_pos[1] < 0: can_eat = True
    elif object_pos[1] - player_pos[1] > 0: can_eat = False
    else: can_eat = False
    return can_eat