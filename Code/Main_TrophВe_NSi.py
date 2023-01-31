import pygame
from Classebouton import Bouton
from Menu import * 

def init():
    global fenetre, run, menu
    pygame.init()
    menu = Menu()
    fenetre = pygame.display.set_mode((1000, 1020))
    run = True 
    process()

 

def process():
    global fenetre, run, menu, event
    while run:        
        
        for event in pygame.event.get(): 
            
            if event.type == pygame.QUIT : 
                print('arret du jeu')
                run = False 

            update()
            update()

        pygame.display.flip()
    pygame.quit()


def update():
    global fenetre, run, menu
    menu.update(event, fenetre)


def draw():
    global fenetre, run, menu
    menu.draw(event, fenetre)

init()