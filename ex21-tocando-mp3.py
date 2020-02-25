# #21 - https://www.youtube.com/watch?v=9FiEji_fzvk
# ex21-tocando-mp3.py
# Programa que abra e reproduza um arquivo mp3 de audío.

import pygame
pygame.init()
pygame.mixer.music.load('ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()