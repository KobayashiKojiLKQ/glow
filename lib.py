import pygame as pg
import os
import math
import time
import settings

pg.init()


class Object(pg.sprite.Sprite):
    def __init__(self, xpos, ypos):
        pg.sprite.Sprite.__init__(self)

        self.xpos = xpos
        self.ypos = ypos
        self.oldx = xpos
        self.oldy = ypos

        self.image = None
        self.moveSpeed = None

        self.frameNum = 0
        self.state = "idle"

    def position(self):
        """return object location
        :return: tuple for object location in xy coordinates
        """
        return self.xpos, self.ypos

    def update(self, image):
        self.rect = image.get_rect()


class Character(Object):
    def __init__(self, xpos, ypos, name):
        pg.sprite.Sprite.__init__(self)
        Object.__init__(self, xpos, ypos)

        self.movex = 0
        self.movey = 0

        self.name = name

    def __str__(self):
        return self.name

    def control(self, x, y):
        """control player movement
        :param x: the value by which to move in the x dimension
        :param y: the value by which to move in the y dimension
        :return:
        """
        self.movex += x
        self.movey += y

    def update(self, image):
        """update sprite position
        :return:
        """
        self.oldx = self.xpos
        self.oldy = self.ypos
        self.xpos += self.movex
        self.ypos += self.movey

        self.rect = image.get_rect(topleft=(self.xpos, self.ypos))

    def revert(self, image):
        """move sprite to previous location
        :return:
        """
        self.xpos = self.oldx
        self.ypos = self.oldy

        self.rect = image.get_rect(topleft=(self.xpos, self.ypos))

    def teleport(self, x, y):
        """move sprite to specific location on screen
        :return:
        """
        self.xpos = x
        self.ypos = y


class Player(Character):
    def __init__(self, xpos, ypos, name):
        Character.__init__(self, xpos, ypos, name)

        self.sheet = Spritesheet("characters.png", 23, 4)
        self.moveSpeed = 3
        self.image = self.sheet.image(23)
        self.rect = self.image.get_rect()

    def handleState(self):
        if self.movex == 0 and self.movey == 0:
            self.state = "idle"

        self.frameNum += 0.2

        if self.state == "idle":
            self.image = self.sheet.image(23)

        elif self.state == "walking":
            if int(self.frameNum) >= 3:
                self.frameNum = 0
            self.image = self.sheet.image(int(self.frameNum) + 23)

        if self.frameNum > 46:
            self.frameNum = 46

        self.rect = self.image.get_rect()


class Spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pg.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows

        total = cols * rows
        self.cells = []

        for i in range(total):
            self.cells.append((i % cols * w, int(i / cols) * h, w, h))

        for i in self.cells:
            print(i[0],i[1],i[2],i[3])

    def image(self, cIndex):
        cellIndex = cIndex
        if cellIndex < 0:
            cellIndex = 0
        image = pg.Surface((self.cellWidth,self.cellHeight))
        print(cellIndex)
        image.blit(self.sheet,(0, 0), self.cells[cellIndex])
        image.set_colorkey(settings.BLACK)
        return pg.transform.scale2x(image)
