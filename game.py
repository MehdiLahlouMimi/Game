#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Space invaders
@author: the only one redwood soleil (he is so handsome)
demo
"""
#importement
import pygame
import sys
import random
import time
pygame.init()


#nom fenetre
pygame.display.set_caption("redwood's space")

#variables

w = 70     #weight standarde
h = 80     #height standarde

x = 500 - 35          #abscisse du vaisseau
y = 700          #ordonnee du vaisseau
X = x - 35          #abscisse de l'alien
Y = 70          #ordonnee de l'alien

a = 0         #variable essentielle pour etoile

ecran = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()   #pour mettre les FPS

vaisseau = pygame.image.load('vaisseau.png')
vaisseau = pygame.transform.scale(vaisseau, (w, h))  #resize de l'image
alien = pygame.image.load("alien.png").convert_alpha()     #import et transparence
alien = pygame.transform.scale(alien, (w, h))

icone = pygame.transform.scale(alien, (64, 64))
pygame.display.set_icon(icone)        #icone du jeu

tir = pygame.mixer.Sound('tir.wav')     #tir vaisseau
tir_ennemi = pygame.mixer.Sound('tir-ennemi.wav')   #tir ennemi
ambiance = pygame.mixer.Sound('musique.wav')

font = pygame.font.SysFont("papyrus", 72)
font_ = pygame.font.SysFont("papyrus", 30)

ver, hor = 0, 0           #wallah frere je sais pas a quoi sa sert

pv_alien = 50             #points de vie de l'alien
pv_vaisseau = 3            #points de vie du vaisseau

bouger = 0             #variable de mouvement de l'alien
valeurs = [-1, 0, 1]

liste_tirs = []      #liste des tirs effectues par le joueur

tirs_alien = []          #liste des tirs de l'alien
tirage = 0              #variable pour que l'alien tire

jouer = False         #bool de jeu
fin_jeu = False       #bool de fin de jeu
quitter = False      #bool de quittage
ecran_titre = True       #bool ecran titre

debut = time.time()        #debut du jeu

#couleurs
blue = (0, 0, 255)
red = (255, 0, 0)
orange = (255,165,0)
yellow = (255,255,0)
white = (255, 255, 255)
black = (0, 0, 0)
blue_ = (0, 100, 155)


#fonctions pour tirer
def tirer(a):
    if a % 2 == 0:        
        tir.play()
        liste_tirs.append([x+35, y])
  
    else:
        tir_ennemi.play()
        tirs_alien.append([X + w/2, Y+h])
        

#musique
ambiance.play()


#programme

  #ecran titre
while ecran_titre:
    
    text_debut = font_.render("REDWOOD'S SPACE [press R to start playing]", True, blue_)
    rect_text = text_debut.get_rect()
    ecran.blit(text_debut, (500 - rect_text[2]/2, 400 - rect_text[3]/2))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitter = True
            ecran_titre = False
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            jouer = True
            ecran.fill(black)
            ecran_titre = False 
  #jeu
  
while jouer:
    
    
    if not fin_jeu:
    
        a = 0                                          #generateur d'etoiles        
        rect_alien = pygame.Rect(X, Y, w, h)           #Rect associe a l'alien
        rect_vaisseau = pygame.Rect(x, y, w, h)        #Rect associe au vaisseau
        text = font.render("PV : {}/50".format(pv_alien), True, yellow)  
        text_ = font.render("PV : {}/3".format(pv_vaisseau), True, red)
        
        
        #mouvement vaisseau
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and x > 0:  #le and c'est pour pas sortir de l'ecran
            x -= 3
        if pressed[pygame.K_RIGHT] and x < 930: #pareil
            x += 3
        
        #mouvement alien
        if bouger == 30:    
            ver , hor = random.choice(valeurs) , random.choice(valeurs)
            bouger = 0
            
        if X + ver*3 >= 0 and X + ver*3 + w <= 1000:
            X += ver*5
        
        if Y + hor*3 >= 0 and Y + hor*3 + h <= 500:
            Y += hor*3

        #tir alien 
        if tirage == 50 :
            tirer(1)
            tirage = 0
        
        
        #evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #quand il quitte la fenetre
                quitter = True
                jouer = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                tirer(2)
    
    
    
        #affichage des bullets et leur collision
            
            #du vaisseau
        for i in liste_tirs:
            
            rect_tir = pygame.Rect(i[0], i[1], 3, 6)    #rect associe a chaque tir
            
            if rect_tir.colliderect(rect_alien):    #collision du tir
                pv_alien -= 1
                liste_tirs.remove(i)
                
               
            
            elif i[1] <= 0 :                  #pour pas que le jeu ne commence à ramer sa mère
                liste_tirs.remove(i)
                
            else:
                i[1] -= 5
                pygame.draw.rect(ecran, red, rect_tir, 0)
                ecran.blit(vaisseau, [x, y])
                
            #de l'alien
        for o in tirs_alien:
            
            rect_tir_ = pygame.Rect(o[0], o[1], 3, 6)          #rect associe a chaque tir de l'ennemi
            
            if rect_tir_.colliderect(rect_vaisseau):              #collision du tir avec le vaisseau
                pv_vaisseau -= 1
                tirs_alien.remove(o)
            
            elif o[1] >= 800:                       #pour eviter que le jeu ramme
                tirs_alien.remove(o)
            
            else:
                o[1] += 5
                pygame.draw.rect(ecran, yellow, rect_tir_, 0)
                ecran.blit(alien, [X, Y])
        
          
        
        #si l'un des deux meurs
        if pv_alien <= 0 or pv_vaisseau <= 0:
            fin = time.time()
            fin_jeu = True        
            
            
        #collision des deux antagonistes
        if rect_alien.colliderect(rect_vaisseau) or rect_vaisseau.colliderect(rect_alien):
            pv_vaisseau -= 1
            
        #affichage vaisseau, alien, etc......   
        ecran.blit(vaisseau, [x, y])
        ecran.blit(alien, [X, Y])
        ecran.blit(text, (0,0))
        ecran.blit(text_, (0,750))
        
        
        while a <= 2:                #etoiles aleatoires
            pygame.draw.circle(ecran, white, [random.randint(0,1000), random.randint(0,800)], 1)
            a += 1 
        
        bouger += 1      #augmentation de l'indice de mouvement
        tirage += 1      #augmentation de l'indice de tir
        
        pygame.display.update()
        ecran.fill(black)
        clock.tick(60)

#fin du jeu    
    else:
        
        #time score
        duree = fin - debut
        
        #text de congratulance
        ecran.fill(black)
        text_fin = font.render("Bravo, your score {}, level 2 is starting in 12 seconds".format(int(duree)), True, yellow)      #felicitations
        rect_fin =  text_debut.get_rect()                                                                                   
        texte_fin_ = font.render("You failed", True, yellow)            #depression                
        rect_fin_ = texte_fin_.get_rect()
        
        if pv_alien <= 0 and pv_vaisseau > 0:         #si le joueur a gagne
            ecran.blit(text_fin, (500 - rect_fin[2]/2, 400 - rect_fin[3]/2))
            #on stoppe le time
      
        
        else:                    #si le joueur a perdu
            ecran.blit(texte_fin_, (500 - rect_fin_[2]/2, 400 - rect_fin_[3]/2))
        
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #quand il quitte la fenetre
                quitter = True
                jouer = False
        
if quitter: #quand le joueur quitte
    pygame.quit()
    sys.exit()
