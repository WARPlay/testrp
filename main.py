import random
import os
import pygame
from classes import HeroHealthBar, start, game
import consts as c



#pygame.init()
start(c.width, c.height, c.font, c.win, c.all_sprites0, c.fon, c.bfon, c.bfon1, c.bfon2)
game(c.win)