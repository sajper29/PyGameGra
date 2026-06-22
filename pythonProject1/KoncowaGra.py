import random
import time
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
import pygame
from sys import exit




def main():
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            player_att1 = pygame.image.load('aa-1.png.png').convert_alpha()
            player_att2 = pygame.image.load('aa-1.png2.png').convert_alpha()
            player_att1_2 = pygame.image.load('aa-2.png.png').convert_alpha()
            player_att2_2 = pygame.image.load('aa-2.png2.png').convert_alpha()
            self.player_att = [player_att1, player_att2, player_att1_2, player_att2_2]
            self.player_index = 0
            self.image = self.player_att[self.player_index]
            self.rect = self.image.get_rect(midbottom=(110, 330))
            self.swordsound = pygame.mixer.Sound('kl-peach-game-over-iii-142453.mp3')
            self.swordsound.set_volume(0.01)
            self.doplay=False



        def animation_move(self):
            self.doplay=False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d] and self.rect.x <= 580:
                self.rect.x += 3
                self.player_index = 0
            if keys[pygame.K_a] and self.rect.x >= -71:
                self.rect.x -= 3
                self.player_index = 2
            if keys[pygame.K_w] and self.rect.y >= 73:
                self.rect.y -= 3
                if self.player_index == 1 or self.player_index == 3:
                    self.player_index -= 1
            if keys[pygame.K_s] and self.rect.y <= 201:
                self.rect.y += 3
                if self.player_index == 1 or self.player_index == 3:
                    self.player_index -= 1
            self.image = self.player_att[self.player_index]
            self.r_hitbox_1 = pygame.Rect(self.rect.x + 100, self.rect.y + 150, 100, 52)
            self.l_hitbox_1 = pygame.Rect(self.rect.x + 100, self.rect.y + 150, 100, 52)
            self.r_hitbox_2 = pygame.Rect(self.rect.x + 100, self.rect.y + 60, 80, 140)
            self.l_hitbox_2 = pygame.Rect(self.rect.x + 120, self.rect.y + 60, 80, 140)
            self.latt1 = pygame.Rect(self.rect.x, self.rect.y + 130, 120, 45)
            self.latt2 = pygame.Rect(self.rect.x + 180, self.rect.y + 130, 120, 45)
            return self.r_hitbox_1, self.l_hitbox_1, self.latt1, self.latt2

        def animation_att(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player_index = 3
                self.image = self.player_att[self.player_index]
                self.doplay=True
            if keys[pygame.K_RIGHT]:
                self.player_index = 1
                self.image = self.player_att[self.player_index]
                self.doplay=True
            if self.doplay==True:
                self.swordsound.play()
                doplay=False
            return self.player_index

        def update(self):
            self.animation_att()
            self.animation_move()

    class Enemy(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            enemy_sur1 = pygame.image.load('poro-1.png.png').convert_alpha()
            enemy_sur2 = pygame.image.load('poro-3.png.png').convert_alpha()
            enemy_sur1_2 = pygame.image.load('poro-2.png.png').convert_alpha()
            enemy_sur2_2 = pygame.image.load('poro-4.png.png').convert_alpha()

            self.enemy_att1 = [enemy_sur1,enemy_sur1_2]
            self.enemy_att2 = [enemy_sur2,enemy_sur2_2]
            self.enemy_index = 0
            self.image = self.enemy_att1[self.enemy_index]
            self.lista = [-60, 860]
            self.rect = self.image.get_rect(midbottom=(860, random.randint(245, 340)))
            self.posx = 860

        def movement(self):
            if self.rect.x>=-60 and self.posx==-60:
                self.rect.x+=7
            elif self.rect.x<=860 and self.posx==860:
                self.rect.x-=7
            if self.rect.x<-60:
                self.rect.x=random.choice(self.lista)
                self.rect.y=random.randint(245,340)
                self.posx = self.rect.x
            if self.rect.x>860:
                self.rect.x = random.choice(self.lista)
                self.rect.y = random.randint(245, 340)
                self.posx = self.rect.x
            if self.posx==-60:
                self.enemy_index+=0.1
                if self.enemy_index>=len(self.enemy_att2):
                    self.enemy_index=0
                self.image = self.enemy_att2[int(self.enemy_index)]
                screen.blit(self.image, self.rect)
            if self.posx==860:
                self.enemy_index+=0.1
                if self.enemy_index>=len(self.enemy_att1):
                    self.enemy_index=0
                self.image = self.enemy_att1[int(self.enemy_index)]
                screen.blit(self.image, self.rect)
            print(self.enemy_index)
            print(self.posx)
            return self.rect
        def zabij(self):
            self.rect=self.image.get_rect(midbottom=(random.choice(self.lista),random.randint(245,340)))

    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('LOL')
    clock = pygame.time.Clock()
    sky_sur = pygame.image.load('1.png').convert_alpha()
    menu_active = True
    controls_active = False
    over_menu = False
    game_active=False

    def pocz():
        font_1 = pygame.font.Font('Fonts_Package/BeaufortForLoL-OTF/BeaufortforLOL-Bold.otf', 90)
        font_2 = pygame.font.Font('Fonts_Package/BeaufortForLoL-OTF/BeaufortforLOL-Bold.otf', 55)
        font_3 = pygame.font.Font('Fonts_Package/BeaufortForLoL-OTF/BeaufortforLOL-Bold.otf', 35)
        playerg = pygame.sprite.GroupSingle()
        playerg.add(Player())
        player = Player()
        enemy = Enemy()
        text_1 = font_1.render('Start', True, '#d39e3b')
        text_2 = font_2.render('Controls', True, '#d39e3b')
        text_1_rect = text_1.get_rect(midleft=(0, 200))
        text_2_rect = text_2.get_rect(midright=(800, 200))
        text_3 = font_1.render('Move---WSAD', True, '#d39e3b')
        text_4 = font_1.render('Attack---Arrows', True, '#d39e3b')
        text_3_rect = text_3.get_rect(center=(400, 100))
        text_4_rect = text_4.get_rect(center=(400, 300))
        text_5 = font_1.render('Main Menu', True, '#d39e3b')
        text_6 = font_1.render('Retry', True, '#d39e3b')
        text_5_rect = text_5.get_rect(center=(520, 100))
        text_6_rect = text_6.get_rect(center=(300, 300))
        text_hp1 = font_3.render('1HP',True,'black')
        text_hp2 = font_3.render('2HP', True, 'black')
        text_hp3 = font_3.render('3HP', True, 'black')
        text_hp1_rect = text_hp1.get_rect(topleft=(0,0))
        text_hp2_rect = text_hp2.get_rect(topleft=(0,0))
        text_hp3_rect = text_hp3.get_rect(topleft=(0,0))


        nonlocal menu_active
        nonlocal controls_active
        nonlocal over_menu
        nonlocal game_active
        score1=0
        counting = 0
        countinghp=0
        hp = text_hp3
        hp_rect=text_hp3_rect

        timer = pygame.USEREVENT +1
        pygame.time.set_timer(timer, 3000)


        collide = False
        invis = False

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type==timer and game_active==True and invis == True:
                    invis=False


            if  menu_active==True:
                screen.fill('#0a717d')
                mouse_stan = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                logo = pygame.image.load('gallery-1.png.png')
                logo_rect = logo.get_rect(midbottom=(400,400))
                screen.blit(logo,logo_rect)
                screen.blit(text_1,text_1_rect)
                screen.blit(text_2,text_2_rect)
                if text_1_rect.collidepoint(mouse_pos) :
                    text_1 = font_1.render('Start',True,'#0b2731')
                else:
                    text_1 = font_1.render('Start', True, '#d39e3b')
                if text_2_rect.collidepoint(mouse_pos):
                    text_2 = font_2.render('Controls',True,'#0b2731')
                else:
                    text_2 = font_2.render('Controls', True, '#d39e3b')
                if text_1_rect.collidepoint(mouse_pos) and mouse_stan[0]==True:
                    menu_active=False
                    game_active=True
                elif text_2_rect.collidepoint(mouse_pos) and mouse_stan[0]==True:
                    menu_active=False
                    controls_active=True
                else:
                    menu_active=True
                    game_active=False
            elif controls_active==True:
                backes = pygame.image.load('pobrany plik-1.png.png')
                mouse_stan2 = pygame.mouse.get_pressed()
                mouse_pos2 = pygame.mouse.get_pos()
                backes_rect=backes.get_rect(topleft = (0,0))
                screen.fill('#0a717d')
                screen.blit(text_3,text_3_rect)
                screen.blit(text_4,text_4_rect)
                screen.blit(backes,backes_rect)

                if backes_rect.collidepoint(mouse_pos2) and mouse_stan2[0]==True:
                    menu_active=True
                    controls_active=False
                    game_active=False
            elif game_active==True:
                pygame.mixer.music.load('kl-peach-game-over-iii-142453.mp3')
                pygame.mixer.music.set_volume(0.01)
                pygame.mixer.music.play()
                screen.blit(sky_sur,(0,0))
                score1 = int(pygame.time.get_ticks() / 1000)+counting
                text_7 = font_3.render(f'{score1}', True, 'black')
                text_7_rect = text_7.get_rect(center=(400, 30))
                screen.blit(text_7, text_7_rect)
                print(score1)
                if score1>=100:
                    game_active==False
                    menu_active==True
                screen.blit(hp,hp_rect)
                enemy1 = enemy.movement()
                playerg.draw(screen)
                playerg.update()
                player1 = player.animation_move()
                player2 = player.animation_att()
                if player1[0].colliderect(enemy1) == True or player1[1].colliderect(enemy1) == True:
                    collide=True

                    if invis==False:
                        enemy.zabij()
                        counting -= 50
                if player1[2].colliderect(enemy1) == True and player2 == 3 or player1[3].colliderect(
                        enemy1) == True and player2 == 1:
                    enemy.zabij()
                    counting+=5
                if collide==True:
                    if invis == False:
                        countinghp += 1
                        if countinghp == 1:
                            hp = text_hp2
                            hp_rect = text_hp2_rect
                        if countinghp == 2:
                            hp = text_hp1
                            hp_rect = text_hp1_rect
                        if countinghp == 3:
                            game_active=False
                            over_menu=True
                        invis = True
                    collide=False
            elif over_menu==True:
                mouse_stan3 = pygame.mouse.get_pressed()
                mouse_pos3 = pygame.mouse.get_pos()
                screen.fill('#0a717d')
                screen.blit(text_5, text_5_rect)
                screen.blit(text_6, text_6_rect)
                if text_5_rect.collidepoint(mouse_pos3) :
                    text_5 = font_1.render('Retry',True,'#0b2731')
                else:
                    text_5 = font_1.render('Retry', True, '#d39e3b')
                if text_6_rect.collidepoint(mouse_pos3):
                    text_6 = font_1.render('Main Menu',True,'#0b2731')
                else:
                    text_6 = font_1.render('Main Menu', True, '#d39e3b')
                if text_5_rect.collidepoint(mouse_pos3) and mouse_stan3[0]==True:
                    menu_active=False
                    over_menu=False
                    controls_active=False
                    game_active=True
                    pocz()
                elif text_6_rect.collidepoint(mouse_pos3) and mouse_stan3[0]==True:
                    menu_active=True
                    controls_active=False
                    over_menu=False
                    game_active=False
                    pocz()
            else:
                print("ERROR")
            pygame.display.update()
            clock.tick(60)
    pocz()
main()