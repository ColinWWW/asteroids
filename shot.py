#!/usr/bin/env python3
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from ui import Ui

class Shot(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self,screen):
        image = pygame.image.load("./assets/laserbeam.png")
        new_size = (100,10)
        scaled_image = pygame.transform.scale(image, new_size)
        screen.blit(scaled_image,(self.position.x + 2 ,self.position.y + 2))
        pygame.draw.circle(screen,"white",self.position,self.radius, 2)

    def update(self,dt):
        self.position  += self.velocity * dt
