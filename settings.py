import os
import pygame
from pygame.math import Vector2
# screen

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
# SCREEN_WIDTH = 1280
# SCREEN_HEIGHT = 720
TILE_SIZE = 64
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255,255,255)
Color = (102, 57, 49)

# overlay positions
OVERLAY_POSITIONS = {
    'tool' : (SCREEN_WIDTH - 50, SCREEN_HEIGHT - SCREEN_HEIGHT + 130),
    'seed' : (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
    'left' : Vector2(-50,40),
    'right': Vector2(50,40),
    'up': Vector2(0,-10),
    'down': Vector2(0,50)}

LAYERS = {
    'tembok': 0,
    'ground': 1,
    'karakter': 2,
    'main': 3,
    'coin': 4,
}