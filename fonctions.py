import pygame
import os


# function loading ressources for the images of the game
def load_image(name):
    fullname = os.path.join('graphics', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def create_a_text_object(text, police):
    texte_surface = police.render(text, True, (0, 0, 0))
    return texte_surface, texte_surface.get_rect()


def message(text, window, x=240, y=200, wide=50):
    police = pygame.font.Font(None, wide)
    comments_surface, comments_rect = create_a_text_object(text, police)
    comments_rect.center = x, y
    window.blit(comments_surface, comments_rect)


def victory(window, syringe):
    window.blit(syringe, (195, 115))
    message('Using the objects collected,', window, 240, 260, 35)
    message('Mac Gyver made a syringe to', window, 240, 310, 35)
    message('eliminate the guardian and exit the labyrinth', window, 240, 360, 35)
    message('As always, his adventures were to be continued', window, 240, 410, 35)
    message('at the next episode!', window, 240, 460, 35)
