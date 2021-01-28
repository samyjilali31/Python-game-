from cgitb import reset
from turtledemo.forest import start

import keyboard as keyboard
import pygame
import keyboard
from pygame.locals import *
from random import*
from pygame import time as T


pygame.init()
sound = pygame.mixer.music.load("musicgamew.wav")
pygame.mixer.music.play()
loop = 1
fenetre = pygame.display.set_mode((1920, 1200))
rectScreen = fenetre.get_rect()
police = pygame.font.Font("Flesh Wound.ttf",120)
start_ticks=pygame.time.get_ticks() #starter tick
t2  = (pygame.time.get_ticks() - start_ticks) / 1000
menu = pygame.image.load("Deuxboutons.png")
menu3 = pygame.image.load("Deuxboutons2.png")
fond = pygame.image.load("fond.jpg")
pic = pygame.image.load("pic.png")
pic_position = pic.get_rect()
pic_position.x = 1200
pic_position.y = 500
pygame.display.flip()
perso = pygame.image.load("iconperso2.png")
menu2 = pygame.image.load("Deuxboutons1.png")
epe = pygame.image.load("epee.png")
position_epe = epe.get_rect()
position_epe.x = 1000
position_epe.y = 200

sabre = pygame.image.load("katar2.png")
position_sabre = sabre.get_rect()
position_sabre.y = 200
position_sabre.x = 900

decor3 = pygame.image.load("canon.png")
fond.blit(decor3,(1410,770))

decor =0

if decor:
 decor1 = pygame.image.load("boite.png")
 fond.blit(decor1,(700,770))
 decor2 = pygame.image.load("or.png")
 fond.blit(decor2,(850,750))
 decor3 = pygame.image.load("canon.png")
 fond.blit(decor3,(1410,770))

icondim = pygame. transform. scale(perso, (350, 400))
position_perso = icondim.get_rect()
position_perso.x = 700
position_perso.y = 580
pygame.pressed = {}
pygame.display.flip()
continuer = 1
maskepe = pygame.mask.from_surface(epe)
maskpic = pygame.mask.from_surface(pic)
masksabre = pygame.mask.from_surface(sabre)
maskperso = pygame.mask.from_surface(perso)
maskmenu = pygame.mask.from_surface(menu)
pygame.mixer.init()
oui = 1
pause = 0
bouger = 1
menupause = 0
click = 0
curseurcentre = 0
curseurbas = 0
stable = 0
tempsseconds = 1
sound = pygame.mixer.music.load("musicgamew.wav")
pygame.mixer.music.play()



