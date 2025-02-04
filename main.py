import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
from ui import Ui

def main():

    score = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    ui = Ui()
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
        ui.draw_text(f"Score: {score}",screen,pygame.font.SysFont("Arial",30),(255,255,255),100,100)
        updatable_group.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    score += 1
                    asteroid.split()
                    bullet.kill()
            if asteroid.collision(player):
                print("Game Over")
                print(f"Final Score: {score}")
                pygame.QUIT
                return
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    pygame.init()
