# -*- coding: utf-8 -*-
"""
level 2
"""
#importement
import pygame
import sys
pygame.init()


#nom fenetre
pygame.display.set_caption("redwood's space")


#class vaisseau
class vaisseau:
    def __init__(self, x, y, pv, vitesse_mov, vitesse_tir, image, sound):
        self.pv = pv            #points de vie du vaisseau
        self.coor = [x, y]       #coordonnes du vaisseau
        self.vitesse_m = vitesse_mov          #vitesse de mouvement
        self.vitesse_t = vitesse_tir               #vitesse de tir
        self.image = pygame.image.load(image)        #sprite du vaisseau
        self.sound = pygame.mixer.Sound(sound)       #bruitage du tir
        self.tirs = []           #liste des tirs du vaisseau    
    
    def tirer(self):    #methode pour tirer
        self.sound.play()       #play le sound
        self.tirs.append(self.coor)             #ajouter le tir a la liste
    


#variables
ecran = pygame.display.set_mode((1000, 800))   #fenetre de jeu

jouer = True             #bool de jeu
fin_jeu = False          #bool fin de jeu
quitter = False          #boolean de quittage


#objets vaisseau
joueur = vaisseau(465, 700, 3,)


#programme
     #jeu (pas besoin d'ecran titre)
while jouer:
    if not fin_jeu:
        
        #events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:      #si le joueur quitte
                quitter = True
                jouer = False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                

if quitter:       #quand le joueur quitte
    pygame.quit()
    sys.exit()
                    