import pygame
import settings
import random
import settings
import different_function
from different_function import IsAlive

class Object:
    def __init__(self, x, y, radius):
            self.x = x
            self.y = y
            self.radius = radius
            self.center = (self.x, self.y)
            self.list_eat = []
            list_pos = Player.get_pos()

    def draw(self, centr):
        self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        self.color = random.choice(settings.COLOR)
        self.object_circle = pygame.draw.circle(centr, self.color, (self.x, self.y), self.radius)
        return self.list_eat.append(self.object_circle)

    def render(x, y, radius, color):
        object = Object(x, y, radius, color)
        return object
    
    def get_pos(self):
         return list(self.x, self.y)


class Player(Object):
    def __init__(self, x, y, radius, color):
         super().__init__(x, y, radius, color)

    def draw(self, centr):
        self.radius = 8
        return super().draw(centr)
    
    def get_pos(self):
        super().get_pos()

    def move():
         ...
    


    def eat(self, list_eat, list_pos):
        for food in list_eat:
            if different_function.get_distans(food.Food.get_pos(), list_pos):
                 food.IsAlive.die
                 list_eat.remove(food.Food.get_pos())

    def render(self, x, y, radius, color):
        self.x = settings.WINDOW_WIDTH // 2
        self.y = settings.WINDOW_HEIGHT // 2
        self.radius = 20
        self.color = settings.RED
        return super().render(y, radius, color)

class Food(object):
    def __init__(self):
          ...

    def draw(self, centr):
        self.x = random.randint(settings.WINDOW_WIDTH)
        self.y = random.randint(settings.WINDOW_HEIGHT)
        self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        return super().draw(centr)
    
    def get_pos(self):
        return super().get_pos()
