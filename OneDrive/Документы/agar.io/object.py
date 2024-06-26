import pygame
import settings
import random
import settings

class Object:
    def __init__(self, x, y, mass):
            self.x = x
            self.y = y
            self.mass = mass
    def draw(self, centr):
        self.mass = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        self.color = random.choice(settings.COLOR)
        object_circle = pygame.draw.circle(centr, self.color, (self.x, self.y), self.mass)

class Player(Object):
    def __init__(self, x, y, mass, color):
         super().__init__(x, y, mass, color)

    def draw(self, centr):
        self.mass = 8
        return super().draw(centr)
    

    def move():
         ...


    def eat():
        ...
