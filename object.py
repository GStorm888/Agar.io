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
            self.field = None
            self.position = None

    def draw(self, centr):
        self.radius = random.randint(settings.MIN_MASS, settings.MAX_MASS)
        self.color = random.choice(settings.COLOR)
        self.object_circle = pygame.draw.circle(centr, self.color, (self.x, self.y), self.radius)
        return self.list_eat.append(self.object_circle)

    def render(x, y, radius, color):
        object = Object(x, y, radius, color)
        return object
    
    def set_field(self, field):
         self.field = field
        
    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

class Player(Object):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = settings.COLOR[2]
        self.position = (self.x, self.y)

    def draw(self, centr):
        self.radius = 8
        return super().draw(centr)
    
    def get_pos(self):
        super().get_position()

    def move():
         ...

    def eat(self, list_eat, list_pos):
        for food in list_eat:
            if different_function.get_distans(food@Food.get_pos(), list_pos):
                 food@IsAlive.die
                 list_eat.remove(food@Food.get_pos())
                 self.radius += food@Food.radius()

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
        return super()@Object.draw(centr)
    
    def get_pos(self):
        return super()@Object.get_position()
    
    def get_radius(self):
        return self.radius