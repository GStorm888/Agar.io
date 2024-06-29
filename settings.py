import pygame
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
MAIN_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAX_MASS = 30
MIN_MASS = 1
FPS = 60
CELL_SIZE = 100
WINDOW_CELLS_FILL = (WINDOW_HEIGHT // 10, WINDOW_WIDTH // 10)
COLOR = [BLACK,                  # black
         RED,                    # red
         (0, 0, 255, 255),       # blue
         (0, 255, 255, 255),     # cyan
         (255, 215, 0, 255),     # gold
         (0, 255, 0, 255),       # green
         (255, 165, 0, 255),     # orange
         (160, 32, 240, 255),    # purple
         (255, 255, 0, 255)]     # yellow