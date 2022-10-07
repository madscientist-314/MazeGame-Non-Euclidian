import sys
import os
from turtle import speed
import pip
import random as rand
import pygame as pg
from pickle import TRUE
from pygame import QUIT
from tkinter import ON

#init pygame
pg.init()

#set h+w of screen
size = [1280, 720]
screen = pg.display.set_mode(size)

#window name
title = "Non-Euclidian Maze"
pg.display.set_caption(title)

#loop untill close button pressed
clock = pg.time.Clock()
g_ON = True

#player rect size and start pos
rect = pg.Rect(0,0,32,32)
rect.center = (size[0] / 2, size[1] / 2)

playerspeed = 32

while g_ON:
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for ev in pg.event.get():
        if ev.type == QUIT:
            pg.quit()
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_LEFT or ev.key == pg.K_a:
                rect = pg.Rect.move(rect, -playerspeed, 0)
            if ev.key == pg.K_RIGHT or ev.key == pg.K_d:
                rect = pg.Rect.move(rect, playerspeed, 0)
            if ev.key == pg.K_UP or ev.key == pg.K_w:
              rect = pg.Rect.move(rect, 0, -playerspeed)
            if ev.key == pg.K_DOWN or ev.key == pg.K_s:
              rect = pg.Rect.move(rect, 0, playerspeed)
    
    screen.fill((255, 255, 255), rect)
    pg.display.flip()
pg.quit()