import pygame
import os
from pygame.locals import *
from fonctions import load_image, create_a_text_object, message
from classes import Player, Map, Object


pygame.init()

# variables
name = ''
menu = 1
sprite = 32
play_game = True

# creating the screen game window
window = pygame.display.set_mode((480, 480))
pygame.display.set_caption('Mac Gyver et le labyrinthe infernal!')


# loading images
floor, wall = load_image('floor.png'), load_image('wall.png')
seringue = load_image('seringue.png')
intro = load_image('macgyver.jpg')

# creating player class object
mc_gyver = Player(0, 0, load_image('MacGyver.png'))
guardian = Player(14, 14, load_image('Gardien.png'))

# creating map class object
map = Map(0, 0, mc_gyver)

# creating elements of the object class
aiguille = Object('aiguille', load_image('aiguille.png'), 6, 4)
tube = Object('tube', load_image('tube_plastique.png'), 5, 9)
ether = Object('ether', load_image('ether.png'), 13, 5)

# loading the map
map.loading()

# main loop
while play_game:

    # intro loop
    while menu:

        pygame.time.Clock().tick(30)

        window.blit(intro, (0, 0))
        message("Appuyer sur une touche", window)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            elif event.type == KEYDOWN:
                menu = 0

    # game loop
    while mc_gyver.alive:

        pygame.time.Clock().tick(30)

        # checking the events
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

        # Printing the floor, walls, Mc Gyver, guardian and objects to the screen
        window.blit(floor, (0, 0))
        map.walling_the_lab(window, wall)
        window.blit(mc_gyver.image, (mc_gyver.x, mc_gyver.y))
        window.blit(guardian.image, (guardian.x, guardian.y))
        ether.print_object(window, mc_gyver)
        aiguille.print_object(window, mc_gyver)
        tube.print_object(window, mc_gyver)

        # checking victory/defeat conditions
        mc_gyver.alive, mc_gyver.kill_the_guardian = mc_gyver.facing_the_end((mc_gyver.x, mc_gyver.y))

        # screen update
        pygame.display.update()

    if mc_gyver.kill_the_guardian is True:
        message('YOU WIN !', window)
    else:
        message('GAME OVER !', window)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        elif event.type == KEYDOWN:
            quit()

quit()
