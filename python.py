from email.mime import image
from json import load
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
#must change rect size as well - L 27
tilesize = 32 * 32
gmt = True

empty = pg.image.load('white.png')
wall = pg.image.load('black.png')       
goal = pg.image.load('green.jpg')
clock.tick(60)
screen.fill((0, 0, 0))

while g_ON:
    #tutorial level
    if gmt == True:
        #width and hight of maze
        mw = 8 * tilesize
        mh = 8 * tilesize
        
        mazetut = [
            [1,1,1,1,1,1,1,1], #1
            [1,0,0,0,1,2,0,1], #2
            [1,0,1,0,1,1,0,1], #3
            [1,0,1,0,0,0,0,1], #4
            [1,0,1,0,1,1,0,1], #5 
            [1,0,1,0,1,0,0,1], #6
            [1,1,0,0,0,0,1,1], #7
            [1,1,1,1,1,1,1,1], #8
            ]
        for row in range(len(mazetut)):
            for column in range(len(mazetut[row])):
                x = column * tilesize
                y = row * tilesize
                if mazetut[row][column] == 1:
                    screen.blit(wall, (x,y))
                elif mazetut[row][column] == 2:
                    screen.blit(goal, (x,y))
                elif mazetut[row][column] == 0:
                    screen.blit(empty, (x,y))
    
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
              
        if mazetut[row][column] == 0:
            rect.x = column * tilesize
            rect.y = row * tilesize
        elif mazetut[row][column] == 2:
            print("Well done")
            
    screen.fill((255, 255, 255), rect)
    pg.display.flip()
pg.quit()