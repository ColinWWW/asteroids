#!/usr/bin/env python3
import pygame
import os
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    SPRITE_FOLDER = "./assets/moon_frames/"  # Adjust path if needed

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Load all frames from the folder
        self.frames = self.load_frames()
        self.current_frame = random.randint(0, len(self.frames) - 1)  # Start at a random frame
        self.frame_timer = 0  # Time tracker for animation speed
        self.animation_speed = 0.05  # Adjust speed (lower = faster animation)

    def load_frames(self):
        """Loads all PNG images from the folder in numerical order."""
        images = []
        for i in range(1, 61):  # Load from 1.png to 60.png
            file_path = os.path.join(self.SPRITE_FOLDER, f"{i}.png")
            if os.path.exists(file_path):  # Ensure the file exists before loading
                images.append(pygame.image.load(file_path).convert_alpha())

        if not images:
            raise RuntimeError("No frames found! Check your SPRITE_FOLDER path and file naming.")

        return images

    def draw(self, screen):
        """Draws the animated asteroid."""
        image = self.frames[self.current_frame]
        scale_factor = (self.radius*2) / image.get_width()
        scaled_size = (int(image.get_width() * scale_factor), int(image.get_height() * scale_factor))
        scaled_image = pygame.transform.scale(image, scaled_size)
        image_rect = scaled_image.get_rect(center=(int(self.position.x), int(self.position.y)))
        screen.blit(scaled_image, image_rect)

    def update(self, dt):
        """Updates asteroid movement and animation."""
        self.position += self.velocity * dt

        # Animate frame
        self.frame_timer += dt
        if self.frame_timer >= self.animation_speed:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)  # Loop animation


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
