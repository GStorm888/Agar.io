import pygame
import random
import sys
import settings
from object import Object, Player, Food
from field import Field

class Game:
    pygame.init()
    pygame.display.set_caption("Agar.io")

    def __init__(self):
        self.main_window = settings.MAIN_WINDOW
        self.pos_player = Player.move(self)
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(8)
        self.field = Field(self.player)
        self.food = Food()
        self.field.put_at(self.player, self.pos_player)

    def process_input(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            Object.center = mouse_pos
            self.main_window.fill((255, 255, 255))
            pygame.display.flip()
            if random.randint(1, 30) >= 20 :
                self.pos_food = Food.get_pos
                self.field.put_at(self.food, self.pos_food)
                print("process")


    def update_game_state(self):        
        self.player@Player.render()
        print("update")

    def render(self):
        main_window_color = pygame.color.THECOLORS["white"]
        self.main_window.fill(main_window_color)
        self.field.render()
        self.main_window.blit(self.field.render(), (0, 0))
        Player.draw(self@Player.x, self@Player.y)
        pygame.display.update()
        print("render")

    def main_loop(self):  
        while self.running:
            self.process_input()
            self.update_game_state()
            self.render()
            self.clock.tick(settings.FPS)
            print("main")
        pygame.quit()
        sys.exit()

game = Game()
game.render()
game.main_loop()