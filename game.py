import pygame
import random
import sys
import settings
from object import Object, Player
from field import Field

class Game:
    pygame.init()
    pygame.display.set_caption("Agar.io")

    def __init__(self):
        self.main_window = settings.MAIN_WINDOW
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0, 8)
        self.field = Field(self.player)

    def process_input(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            Object.center = mouse_pos
            self.main_window.fill((255, 255, 255))
            pygame.display.flip()

    def update_game_state(self):        
        self.player@Player.render()

    def render(self):
        main_window_color = pygame.color.THECOLORS["white"]
        self.main_window.fill(main_window_color)
        self.main_window.blit(self.field.render(), (0, 0))
        Player.draw(self@Player.x, self@Player.y)

        pygame.display.update()



    def main_loop(self):  
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(settings.FPS)


        pygame.quit()
        sys.exit()

game = Game()
game.main_loop()