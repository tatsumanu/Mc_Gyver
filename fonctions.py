
import pygame
import os


def load_image(name):
    fullname = os.path.join('graphics', name)
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image

