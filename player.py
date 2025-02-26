
import pygame
import sys
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED, SHOT_RADIUS
from shot import Shot
from sounds import Sounds

class Player(CircleShape):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, PLAYER_RADIUS)
        self.rotation = 0
        self.ratecount = 0
        self.sounds = Sounds()

        self.ship_image = pygame.image.load("./assets/extracted_ship.png").convert_alpha()
        self.ship_image = pygame.transform.scale(self.ship_image,(96,96))
        self.ship_image = pygame.transform.rotate(self.ship_image,180)
        self.rect = self.ship_image.get_rect()


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius/1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.ship_image, -self.rotation)
        rotated_rect = rotated_image.get_rect()
        rotated_rect.center = self.position

        screen.blit(rotated_image, rotated_rect)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.ratecount > 0:
            return
        self.ratecount = PLAYER_SHOOT_COOLDOWN
        new_shot = Shot(self.position.x, self.position.y)
        self.sounds.play_blaster_sound()
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        new_shot.velocity = forward * PLAYER_SHOOT_SPEED




    def update(self,dt):
        self.ratecount -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
