import pygame as pg

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

FPS = 60


class Keys:
    def __init__(self):
        self.UP = pg.K_UP
        self.DOWN = pg.K_DOWN
        self.LEFT = pg.K_LEFT
        self.RIGHT = pg.K_RIGHT
        self.W = pg.K_w
        self.A = pg.K_a
        self.S = pg.K_s
        self.D = pg.K_d
        self.P = pg.K_p
        self.ESC = pg.K_ESCAPE


class Window:
    def __init__(self):
        self.HEIGHT = 600
        self.WIDTH = 800
        self.DIMENSIONS = (800, 600)
