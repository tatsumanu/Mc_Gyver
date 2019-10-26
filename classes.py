import pygame
from random import randrange


class Player:

    """ player class attributes, initiate object, and function 'move'
        takes events from pygame and check wether the player
        can move in this direction or not """

    def __init__(self, x, y, image, sprite=32, object=[]):
        self.x = x * sprite
        self.y = y * sprite
        self.image = image
        self.object = []

    def move(self, old_pos, new_pos, map):
        if map.is_obstacle(new_pos):
            self.x, self.y = old_pos
        else:
            self.x, self.y = new_pos
        return self.x, self.y


class Map:

    """ Map class attributes, defines the lab map, the position of the
    walls, the objects... """

    def __init__(self, x, y, player, grid=[], sprite=32):
        self.x = x
        self.y = y
        self.grid = grid
        self.player = player
        self.sprite = sprite

    def loading(self):
        with open('map.txt', 'r') as text_map:
            text_map_read = text_map.read()
        self.grid = [[self.y for self.y in self.x] for self.x in (text_map_read.split('\n'))]
        return self.grid

    def walling_the_lab(self, window, wall):
        for i in range(15):
            for j in range(15):
                if self.grid[i][j] == 'x':
                    window.blit(wall, (i*self.sprite, j*self.sprite))

    def is_obstacle(self, new_pos):
        a, b = new_pos
        self.player.x, self.player.y = a // self.sprite, b // self.sprite
        if self.player.x < 0 or self.player.x > 14 or self.player.y < 0 or self.player.y > 14:
            return True
        elif self.grid[self.player.x][self.player.y] == 'x':
            return True


class Object:

    def __init__(self, name, image, x=0, y=0):
        self.name = name
        self.x = x * 32
        self.y = y * 32
        self.image = image

    def print_object(self, window, player):
        if self.name in player.object:
            pass
        elif (self.x, self.y) == (player.x, player.y):
            if self.name not in player.object:
                player.object.append(self.name)
        else:
            window.blit(self.image, (self.x, self.y))
