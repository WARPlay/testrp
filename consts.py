import random
import sys
import pygame
import os


pygame.init()
run = False
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
win = pygame.display.set_mode((width, height))
gamesurface = pygame.Surface((width * 0.8, height * 0.65))
buttons = pygame.sprite.Group()
heroes = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites0 = pygame.sprite.Group()
all_sprites1 = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()
bfon = [pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Large Buttons/Start Button.png"), (width * 0.19, height * 0.2)), pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Colored Large Buttons/Start  col_Button.png"), (width * 0.19, height * 0.2))]
bfon1 = [pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Large Buttons/Controls Button.png"), (width * 0.19, height * 0.2)), pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Colored Large Buttons/Controls  col_Button.png"), (width * 0.19, height * 0.2))]
bfon2 = [pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Large Buttons/Exit Button.png"), (width * 0.19, height * 0.2)), pygame.transform.scale(pygame.image.load("assets/sprites/buttons/Large Buttons/Colored Large Buttons/Exit  col_Button.png"), (width * 0.19, height * 0.2))]

hero_move = pygame.image.load("assets/sprites/cyborg_platformer/cyber prisoner run cycle-Sheet.png")
hero_idle = pygame.image.load("assets/sprites/cyborg_platformer/cyber prisoner idle-Sheet.png")
hero_shoot = pygame.image.load("assets/sprites/cyborg_platformer/cyber prisoner Light attack slash-Sheet.png")

texturefloor = pygame.transform.scale(pygame.image.load("assets/sprites/textures/floor.jpg"), (width * 0.8, height * 0.65))
cur_image = pygame.transform.scale(pygame.image.load("assets/sprites/textures/cursor.png"), (50, 50))
bullet_image = pygame.image.load("assets/sprites/textures/sheet1.png")
fon = [pygame.transform.scale(pygame.image.load("assets/sprites/fon/" + i), (width, height)) for i in os.listdir("assets/sprites/fon/")]
pygame.display.set_caption("XXXXXXXXXXXXXXXXXXXXXXXXX")
font = pygame.font.SysFont('arial', 30)