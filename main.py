import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()
    Shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (Asteroids ,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (Shots ,updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    astrofield = AsteroidField()

    #____Game Loop____
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updatable.update(dt)

        for astro in Asteroids:
            if player.collision_check(astro):
                print("Game over!")
                return
            
        for astro in Asteroids:
            for bullet in Shots:
                if astro.collision_check(bullet):
                    astro.split()
                    bullet.kill()

        screen.fill("black")
        
        for i in drawable:
            i.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
    