#!/usr/bin/env python3

import pygame

class Ui():
    def __init__(self):
        pygame.init()
    def draw_text(self,text,screen, text_col, x, y):
        font = pygame.font.SysFont("Arial",30)
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))
    def draw_background(self, screen):
        image = pygame.image.load("./assets/background/backgroundart.png")
        screen.blit(image, (0,0))
