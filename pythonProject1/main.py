import random
import time

import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('LOL')
clock=pygame.time.Clock()
sky_sur = pygame.image.load('1.png').convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_att1 = pygame.image.load('aa-1.png.png').convert_alpha()
        player_att2 = pygame.image.load('aa-2.png.png').convert_alpha()
        player_att1_2 = pygame.image.load('aa-1.png2.png').convert_alpha()
        player_att2_2 = pygame.image.load('aa-2.png2.png').convert_alpha()

        self.player_att = [player_att1,player_att2,player_att1_2,player_att2_2]
        self.player_index = 0
        self.image = self.player_att[self.player_index]
        self.rect = self.image.get_rect(midbottom=(110,330))
        self.l_hitbox1 = (self.rect.x + 90, self.rect.y + 60, 130, 140)
        self.r_hitbox2 = (self.rect.x + 20, self.rect.y + 60, 105, 140)
        self.l_hitbox2 = (self.rect.x + 120, self.rect.y + 60, 110, 140)
        self.hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 60, 130, 140)
        self.r_hitbox_2 = pygame.Rect(self.r_hitbox2)
        self.l_hitbox_1 = pygame.Rect(self.l_hitbox1)
        self.l_hitbox_2 = pygame.Rect(self.l_hitbox2)

    def animation_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x>=-71:
            self.rect.x-=3
            self.player_index=2
        if keys[pygame.K_d] and self.rect.x<=640:
            self.rect.x+=3
            self.player_index=0
        if keys[pygame.K_w] and self.rect.y>=73:
            self.rect.y-=3
            if self.player_index==1 or self.player_index==3:
                self.player_index-=1
        if keys[pygame.K_s] and self.rect.y<=201:
            self.rect.y+=3
            if self.player_index==1 or self.player_index==3:
                self.player_index-=1
        self.image = self.player_att[self.player_index]
        self.l_hitbox1 = (self.rect.x + 90, self.rect.y + 60, 130, 140)
        self.r_hitbox2 = (self.rect.x + 20, self.rect.y + 60, 105, 140)
        self.l_hitbox2 = (self.rect.x + 120, self.rect.y + 60, 110, 140)
        self.hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 60, 130, 140)
        self.r_hitbox_2 = pygame.Rect(self.r_hitbox2)
        self.l_hitbox_1 = pygame.Rect(self.l_hitbox1)
        self.l_hitbox_2 = pygame.Rect(self.l_hitbox2)
        print(self.hitbox)
        if self.player_index==0:
            pygame.draw.rect(screen, 'red', self.hitbox, 2)
            pygame.draw.rect(screen,'blue',self.rect,2)
        if self.player_index==2:
            pygame.draw.rect(screen, 'red', self.l_hitbox_1, 2)
        if self.player_index == 1:
            pygame.draw.rect(screen, 'red', self.r_hitbox_2, 2)
        if self.player_index == 3:
            pygame.draw.rect(screen, 'red', self.l_hitbox_2, 2)


    def animation_att(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_index=3
            self.image = self.player_att[self.player_index]

        if keys[pygame.K_RIGHT]:
            self.player_index=1
            self.image = self.player_att[self.player_index]
    def update(self):
        self.animation_att()
        self.animation_move()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        enemy_sur = pygame.image.load('poro.gif').convert_alpha()
        self.enemy_att=[enemy_sur]
        self.enemy_index=0
        self.image = self.enemy_att[self.enemy_index]
        self.rect = self.image.get_rect(midbottom=(700,random.randint(300,400)))
        self.hitbox = pygame.Rect(self.rect.x,self.rect.y,60,60)
    def draw(self):
        pygame.draw.rect(screen, 'red', self.hitbox,2)
    def update(self):
        self.draw()



obstacle_timer = pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,900)
player_sur = pygame.image.load('aa.gif').convert_alpha()

enemy_pos= 800
enemy_sur = pygame.image.load('poro.gif').convert_alpha()
enemy_rect = enemy_sur.get_rect(bottomleft=(800,330))
player = Player()
enemy = Enemy()
playerg = pygame.sprite.GroupSingle()
playerg.add(Player())
enemyg = pygame.sprite.GroupSingle()
enemyg.add(Enemy())
player_rect = player.hitbox
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_sur,(0,0))
    playerg.draw(screen)
    playerg.update()
    enemyg.draw(screen)
    enemyg.update()
    player1 = player.hitbox
    enemy1 = enemy.hitbox
    collide = player1.colliderect(enemy1)
    if collide==False:
        print('false')
        print(player1)
    else:
        print('true')

    pygame.display.update()
    clock.tick(60)