# sound functions
import pygame
# initiating music mixer
pygame.mixer.init()

class Sound:
    def play_del(self):
        pygame.mixer.music.load("delete.mp3")
        pygame.mixer.music.play(loops=0)


    def play_add(self):
        pygame.mixer.music.load("add.wav")
        pygame.mixer.music.play(loops=0)


    def play_cro(self):
        pygame.mixer.music.load("cross.mp3")
        pygame.mixer.music.play(loops=0)


    def play_unc(self):
        pygame.mixer.music.load("uncross.mp3")
        pygame.mixer.music.play(loops=0)