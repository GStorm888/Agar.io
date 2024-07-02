def get_distance(list_eat: list, list_pos: list):
    if list_eat[0] - list_pos[0] < 0: can_eat = True 
    elif list_eat[0] - list_pos[0] > 0: can_eat = False
    if list_eat[1] - list_pos[1] < 0: can_eat = True
    elif list_eat[1] - list_pos[1] > 0: can_eat = False
    else: can_eat = False
    return can_eat

class IsAlive:

    def __init__(self):
        self._is_alive = True

    def is_alive(self) -> bool:
        return self._is_alive
    
    def die(self) -> bool:
        self._is_alive = False