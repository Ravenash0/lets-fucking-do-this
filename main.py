import pygame
import sys
from setting import *
from level_tile import Tile
#the road to the end
pygame.init()


Screen=pygame.display.set_mode((screen_X,screen_Y))
clock=pygame.time.Clock()
placeholder_tile=pygame.sprite.Group(Tile((100,100),200))
#game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit
      sys.exit
  Screen.fill("grey")
  placeholder_tile.draw(Screen)
  pygame.display.update
  clock.tick(60)