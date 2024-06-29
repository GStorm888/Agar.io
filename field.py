import pygame
import settings
from object import Object, Player, Food
from different_function import IsAlive
import pygame
import numpy as np
import settings 
from game import Game
class Field:
    def __init__(self):
        self.units = []
        self._init_field()

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

    def _init_field():
        ...

    def clear_dead_units(self):
        self.units = [unit for unit in self.units if unit.is_alive()]

    def render_units(self, field):
        for unit in self.units:
            unit_pos = unit@Object.get_position()
            field.blit(unit.render(), unit_pos)
    
    def render(self):
        cells = np.zeros(settings.WINDOW_CELLS_FILL)
        self@Game.main_window.fill(settings.BLACK)
        Field.draw_grid(self@Game.main_window, cells)
        field = pygame.Surface((settings.WINDOW_WIDTH,
                                 settings.WINDOW_HEIGHT))
        self.render_units(field)
