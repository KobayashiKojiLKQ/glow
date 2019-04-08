import pygame as pg
import os
import math
import time
import settings

class character():
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0

    def control(self, x, y):
        '''
        control player movement
        :param x: the value by which to move in the x dimension
        :param y: the value by which to move in the y dimension
        :return:
        '''
        self.movex += x
        self.movey += y

    def update(self):
        '''
        update sprite position
        :return:
        '''
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey