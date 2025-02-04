#!/usr/bin/env python3

import pygame

class Ui():
    def __init__(self):
        pygame.init()
    def draw_text(self,text,screen, font, text_col, x, y):
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))
