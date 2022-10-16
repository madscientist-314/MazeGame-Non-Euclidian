# Geoheart  Copyright(C) 2022  Thomas Kirby

import sys
import os
import pip
import random
import thorpy
import pygame as pg
from pygame import QUIT

# init pygame
pg.init()
pg.key.set_repeat(300, 30)

# set h+w of screen
size = [1280, 720]
screen = pg.display.set_mode(size)

# window name
title = "Non-Euclidian Maze"
pg.display.set_caption(title)

# loop untill close button pressed
clock = pg.time.Clock()
g_ON = True

# define a font
smallFont = pg.font.SysFont('Corbel', 35)
quitText = smallFont.render('quit', True, (0, 0, 0))

# player rect size and start pos
rect = pg.Rect(0, 0, 32, 32)
rect.center = (size[0] / 2, size[1] / 2)

playerspeed = 32
# must change rect size as well - L 27
tilesize = 32
gmt = True

empty = pg.image.load('white.png')
wall = pg.image.load('black.png')
goal = pg.image.load('green.jpg')
clock.tick(60)
screen.fill((255, 255, 255))


def collide(rect):
    if rect.collidepoint(x, y):
        return True

# startup screen
application = thorpy.Application(size=(1280, 720))

#setting the graphical theme.
thorpy.set_theme('windows10')

##Declaration of some elements...
Tutorial = thorpy.make_button("Tutorial")
Tutorial.scale_to_content()
button = thorpy.make_button("Quit")
box = thorpy.Box(elements=[Tutorial,button])
#we regroup all elements on a menu, even if we do not launch the menu
menu = thorpy.Menu(box)
for element in menu.get_population():
    element.surface = screen
#use the elements normally...
thorpy.Background.make((255,255,255), elements=[box, button, Tutorial])
box.set_topleft((100,100))
box.blit()
box.update()

# tutorial level
if gmt == True:
    # width and hight of maze
    mw = 8 * tilesize
    mh = 8 * tilesize
    x_offset = size[0] / 2 - 144
    y_offset = size[1] / 2 - 144
    mazetut = [
        [1, 1, 1, 1, 1, 1, 1, 1],  # 1
        [1, 0, 0, 0, 1, 1, 2, 1],  # 2
        [1, 0, 1, 0, 1, 0, 0, 1],  # 3
        [1, 0, 1, 0, 1, 0, 1, 1],  # 4
        [1, 0, 1, 0, 1, 0, 0, 1],  # 5
        [1, 0, 1, 0, 1, 1, 0, 1],  # 6
        [1, 0, 1, 0, 0, 0, 0, 1],  # 7
        [1, 1, 1, 1, 1, 1, 1, 1],  # 8
    ]
    for row in range(len(mazetut)):
        for column in range(len(mazetut[row])):
            x = column * tilesize + x_offset
            y = row * tilesize + y_offset
            if mazetut[row][column] == 1:
                screen.blit(wall, (x, y))
            elif mazetut[row][column] == 2:
                 screen.blit(goal, (x, y))
            elif mazetut[row][column] == 0:
                screen.blit(empty, (x, y))

while g_ON:
    for ev in pg.event.get():
        if ev.type == QUIT:
            g_ON = False
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_LEFT or ev.key == pg.K_a:
                rect = pg.Rect.move(rect, -playerspeed, 0)
            if ev.key == pg.K_RIGHT or ev.key == pg.K_d:
                rect = pg.Rect.move(rect, playerspeed, 0)
            if ev.key == pg.K_UP or ev.key == pg.K_w:
                rect = pg.Rect.move(rect, 0, -playerspeed)
            if ev.key == pg.K_DOWN or ev.key == pg.K_s:
                rect = pg.Rect.move(rect, 0, playerspeed)
            if ev.key == pg.K_ESCAPE:
                g_ON = False

    screen.fill((255, 172, 0), rect)
    pg.display.update()
    menu.react(ev)
    
pg.quit()

'''
import pygame 
import sys 

# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update()

import thorpy

##Declaration of the application in which the menu is going to live.
application = thorpy.Application(size=(500, 500))

##Setting the graphical theme. By default, it is 'classic' (windows98-like).
###thorpy.theme.set_theme('human')

##Declaration of some elements...
useless1 = thorpy.Element("This button is useless.\nAnd you can't click it.")
useless1.set_pressed_state() #so user knows he can't click
useless1.scale_to_content()

text = "This button also is useless.\nBut you can click it anyway."
useless2 = thorpy.make_button(text)

draggable = thorpy.Draggable("Drag me!")
draggable.scale_to_content()

box1 = thorpy.make_ok_box([useless1, useless2, draggable])
options1 = thorpy.make_button("Some useless things...")
thorpy.set_launcher(options1, box1)


inserter = thorpy.Inserter(name="Tip text: ",
                            value="This is a default text.",
                            size=(150, 20))

file_browser = thorpy.Browser(path="C:/Users/", text="Please have a look.")

browser_launcher = thorpy.BrowserLauncher(browser=file_browser,
                                                const_text="Choose a file: ",
                                                var_text="")
browser_launcher.scale_to_title()

color_setter = thorpy.ColorSetter.make()
color_launcher = thorpy.ColorSetterLauncher(color_setter,
                                                    "Launch color setter")

options2 = thorpy.make_button("Useful things")
box2 = thorpy.make_ok_box([inserter, color_launcher, browser_launcher])
thorpy.set_launcher(options2, box2)

quit_button = thorpy.make_button("Quit")
quit_button.set_as_exiter()

central_box = thorpy.Box.make([options1, options2, quit_button])
central_box.set_main_color((200, 200, 200, 120))
central_box.center()

##Declaration of a background element - include your own path!
background = thorpy.Background(image=thorpy.style.EXAMPLE_IMG,
                                    elements=[central_box])

menu = thorpy.Menu(elements=background, fps=45)
menu.play()

application.quit()
'''
