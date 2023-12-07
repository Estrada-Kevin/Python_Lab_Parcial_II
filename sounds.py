from pygame.locals import *
from pygame import mixer
import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
#load sounds
coin_fx = pygame.mixer.Sound("sounds/coin.wav")
game_over_fx = pygame.mixer.Sound("sounds/game_over.wav")
jump_fx = pygame.mixer.Sound("sounds/jump.wav")
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play(-1,0.0,5000)


#volume of sounds
coin_fx.set_volume(0.5)
game_over_fx.set_volume(0.5)
jump_fx.set_volume(0.5)
