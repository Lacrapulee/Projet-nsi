import pygame
from Classebouton import Bouton


class Menu() :
    
    def __init__(self):
        self.page_atuelle = 0
        self.nb_de_page = 10
        self.bouton_fleche_gauche = Bouton("Sprites/Boutons/Bouton_fleches.png", (0, 0), (100,100))
        #self.enigme = enigme


    def affiche(self, fenetre):
        """
        affiche les éléments du menu
        
        """
        #affichages des bouton avec la classe bouton
        self.bouton_fleche_gauche.affiche(fenetre)
        #for enigme in self.enigme:
        #    if enigme.page == self.page_atuelle:
        #        enigme.play()

    def change_page(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if pygame.mouse.get_pos()[0] > 400 and self.page_atuelle < 9: 
                self.page_atuelle += 1
                
                print("page d'après", self.page_atuelle) 
   
            if self.bouton_fleche_gauche.appuye_sur_bouton(event) and self.page_atuelle > 0: 
                self.page_atuelle -= 1 
                print("page d'avant", self.page_atuelle)
                print("appuye sur bouton")

    