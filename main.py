"""
File: main.py
Date: 11 March 2019
Author: Benjamin Parker
Purpose: call in all other relevant files and run the main loop of the project
"""
import pygame as pg
import sys
import os
import math
import time
import lib
from settings import *

# initialize PyGame and all that jazz
from lib import Player, Character, Object

pg.init()
keys = Keys()
winSets = Window()
window = pg.display.set_mode(winSets.DIMENSIONS)
running = True
clock = pg.time.Clock()

gameState = "playing"

sprites = pg.sprite.Group()
objects = pg.sprite.Group()

bgnd = pg.image.load("background.png")
player = Player(300, 300, "Bob")
obj = Player(100, 100, "sprite.png")

objects.add(obj)
sprites.add(player, obj)


def checkQuit(e):
    if e.type == pg.QUIT:
        pg.quit()
        sys.exit()


# main loop
while running:
    window.blit(bgnd, (0, 0))
    if gameState == "playing":
        for event in pg.event.get():
            checkQuit(event)
            if event.type == pg.KEYDOWN:
                if event.key == keys.UP or event.key == keys.W:
                    player.control(0, -player.moveSpeed)
                    player.state = "walking"
                if event.key == keys.DOWN or event.key == keys.S:
                    player.control(0, player.moveSpeed)
                    player.state = "walking"
                if event.key == keys.LEFT or event.key == keys.A:
                    player.control(-player.moveSpeed, 0)
                    player.state = "walking"
                if event.key == keys.RIGHT or event.key == keys.D:
                    player.control(player.moveSpeed, 0)
                    player.state = "walking"
                if event.key == keys.ESC:
                    gameState = "paused"

            if event.type == pg.KEYUP:
                if event.key == keys.UP or event.key == keys.W:
                    player.control(0, player.moveSpeed)
                if event.key == keys.DOWN or event.key == keys.S:
                    player.control(0, -player.moveSpeed)
                if event.key == keys.LEFT or event.key == keys.A:
                    player.control(player.moveSpeed, 0)
                if event.key == keys.RIGHT or event.key == keys.D:
                    player.control(-player.moveSpeed, 0)

        player.handleState()
        player.update(player.image)
        collision = pg.sprite.spritecollide(player, objects, False)
        if collision:
            player.revert(player.image)

        for sprite in sprites:
            window.blit(sprite.image, sprite.position())

    elif gameState == "paused":
        for event in pg.event.get():
            checkQuit(event)
            if event.type == pg.KEYDOWN:
                if event.key == keys.ESC:
                    gameState = "playing"
                    player.state = "idle"

        pScreen = pg.Surface(winSets.DIMENSIONS)
        pScreen.fill(WHITE)
        pScreen.set_alpha(100)

        for sprite in sprites:
            window.blit(sprite.image, sprite.position())
        window.blit(pScreen, (0, 0))

    clock.tick(FPS)
    pg.display.flip()
