import pygame
import settings
import random

class Object:
    def __init__(self, x, y, mass, color):
            self.x = x
            self.y = y
            self.mass = mass
            self.color = color

    def draw(self, win):
        object_circle = pygame.draw.circle(win, self.color, (self.x, self.y), self.mass)


