import pygame
from circleshape import CircleShape
import constants
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width = 2)    

    def update(self, dt):
        super().update(dt)
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        random_dir_1 = self.velocity.rotate(angle)
        random_dir_2 = self.velocity.rotate(-angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        first = Asteroid(self.position.x,self.position.y, new_radius)
        second = Asteroid(self.position.x,self.position.y, new_radius)

        first.velocity = random_dir_1 * 1.2
        second.velocity = random_dir_2 * 1.2


