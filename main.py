import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot
from ui import Ui
from sounds import Sounds
def main():

    score = 0
    lives = 3
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    ui = Ui()
    sound = Sounds()
    AsteroidField.containers = (updatable_group,)
    AsteroidField()
    Asteroid.containers = (asteroids,updatable_group,drawable_group)
    Shot.containers = (bullets,updatable_group, drawable_group)
    dt = 0
    sound.play_background_music()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return


        screen.fill("black")
        ui.draw_background(screen)
        ui.draw_text(f"Score: {score}",screen,(255,255,255),100,100)
        ui.draw_text(f"Lives: {lives}",screen,(255,255,255),100,150)
        updatable_group.update(dt)
        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.collision(bullet):
                    sound.play_destruction_sound()
                    score += 1
                    asteroid.split()
                    bullet.kill()
            if asteroid.collision(player):
                lives -= 1
                asteroid.split()
                if lives <= 0:
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