while continuer :

    if pause == False:
     position_sabre = position_sabre.move(0,1)
     position_epe = position_epe.move(0, 1)
     pic_position = pic_position.move(0,2)
     seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    texte = police.render("Time: "+(str(seconds)), True, pygame.Color("#FFEFFF"))

    if maskperso.overlap(maskepe, (position_epe.left - position_perso.left, position_epe.top - position_perso.top)) != None:
      position_epe = position_epe.move(0,16)
      position_sabre = position_sabre.move(2000,0)
      pic_position = pic_position.move(2000,0)
      sound = pygame.mixer.music.load("perdu.wav")
      pygame.mixer.music.play()
      start_ticks = pygame.time.get_ticks()
      texte = police.render("Time: " + (str(t2)), True, pygame.Color("#FFEFFF"))
      texte2 = police.render(str(seconds), True, pygame.Color("#FFEFFF"))
      bouger = 0
      menupause = 1
      tempsseconds = 0
      if position_epe.y > 300:
       position_epe.move(1500,0)
       pause = True

    if maskperso.overlap(masksabre,(position_sabre.left - position_perso.left, position_sabre.top - position_perso.top)) != None:
      position_epe = position_epe.move(2000, 0)
      position_sabre = position_sabre.move(0, 70)
      pic_position = pic_position.move(2000, 0)
      sound = pygame.mixer.music.load("perdu.wav")
      pygame.mixer.music.play()
      start_ticks = pygame.time.get_ticks()
      texte = police.render("Time: " + (str(t2)), True, pygame.Color("#FFEFFF"))
      texte2 = police.render(str(seconds), True, pygame.Color("#FFEFFF"))
      bouger = 0
      fenetre.blit(menu, (770, 400))
      menupause = 1
      tempsseconds = 0
      if position_sabre.y > 500:
       position_epe.move(1200, 0)
       pause = True

    if maskperso.overlap(maskpic,(pic_position.left - position_perso.left, pic_position.top - position_perso.top)) != None:
      position_epe = position_epe.move(2000, 0)
      position_sabre = position_sabre.move(2000, 0)
      pic_position = pic_position.move(0, 40)
      sound = pygame.mixer.music.load("perdu.wav")
      pygame.mixer.music.play()
      start_ticks = pygame.time.get_ticks()
      texte = police.render("Time: " + (str(t2)), True, pygame.Color("#FFEFFF"))
      texte2 = police.render(str(seconds),True,pygame.Color("#FFEFFF"))
      menupause = 1
      bouger = 0
      tempsseconds = 0

      if pic_position.y > 500:
       position_epe.move(1500, 0)
       pause = True

    if seconds >10 and bouger == 1:
        position_epe = position_epe.move(0, 3)
    if seconds >20 and seconds<30 and bouger == 1:
           position_sabre = position_sabre.move(0, 3)
           position_epe = position_epe.move(0, 2)
    if seconds >30 and seconds< 40 and bouger == 1:
        position_epe = position_epe.move(0, 2)
        position_sabre = position_sabre.move(0, 3)
    if seconds >40 and bouger == 1:
               position_epe = position_epe.move(0, 1)
               position_sabre = position_sabre.move(0, 1)
               pic_position = pic_position.move(0,3)
    if seconds > 50 and bouger == 1:
        position_epe = position_epe.move(0, 1)
        position_sabre = position_sabre.move(0, 2)
        pic_position = pic_position.move(0, 3)

    if seconds > 55 and bouger == 1:
        position_epe = position_epe.move(0, 1)
        position_sabre = position_sabre.move(0, 2)
        pic_position = pic_position.move(0, 1)

    if seconds > 70 and bouger == 1:
        position_epe = position_epe.move(0, 3)
        position_sabre = position_sabre.move(0, 1)
        pic_position = pic_position.move(0, 1)

    if seconds > 90 and bouger == 1:
        position_epe = position_epe.move(0, 1)
        position_sabre = position_sabre.move(0, 3)
        pic_position = pic_position.move(0, 3)


    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
    if event.type == KEYDOWN :
        if event.key == K_ESCAPE:
            continuer = 0
        if event.key == K_RIGHT and bouger == 1:
            position_perso = position_perso.move(8, 0)
            pygame.pressed[event.key] = True
        if event.key != K_RIGHT :
            pygame.pressed[event.key] = True
        if event.key == K_LEFT and bouger == 1:
            position_perso = position_perso.move(-8, 0)
            pygame.pressed[event.key] = True
        if event.key != K_LEFT:
            pygame.pressed[event.key] = True

    if position_epe.y > 1000:
         p= randint(320,1550)
         position_epe.x = p
         position_epe.y = 200
    if position_sabre.y > 1000:
         n = randint(320,1550)
         position_sabre.x = n
         position_sabre.y = 200
    if pic_position.y > 1000:
         n = randint(320,1550)
         pic_position.x = n
         pic_position.y = 200
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso, position_perso)
    fenetre.blit(sabre, position_sabre)
    fenetre.blit(epe, position_epe)
    fenetre.blit(pic, pic_position)

    if tempsseconds == 1:
     fenetre.blit(texte, (370, 250))

    if menupause:
        fenetre.blit(menu, (670, 370))
        fenetre.blit(texte2, (880,200))
        if event.type == KEYDOWN:
            if event.key != K_DOWN and click:
                curseurcentre = 0
            if event.key == K_DOWN and click:
                curseurcentre = 1
            if event.key != K_UP and curseurcentre:
                click = 1
            if event.key == K_UP and curseurcentre==1:
                click = 1
                curseurcentre = 0
            if event.key == K_UP and curseurcentre==0:
                 click = 0
                 curseurcentre =1
            if event.key == K_DOWN and curseurcentre:
                 curseurbas = 1
            if event.key != K_DOWN and curseurcentre:
                 curseurbas = 0

    if click :
        fenetre.blit(menu,(670,370))
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                menupause = 0
                pause = 0
                bouger = 1
                click = 0
                curseurcentre = 0
                start_ticks = pygame.time.get_ticks()  # starter tick
                sound = pygame.mixer.music.load("musicgamew.wav")
                pygame.mixer.music.play()
                tempsseconds = 1

    if curseurcentre:
     fenetre.blit(menu2,(670,370))
     click = 0
    if curseurbas:
       click = 0
       curseurcentre = 1
    if curseurcentre:
             click = 1
             curseurcentre = 1
    if curseurbas:
     fenetre.blit(menu3,(670,370))

    pygame.display.flip()

