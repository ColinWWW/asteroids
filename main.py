import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    AsteroidField.containers = (updatable_group,)
    AsteroidField()
    Asteroid.containers = (asteroids,updatable_group,drawable_group)
    Shot.containers = (bullets,updatable_group, drawable_group)
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return


        screen.fill("black")
        updatable_group.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.collision(player):
                print("Game Over")
                pygame.QUIT
                return
        for drawable in drawable_group:
            print(f"Drawing: {type(drawable)}")
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
