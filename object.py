import pygame
import settings
import random
import different_function
from different_function import IsAlive

class Object:
    def __init__(self, x, y, radius):
            self.x = x
            self.y = y
            self.radius = radius
            self.center = (self.x, self.y)
            self.list_eat = []
            self.field = None
            self.position = None
            

    def draw(self, centr):
        self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        self.color = random.choice(settings.COLOR)
        self.object_circle = pygame.draw.circle(centr, self.color, (self.x, self.y), self.radius)
        return self.list_eat.append(self.object_circle)

    @staticmethod
    def render(x, y, radius, color):
        object = Object(x, y, radius, color)
        return object
    
    def set_field(self, field):
         self.field = field
        
    def set_position(self, new_position):
        self.position = new_position

    def get_position(self, pos):
        return self.position

class Player(Object):
    def __init__(self, radius):
        self.radius = radius
        self.color = settings.COLOR[2]
        self.position = None

    # def get_pos(self):
    #     return self.move
    
    def move(self):
        self.position = pygame.mouse.get_pos()
    
    def draw(self, centr):
        self.player_circle = pygame.draw.circle(centr, settings.COLOR[2], self.position, self.radius)
        return self.player_circle

    def eat(self, list_eat, list_pos):
        for food in list_eat:
            if different_function.get_distans(food@Food.get_pos(), list_pos):
                 food@IsAlive.die
                 list_eat.remove(food@Food.get_pos())
                 self.radius += food@Food.radius()

    def render(self):
        self.x = settings.WINDOW_WIDTH // 2
        self.y = settings.WINDOW_HEIGHT // 2
        self.radius = 8
        self.player = pygame.Surface((self.x, self.y), pygame.SRCALPHA) 
        return self.player

class Food(object):
    def __init__(self):
            self.food_list = []

    def draw(self, centr):
        while run is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                food_x = random.randint(0, settings.WINDOW_WIDTH)
                food_y = random.randint(0, settings.WINDOW_HEIGHT)
                self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
                self.food_list.append([food_x, food_y, self.radius])
        return super()@Object.draw(centr)
    
    def get_pos(self):
        return super()@Object.get_position()
    
    def get_radius(self):
        return self.radius
