import random
import sys
import pygame
import consts as c
import math


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y,w, h, group, frames):
        super().__init__(group)
        self.frames = frames
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = pygame.Rect(x, y, w, h)
        self.rect = self.rect.move(x, y)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


#INTERFACE
def start(screenWidth, screenHeight, font, screen, group, fon, bfon, bfon1, bfon2):
    c.run = True
    AnimatedSprite(0, 0, screenWidth, screenHeight, group, fon)
    Button(screenWidth * 0.8, screenHeight * 0.3,screenWidth * 0.19, screenHeight * 0.2, "Играть", font, bfon, screen,
           group, begin)
    Button(screenWidth * 0.8, screenHeight * 0.5, screenWidth * 0.19, screenHeight * 0.2, "Играть", font, bfon1, screen,
           group, controls)
    Button(screenWidth * 0.8, screenHeight * 0.7, screenWidth * 0.19, screenHeight * 0.2, "Играть", font, bfon2, screen,
           group, exit)
    while c.run:
        screen.fill((0, 0, 0))
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.run = False
        keys = pygame.key.get_pressed()
        mkeys = pygame.mouse.get_pressed()
        if mkeys[0]:
            for i in c.buttons:
                i.check()
        group.update()
        group.draw(screen)
        pygame.display.flip()

def begin():
    c.run = False



def game(screen):
    c.run = True
    a = HeroHealthBar(90, 100, 85, 100, 80, 100, screen, c.width, c.height, c.font)
    hero = Hero(c.all_sprites2, 90, 100, 99, 100, 100, 100, 10, 100, 100)
    while c.run:
        c.gamesurface.fill((0, 0, 0))
        screen.fill((0, 0, 0))
        c.gamesurface.blit(c.texturefloor, (0, 0))
        c.heroes.draw(c.gamesurface)
        pygame.time.delay(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                c.run = False
        keys = pygame.key.get_pressed()
        #if mkeys[0]:
            #pygame.draw.rect(c.gamesurface, (255,255,0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 100, 100))
        hero.move()
        hero.draw()
        for i in c.bullets:
            i.move()
            i.check()
        c.bullets.draw(c.gamesurface)
        screen.blit(c.gamesurface, (c.width * 0.1, c.height * 0.1))

        a.draw()
        #group.draw(screen)
        pygame.display.flip()




def exit():
    sys.exit()

def controls():
    pass


class HeroHealthBar:
    def __init__(self, hp, MaxHP, st, MaxST, exp,MaxEXP, screen, screenWidth, screenHeight, font):
        self.HP = hp
        self.MaxHP = MaxHP
        self.HPk = round(self.HP / self.MaxHP, 2)
        self.ST = st
        self.MaxST = MaxST
        self.STk = round(self.ST / self.MaxST, 2)
        self.MaxEXP = MaxEXP
        self.EXP = exp
        self.EXPk = round(self.EXP / self.MaxEXP, 2)
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.font = font
        self.HPt = self.font.render(str(round(self.HPk * 100)) + "%", True,
                          (0, 0, 0))
        self.STt = self.font.render(str(round(self.STk * 100)) + "%", True,
                                    (0, 0, 0))
        self.EXPt = self.font.render(str(round(self.EXPk * 100)) + "%", True,
                                    (0, 0, 0))

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, self.screenHeight * 0.8, self.screenWidth * 0.3, self.screenHeight * 0.2), 5, 50)
        #HP
        pygame.draw.rect(self.screen, (100, 0, 0),
                         (self.screenWidth * 0.02, self.screenHeight * 0.81, self.screenWidth * 0.07,
                          self.screenHeight * 0.18), 0, 10)
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.screenWidth * 0.02, self.screenHeight * 0.81 + self.screenHeight * 0.18 * (1 - self.HPk), self.screenWidth * 0.07,
                          self.screenHeight * 0.18 * self.HPk), 0, 10)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.screenWidth * 0.02, self.screenHeight * 0.81, self.screenWidth * 0.07,
                          self.screenHeight * 0.18), 5, 10)
        self.screen.blit(self.HPt, (self.screenWidth * 0.04,self.screenHeight * 0.9))
        #ST
        pygame.draw.rect(self.screen, (100, 100, 0),
                         (self.screenWidth * 0.11, self.screenHeight * 0.81, self.screenWidth * 0.08,
                          self.screenHeight * 0.18), 0, 10)
        pygame.draw.rect(self.screen, (255, 255, 0),
                         (self.screenWidth * 0.11, self.screenHeight * 0.81 + self.screenHeight * 0.18 * (1 - self.STk),
                          self.screenWidth * 0.08,
                          self.screenHeight * 0.18 * self.STk), 0, 10)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.screenWidth * 0.11, self.screenHeight * 0.81, self.screenWidth * 0.08,
                          self.screenHeight * 0.18), 5, 10)
        self.screen.blit(self.STt, (self.screenWidth * 0.14, self.screenHeight * 0.9))
        #EXP
        pygame.draw.rect(self.screen, (0, 0, 100),
                         (self.screenWidth * 0.21, self.screenHeight * 0.81, self.screenWidth * 0.07,
                          self.screenHeight * 0.18), 0, 10)
        pygame.draw.rect(self.screen, (0, 0, 255),
                         (self.screenWidth * 0.21, self.screenHeight * 0.81 + self.screenHeight * 0.18 * (1 - self.EXPk),
                          self.screenWidth * 0.07,
                          self.screenHeight * 0.18 * self.EXPk), 0, 10)
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.screenWidth * 0.21, self.screenHeight * 0.81, self.screenWidth * 0.07,
                          self.screenHeight * 0.18), 5, 10)
        self.screen.blit(self.EXPt, (self.screenWidth * 0.23, self.screenHeight * 0.9))

    def update(self, hp, MaxHP, st, MaxST, exp,MaxEXP):
        self.HP = hp
        self.MaxHP = MaxHP
        self.HPk = round(self.HP / self.MaxHP, 2)
        self.ST = st
        self.MaxST = MaxST
        self.STk = round(self.ST / self.MaxST, 2)
        self.MaxEXP = MaxEXP
        self.EXP = exp
        self.EXPk = round(self.EXP / self.MaxEXP, 2)
        self.HPt = self.font.render(str(round(self.HPk * 100)) + "%", True,
                                    (0, 0, 0))
        self.STt = self.font.render(str(round(self.STk * 100)) + "%", True,
                                    (0, 0, 0))
        self.EXPt = self.font.render(str(round(self.EXPk * 100)) + "%", True,
                                     (0, 0, 0))


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, text, font, fon, screen, group, func):
        super().__init__(group, c.buttons)
        self.x, self.y, self.w, self.h, self.text, self.font, self.fon, self.screen = x, y, w, h, text, font, fon, screen
        self.rect = pygame.Rect(x, y, w, h)
        self.image0 = fon[0]
        self.image1 = fon[1]
        self.image = self.image0
        self.func = func

    def update(self):
        mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if self.x < mx < self.x + self.w and self.y < my < self.y + self.h:
            self.image = self.image1
        else:
            self.image = self.image0

    def check(self):
        if self.image == self.image1:
            self.func()


