from pickle import TRUE
import sys
from tkinter import ON
import pip
import pygame
from pygame import QUIT

pygame.init()
surface = pygame.display.set_mode((1080, 1080))
clock = pygame.time.Clock()
surfrect = surface.get_rect()
rect = pygame.Rect((0, 0), (128, 128))
rect.center = (surfrect.w / 2, surfrect.h / 2)
touched = False
g_ON = True
while g_ON == True:
  for ev in pygame.event.get():
    if ev.type == QUIT:
      pygame.quit()
    elif ev.type == pygame.MOUSEBUTTONDOWN:
      if rect.collidepoint(ev.pos):
        touched = True
        pygame.mouse.get_rel()
    elif ev.type == pygame.MOUSEBUTTONUP:
      touched = False
  clock.tick(60)
  surface.fill((0, 0, 0))
  if touched:
    rect.move_ip(pygame.mouse.get_rel())
    rect.clamp_ip(surfrect)
  surface.fill((255, 255, 255), rect)
  pygame.display.flip()
    