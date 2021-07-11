import pygame
import sys # to exit using sys.exit
import pygame.locals import *
# basic pygame imports


#global variables for the game
FPS = 32   #frame per second
SCREENWIDTH =289
SCREENHEIGHT =511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * SCREENWIDTH
GAME_SPRITE = {}
GAME_SOUND