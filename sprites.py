import pygame
from settings import *
from settings import LAYERS

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -0)

class Coin(Generic):
    def __init__(self, pos, frames, groups):
        #animation setup
        self.frames = frames
        self.frame_index = 0
        # center_x = x + int(size / 2)
        # center_y = y + int(size / 2)
        # self.rect = self.image.get_rect(center = (center_x,center_y))

        # sprite setup
        super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['coin']) 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -0)
        # self.apple_sprites = pygame.sprite.Group()
    
    def animate(self,dt):
        self.frame_index += 7 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        
    def update(self,dt):
        self.animate(dt)

class Kunci(Generic):
    def __init__(self, pos, frames, groups):
        #animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['coin']) 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -0)
        # self.apple_sprites = pygame.sprite.Group()
    
    def animate(self,dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        
    def update(self,dt):
        self.animate(dt)

class Pos(Generic):
    def __init__(self, pos, frames, groups):
        #animation setup
        self.frames = frames
        self.frame_index = 0

        # sprite setup
        super().__init__(
				pos = pos, 
				surf = self.frames[self.frame_index], 
				groups = groups, 
				z = LAYERS['coin']) 
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.5, -0)
        # self.apple_sprites = pygame.sprite.Group()
    
    def animate(self,dt):
        self.frame_index += 8 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        
    def update(self,dt):
        self.animate(dt)

class Interaction(Generic):
    def __init__(self, pos, size, groups, name):
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.name = name

class Collosion(Generic):
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()
        # .inflate(-30,-self.rect.height * 0.9)