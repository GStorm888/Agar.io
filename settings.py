import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
MAIN_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MAX_MASS = 30
MIN_MASS = 1
FPS = 60
CELL_SIZE = 100
WINDOW_CELLS_FILL = (WINDOW_HEIGHT // 10, WINDOW_WIDTH // 10)

COLOR = [pygame.color.THECOLORS["black"],
         pygame.color.THECOLORS["red"], 
         pygame.color.THECOLORS["blue"],
         pygame.color.THECOLORS["cyan"],
         pygame.color.THECOLORS["gold"],
         pygame.color.THECOLORS["green"],
         pygame.color.THECOLORS["orange"],
         pygame.color.THECOLORS["purple"],
         pygame.color.THECOLORS["yellow"]]