def drawlevel(level):
    pass

def generate(Floor):
    pass

def cut_sheet(sheet, columns, rows):
    frames = []
    w = sheet.get_width()
    h = sheet.get_height()
    rect = pygame.Rect(0, 0, w // columns,
                            h // rows)
    for j in range(rows):
        for i in range(columns):
            frame_location = (rect.w * i, rect.h * j)
            frames.append(pygame.transform.scale(sheet.subsurface(pygame.Rect(
                frame_location, rect.size)), (100, 100)))
    return frames

def between(x, x1, y):
    if x < y < x1:
        return True
    else:
        return False

def mod(a, b):
    result = a - b
    return result * -1 if result <= 0 else result


def count_angle(x0, y0, x1, y1):
    if x1 == x0:
        if x1 > x0:
            return math.pi * 0.5
        else:
            return math.pi * 1.5
    elif y0 == y1:
        if y1 > y0:
            return math.pi
        else:
            return 0
    else:
        if y1 > y0:
            return math.atan((x1 - x0) / (y1 - y0))
        else:
            return math.atan((x1 - x0) / (y1 - y0)) + math.pi


class Hero(pygame.sprite.Sprite):
    def __init__(self, group, hp, MaxHP, st, MaxST, exp,MaxEXP, v, x, y):
        super().__init__(group, c.heroes)
        self.HP = hp
        self.MaxHP = MaxHP
        self.ST = st
        self.MaxST = MaxST
        self.EXP = exp
        self.MaxEXP = MaxEXP
        self.v = v
        self.damage = 10
        self.x, self.y = x, y
        self.cur_frame = 0
        self.rect = pygame.Rect(x, y, 100, 100)
        self.frames_move = cut_sheet(c.hero_move, 8, 1)
        self.frames_idle = cut_sheet(c.hero_idle, 8, 1)
        self.frames_shoot = cut_sheet(c.hero_shoot, 9, 1)
        for i in range(len(self.frames_shoot)):
            self.frames_shoot[i] = pygame.transform.scale(self.frames_shoot[i], (200, 100))

        self.image = self.frames_idle[self.cur_frame]
        self.moving = False
        self.stay = True
        self.shooting = False
        self.direction = "right"
        self.size = (100, 100)

    def move(self):
        keys = pygame.key.get_pressed()
        mkeys = pygame.mouse.get_pressed()
        f = 0
        if not self.shooting:
            if keys[pygame.K_w]:
                if between(0, c.gamesurface.get_height() - self.size[1], self.y - self.v):
                    self.y -= self.v
                    f = 1
            if keys[pygame.K_a]:
                if between(0, c.gamesurface.get_width() - self.size[0], self.x - self.v):
                    self.x -= self.v
                    f = 1
                self.direction = "left"
            if keys[pygame.K_s]:
                if between(0, c.gamesurface.get_height() - self.size[1], self.y + self.v):
                    self.y += self.v
                    f = 1
            if keys[pygame.K_d]:
                if between(0, c.gamesurface.get_width() - self.size[0], self.x + self.v):
                    self.x += self.v
                    f = 1
                self.direction = "right"
        if not self.shooting:
            if mkeys[0]:
                self.shoot()
        if f != 0:
            self.moving = True
            self.stay = False
        else:
            self.moving = False
            self.stay = True


    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        if self.shooting:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames_shoot)
            if self.cur_frame in [1, 6]:
                if -math.pi < count_angle(self.x + c.width * 0.1, self.y + c.height * 0.1, pygame.mouse.get_pos()[0],
                                       pygame.mouse.get_pos()[1]) < math.pi:
                    self.image = self.frames_shoot[self.cur_frame]
                    Bullet(self.damage,
                           count_angle(self.x + c.width * 0.1, self.y + c.height * 0.1, pygame.mouse.get_pos()[0],
                                       pygame.mouse.get_pos()[1]), 0, 25, self.x + self.rect.size[0] * 0.75,
                           self.y + self.rect.size[1] / 2)
                else:
                    self.image = pygame.transform.flip(self.frames_shoot[self.cur_frame], True, False)
                    Bullet(self.damage,
                           count_angle(self.x + c.width * 0.1, self.y + c.height * 0.1, pygame.mouse.get_pos()[0],
                                       pygame.mouse.get_pos()[1]), 0, 25, self.x + self.rect.size[0] * 0.2,
                           self.y + self.rect.size[1] / 2)
            if self.cur_frame == 8:
                self.shooting = False
        else:
            if self.moving:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_move)
                if self.direction == "right":
                    self.image = self.frames_move[self.cur_frame]
                else:
                    self.image = pygame.transform.flip(self.frames_move[self.cur_frame], True, False)
            elif self.stay:
                self.cur_frame = (self.cur_frame + 1) % len(self.frames_idle)
                if self.direction == "right":
                    self.image = self.frames_idle[self.cur_frame]
                else:
                    self.image = pygame.transform.flip(self.frames_idle[self.cur_frame], True, False)

    def shoot(self):
        self.shooting = True
        self.cur_frame = -1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, damage, angle, side, speed, x, y):
        super().__init__(c.bullets)
        self.damage, self.angle, self.side, self.speed = damage, angle, side, speed
        self.vx = self.speed * math.sin(self.angle)
        self.vy = self.speed * math.cos(self.angle)
        self.texture = cut_sheet(c.bullet_image, 5, 6)[::-1]
        for i in range(len(self.texture)):
            self.texture[i] = pygame.transform.scale(pygame.transform.rotate(self.texture[i], 180), (c.width * 0.05, c.height * 0.05))
            self.texture[i] = pygame.transform.rotate(self.texture[i], 180 * self.angle / math.pi)
        self.currentframe = 0
        self.image = self.texture[self.currentframe]
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 10, 10)


    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.currentframe += 1
        if self.currentframe == 15:
            self.kill()
        self.image = pygame.transform.scale(self.texture[0], (self.rect.size[0] + 15 * self.currentframe, self.rect.size[1] + 15 * self.currentframe))

    def check(self):
        if between(0, c.gamesurface.get_width() - 10, self.x) and between(0, c.gamesurface.get_height() + 10, self.y):
            self.rect = pygame.Rect(self.x, self.y, 10, 10)
        else:
            self.kill()


class Enemy:
    def __init__(self):
        pass


class Boss:
    def __init__(self):
        pass