import pygame 
from pygame.locals import *
from Main_TrophВe_NSi import fenetre

class Bouton():
    
    def __init__(self, Sprite = str(), Position =(None, None) , Taille = (None, None)):
        """
            Initiateur de la classe bouton
            Prend en parametre le Sprite, 
            la position (x, y), et la taille (x, y) 
        """
        self.sprite = Sprite
        self.position = (Position[0], Position[1])
        self.taille = (Taille[0], Taille[1])

    def est_sur_bouton(self):
        """
            Retourne True si le joueur 
            à sa souris sur le bouton
        """
        #Position de la souris 
        mousex = pygame.mouse.get_pos()[0]
        mousey= pygame.mouse.get_pos()[1]
        
        #Encadrement des positions de la souris 
        if self.position[0] + self.taille[0]>= mousex \
        >= self.position[0] - self.taille[0]:

            if self.position[1] + self.taille[1] >= mousey \
            >= self.position[1] - self.taille[1]:
                return True 


    def affiche(self):
        """
            Affiche le Sprite
        """
        #On chagre l'image dans pygame et on redefini sa taille 
        image = pygame.image.load(self.sprite).convert_alpha()
        pygame.transform.scale(image, self.taille)
        #Puis on la met dans la fenetre 
        fenetre.blit(image, self.position)
        
        



    def appuye_sur_bouton(self, event):
        """
            Retourne True si le joueur est 
            à cliqué sur le bouton en utilisant 
            la fonction est_sur_bouton()
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.est_sur_bouton():
                return True 