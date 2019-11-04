import pygame
import os


# function loading ressources for the images of the game
def load_image(name):
    fullname = os.path.join('graphics', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


# Function creating an area on the window for text to be writen
def create_a_text_object(text, police):
    texte_surface = police.render(text, True, (0, 0, 0))
    return texte_surface, texte_surface.get_rect()


# Function that passes the text to the screen
def message(text, window, x=240, y=200, wide=50):
    police = pygame.font.Font(None, wide)
    comments_surface, comments_rect = create_a_text_object(text, police)
    comments_rect.center = x, y
    window.blit(comments_surface, comments_rect)


# If the conditions are matched, print to the screen the victory message
def victory(window, syringe):
    window.blit(syringe, (195, 115))
    message('Using the objects collected,', window, 240, 260, 30)
    message('Mac Gyver made a syringe to', window, 240, 310, 30)
    message('eliminate the guardian and exit the labyrinth', window, 240, 360, 30)
    message('As always, his adventures were to be continued', window, 240, 410, 30)
    message('at the next episode!', window, 240, 460, 30)
