import pygame, sys
import random
from settings import *
from player import Player
from overlay import Overlay
from sprites import Generic, Collosion, Coin, Pos, Interaction
from ui import UI
from pytmx.util_pygame import load_pygame
from support import *

# Waktu dlm detik dan ukuran font
TIMER_DURATION = 5400
FONT_SIZE = 24
screen = pygame.display.set_mode((600,300))
BG = pygame.image.load("graphics/background.png")

class Level:
    def __init__(self):
        
        #get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Create a font for the timer
        self.font = pygame.font.Font("assets/font.ttf", FONT_SIZE)
        
        # Initialize timer variables
        self.start_time = pygame.time.get_ticks() 

        self.waktu_menu = pygame.time.get_ticks()
        
        # Get the current time in milliseconds
        self.current_time = 0
        #sprite groups
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.coin_collision_sprites = pygame.sprite.Group()
        # self.kunci_sprites = pygame.sprite.Group()
        # self.kunci_collision_sprites = pygame.sprite.Group()
        self.pos1_sprites = pygame.sprite.Group()
        self.pos1_collision_sprites = pygame.sprite.Group()
        self.pos2_sprites = pygame.sprite.Group()
        self.pos2_collision_sprites = pygame.sprite.Group()
        self.pos3_sprites = pygame.sprite.Group()
        self.pos3_collision_sprites = pygame.sprite.Group()
        self.pos4_sprites = pygame.sprite.Group()
        self.pos4_collision_sprites = pygame.sprite.Group()
        self.pos5_sprites = pygame.sprite.Group()
        self.pos5_collision_sprites = pygame.sprite.Group()
        self.titid2 = pygame.sprite.Group()
        self.interaction_sprites = pygame.sprite.Group()
        self.titid = 0
        self.string = ''
        self.screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
        # self.kebenaran = False

        self.setup()
        # self.setup2()
        self.overlay = Overlay(self.player)
        self.ui = UI(screen)
        # self.player = pygame.sprite.Group()

        # self.gate_info = pygame.sprite.Group()
        
    def time_menu(self, amount):
        self.waktu_menu = int(amount)
        # print(waktu_menu)
    
    def setup(self):
        tmx_data = load_pygame('../Awok/data/Tes2.tmx')
        
        # Collion tiles
        for obj in tmx_data.get_layer_by_name('Tembok'):
            Collosion((obj.x, obj.y), obj.image,  self.collision_sprites)
    
        #pos
        pos1_frames = import_folder('../Awok/graphics/Pos')
        for obj in tmx_data.get_layer_by_name('pos1'):
            self.coin_sprites = Pos((obj.x,obj.y), pos1_frames, [self.all_sprites, self.pos1_collision_sprites])

        pos2_frames = import_folder('../Awok/graphics/Pos')
        for obj in tmx_data.get_layer_by_name('pos2'):
            self.coin_sprites = Pos((obj.x,obj.y), pos2_frames, [self.all_sprites, self.pos2_collision_sprites])

        pos3_frames = import_folder('../Awok/graphics/Pos')
        for obj in tmx_data.get_layer_by_name('pos3'):
            self.coin_sprites = Pos((obj.x,obj.y), pos3_frames, [self.all_sprites, self.pos3_collision_sprites])

        pos4_frames = import_folder('../Awok/graphics/Pos')
        for obj in tmx_data.get_layer_by_name('pos4'):
            self.coin_sprites = Pos((obj.x,obj.y), pos4_frames, [self.all_sprites, self.pos4_collision_sprites])

        pos5_frames = import_folder('../Awok/graphics/Pos')
        for obj in tmx_data.get_layer_by_name('pos5'):
            self.coin_sprites = Pos((obj.x,obj.y), pos5_frames, [self.all_sprites, self.pos5_collision_sprites])

        #coin
        coin_frames = import_folder('../Awok/graphics/Coin')
        for obj in tmx_data.get_layer_by_name('coin'):
            self.coin_sprites = Coin((obj.x,obj.y), coin_frames, [self.all_sprites, self.coin_collision_sprites])
            
     
        #Player
        for obj in tmx_data.get_layer_by_name('Player'):
            if obj.name == 'Start':
                self.player = Player(
                    pos = (obj.x,obj.y),
                    group = self.all_sprites,
                    collision_sprites = self.collision_sprites,
                    coin_collision_sprites = self.coin_collision_sprites,
                    pos1_collision_sprites = self.pos1_collision_sprites,
                    pos2_collision_sprites = self.pos2_collision_sprites,
                    pos3_collision_sprites = self.pos3_collision_sprites,
                    pos4_collision_sprites = self.pos4_collision_sprites,
                    pos5_collision_sprites = self.pos5_collision_sprites,
                    gate_info = True,
                    interaction = self.interaction_sprites)
            if obj.name == 'Finish':
                Interaction((obj.x, obj.y),(obj.width, obj.height), self.interaction_sprites, obj.name)
            
                
                
        Generic(
            pos = (0,0), 
            surf = pygame.image.load('../Awok/World/groundsss.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'])
        # print(self.player.update.coin)

    def finish(self, kebenaran):
        self.player.kebenaran = kebenaran
        # self.kebenaran = kebenaran
        # print(self.player.kebenaran)
        if self.player.kebenaran == True:
            
            # print('tes')
            self.screen.blit(BG, (0, 0))
            self.ui.show_coins(self.player.coin)
            username = self.font.render(self.ayam, True, (255, 255, 255))
            self.display_surface.blit(username, ((SCREEN_WIDTH/2)-600, (SCREEN_HEIGHT/2)+300))
        
    def get_username(self, text):
        self.ikan = text
        self.ayam = 'Nama Peserta Jenjang SD: ' + text

    def run(self,dt):
        self.display_surface.fill('black')
      
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
       
        self.overlay.display()
        
        # Calculate the elapsed time
        self.current_time = pygame.time.get_ticks() - self.start_time 

        # Calculate the remaining time
        remaining_time = max(TIMER_DURATION + self.waktu_menu - self.current_time  // 1000, 0)
        
        # Calculate the remaining time in minutes and seconds
        remaining_minutes = remaining_time // 60
        remaining_seconds = remaining_time % 60
        
        # Create a text surface for the timer
        timer_text = self.font.render(f'Time Left:  {remaining_minutes:02}:{remaining_seconds:02}', True, (255, 255, 255))


        # Blit the timer text onto the screen
        self.display_surface.blit(timer_text, (750, 10))

        # Check if the timer has reached zero
        self.finish(self.player.kebenaran)

        if remaining_time == 0:
            self.screen.blit(BG, (0, 0))
            self.ui.show_coins(self.player.coin)
            username = self.font.render(self.ayam, True, (255, 255, 255))
            self.display_surface.blit(username, ((SCREEN_WIDTH/2)-600, (SCREEN_HEIGHT/2)+300))
            
    


    def tes(self,amount):
        # tmx_data = load_pygame('../Awok/data/Tes2.tmx')
        if amount == 0:
            # for obj in tmx_data.get_layer_by_name('gate'):
            #         Collosion((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])
            #         # print(self.player.gate_info)
            pass
        else:
            pass

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        # self.zoom_scale = 10

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
