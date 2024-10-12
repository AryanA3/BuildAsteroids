import pygame
from circleshape import CircleShape
import constants

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,constants.SHOT_RADIUS)

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width = 2)    

    def update(self, dt):
        super().update(dt)
        self.position += (self.velocity * dt)