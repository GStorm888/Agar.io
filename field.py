import pygame
import settings
from object import Object, Player, Food
from different_function import IsAlive
import pygame
import numpy as np
import settings 
class Field:
    def __init__(self, player):
        self.units = []
        self.player =  player

    def put_at(self, new_unit, pos):
            
        new_unit@Object.set_field(self)
        new_unit@Object.set_position(pos)
        self.units.append(new_unit)
        return True
    
    def draw_grid(window, cells):
        for row, col in np.ndindex(cells.shape):
            color = settings.WHITE
            pygame.draw.rect(window, color, (col * settings.CELL_SIZE, row * settings.CELL_SIZE,
                                              settings.CELL_SIZE  - 1, settings.CELL_SIZE - 1))

    def clear_dead_units(self):
        self.units = [unit for unit in self.units if unit@IsAlive.is_alive()]

    def render_eat(self, field):
        for unit in self.units:
            unit_pos = unit@Food.get_pos()
            field.blit(unit.render(), unit_pos)
    
    def render_player(self, field):
        player_pos = Player.get_pos()
        field.blit(self.player.render(), player_pos)\
    
    def render(self):
        cells = np.zeros(settings.WINDOW_CELLS_FILL)
        self@settings.MAIN_WINDOW.fill(settings.BLACK)
        Field.draw_grid(self@settings.MAIN_WINDOW, cells)
        field = pygame.Surface((settings.WINDOW_WIDTH,
                                 settings.WINDOW_HEIGHT))
        self.render_eat(field)
