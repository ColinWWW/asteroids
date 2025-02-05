#!/usr/bin/env python3
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, bullet_type=0):
        super().__init__(x, y, SHOT_RADIUS)
        self.sprite_sheet = pygame.image.load("./assets/bullet_sheet.png")

        self.sprite_width = 32
        self.sprite_height = 32
        self.columns = 4
        self.rows = 6
        self.image = self.get_bullet_sprite(bullet_type)

    def get_bullet_sprite(self, bullet_type):
        color = bullet_type // (self.columns * 3)
        remaining = bullet_type % (self.columns * 3)
        form = remaining // 3
        size = remaining % 3

        x = form * self.sprite_width
        y = (color * 3 + size) * self.sprite_height

        rect = pygame.Rect(x, y, self.sprite_width, self.sprite_height)
        return self.sprite_sheet.subsurface(rect)

    def draw(self, screen):
        image_rect = self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        offset_x = -6
        offset_y = -6

        image_rect.x += offset_x
        image_rect.y += offset_y
        screen.blit(self.image, image_rect)



    def update(self, dt):
        self.position += self.velocity * dt
