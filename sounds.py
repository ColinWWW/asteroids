#!/usr/bin/env python3

from pygame import mixer

class Sounds:
    def __init__(self):
        mixer.init()

    def play_background_music(self):

        mixer.music.load("./assets/music/gamemusic.mp3")
        mixer.music.set_volume(0.08)
        mixer.music.play(-1)

    def play_blaster_sound(self):
        blaster_sound = mixer.Sound("./assets/gamesound/blaster.mp3")
        blaster_sound.set_volume(0.05)
        blaster_sound.play()

    def play_destruction_sound(self):
        destruction_sound = mixer.Sound("./assets/gamesound/destruction.mp3")
        destruction_sound.set_volume(0.1)
        destruction_sound.play()
