import pygame
import random
import sys
import settings
from object import Object, Player

class Game:
    pygame.init()
    pygame.display.set_caption("Agar.io")

    def __init__(self):
        self.main_window = pygame.display.set_mode((settings.WINDOW_WIDTH
                                                    , settings.WINDOW_HEIGHT))
    def process_input(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            mouse_pos = pygame.mouse.get_pos()
            Object.center = mouse_pos
            Game.main_window.fill((255, 255, 255))
            pygame.draw.rect(self.main_window, settings.RED,
                        Object.object_circle)
            pygame.display.flip()

    def update_game_state(self):
        ...

    def render(self):
        main_window_color = pygame.color.THECOLORS["white"]
        self.main_window.fill(main_window_color)

        Player.draw(self@Player.x, self@Player.y)

        pygame.display.update()



    def main_loop(self):  
                 # x, y, mass, color
        food = Object(random.randint(0, settings.WINDOW_WIDTH), random.randint(0, settings.WINDOW_HEIGHT),
                       random.randint(settings.MIN_MASS, settings.MAX_MASS), settings.WHITE)

        while self.run:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(settings.FPS)


        pygame.quit()

        sys.exit()

game = Game()
game.main_loop