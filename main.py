from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable) 
    Shot.containers = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2) 
    astroid_field = AsteroidField()

    while True  :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color = (0,0,0))

        for item in updatable:
            item.update(dt)
        
        for item in asteroids:
            if item.collision(player):
                print('Game over')
                exit(0)
            for bullet in shots:
                if item.collision(bullet):
                    item.split()
                    bullet.kill()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()