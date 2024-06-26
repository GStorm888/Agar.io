import pygame
import settings
import random
import settings

class Object:
    def __init__(self, x, y, radius):
            self.x = x
            self.y = y
            self.radius = radius
            self.center = (self.x, self.y)

    def draw(self, centr):
        self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        self.color = random.choice(settings.COLOR)
        object_circle = pygame.draw.circle(centr, self.color, (self.x, self.y), self.radius)

    def render():
         ...

class Player(Object):
    def __init__(self, x, y, radius, color):
         super().__init__(x, y, radius, color)

    def draw(self, centr):
        self.radius = 8
        return super().draw(centr)
    

    def move():
         ...


    def eat():
        ...
