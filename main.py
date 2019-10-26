import pygame
import os
from pygame.locals import *
from fonctions import load_image
from classes import Player, Map, Object


pygame.init()

# variables
name = ''
sprite = 32
game_over = False

# création de la fenêtre de jeu
window = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Mac Gyver et le labyrinthe infernal!')


# chargement des images et affectation dans une variable
floor, wall = load_image('floor.png'), load_image('wall.png')
seringue = load_image('seringue.png')


# instanciation des objets des classes Player et Map
mc_gyver = Player(0, 0, load_image('MacGyver.png'))
guardian = Player(14, 14, load_image('Gardien.png'))
map = Map(0, 0, mc_gyver)

aiguille = Object('aiguille', load_image('aiguille.png'), 6, 4)
tube = Object('tube', load_image('tube_plastique.png'), 5, 9)
ether = Object('ether', load_image('ether.png'), 13, 5)

# chargement de la carte
map.loading()

# affichage du sol, des murs et de Mac Gyver
window.blit(floor, (0, 0))
map.walling_the_lab(window, wall)


window.blit(mc_gyver.image, (mc_gyver.x, mc_gyver.y))
window.blit(guardian.image, (guardian.x, guardian.y))

# raffraichissement de la fenêtre de jeu
pygame.display.update()

# boucle principale du programme
while not game_over:

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            old_pos = mc_gyver.x, mc_gyver.y
            if event.key == K_DOWN:
                new_pos = (mc_gyver.x, mc_gyver.y + sprite)
                mc_gyver.move(old_pos, new_pos, map)
            if event.key == K_UP:
                new_pos = (mc_gyver.x, mc_gyver.y - sprite)
                mc_gyver.move(old_pos, new_pos, map)
            if event.key == K_LEFT:
                new_pos = (mc_gyver.x - sprite, mc_gyver.y)
                mc_gyver.move(old_pos, new_pos, map)
            if event.key == K_RIGHT:
                new_pos = (mc_gyver.x + sprite, mc_gyver.y)
                mc_gyver.move(old_pos, new_pos, map)

    window.blit(floor, (0, 0))
    map.walling_the_lab(window, wall)

    # ether.printing_obj(window)

    window.blit(mc_gyver.image, (mc_gyver.x, mc_gyver.y))
    window.blit(guardian.image, (guardian.x, guardian.y))

    ether.print_object(window, mc_gyver)

    aiguille.print_object(window, mc_gyver)
    tube.print_object(window, mc_gyver)
    print(tube.x, tube.y, mc_gyver.x, mc_gyver.y, mc_gyver.object)

    pygame.display.update()

quit()
