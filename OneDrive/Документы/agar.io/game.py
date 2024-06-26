import pygame
import random
import sys
import settings
from object import Object

class Game:
    pygame.init()
    pygame.display.set_caption("Agar.io")


    def __init__(self):
        self.main_window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))

    def process_input():
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            mouse_pos = pygame.mouse.get_pos()
            Object.object_circle.center = mouse_pos
            Game.window.fill((255, 255, 255))
            pygame.draw.rect(Game.window, settings.RED, Object.object_circle)
            pygame.display.flip()


    def render(self):
        self.main_window.blit(self.field.render(), (0, 0))
        pygame.display.update()



    def main_loop():
        player = Object(settings.WINDOW_WIDTH // 2, settings.WINDOW_HEIGHT // 2, 20, settings.RED)
                                # x, y, mass, color
        food = Object(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT),
                       random.randint(settings.MIN_MASS, settings.MAX_MASS), settings.WHITE)

            # Game.win.fill(settings.BLACK)
            # player.draw(Game.win)
            # food.draw(Game.win)
            # pygame.display.update()

        pygame.quit()
        sys.exit()
