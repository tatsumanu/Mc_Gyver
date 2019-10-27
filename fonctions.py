import pygame
import os


# function loading ressources for the images of the game
def load_image(name):
    fullname = os.path.join('graphics', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def create_a_text_object(text, police):
    texte_surface = police.render(text, True, (255, 255, 255))
    return texte_surface, texte_surface.get_rect()


def message(text, window):
    police = pygame.font.Font(None, 50)
    comments_surface, comments_rect = create_a_text_object(text, police)
    comments_rect.center = 240, 200
    window.blit(comments_surface, comments_rect)
