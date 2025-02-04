#!/usr/bin/env python3
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        neg_random_angle = random.uniform(-20,-50)
        new_vec1 = pygame.math.Vector2.rotate(self.velocity,random_angle)
        new_vec2 = pygame.math.Vector2.rotate(self.velocity,neg_random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y,self.radius - ASTEROID_MIN_RADIUS)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = new_vec1 * 1.2
        asteroid2.velocity = new_vec2 * 1.2
