import pygame
from settings import *

class Overlay:
    def __init__(self,player):
        
        #general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player

        #imports
        #overlay_path = '../graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load('../Awok/graphics/overlay/soal.png').convert_alpha() for tool in player.selected_tool}
        
    def display(self):
        pass
        # tool_surf = self.tools_surf[self.player.selected_tool]
        # tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        # self.display_surface.blit(tool_surf,[0,0])
        