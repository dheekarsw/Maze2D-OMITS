import pygame
from support import *
from settings import *
from pytmx.util_pygame import load_pygame

class Gate:
    def __init__(self, all_sprites, collision_sprites, kunci_collision_sprites):
        self.all_sprites = all_sprites
        self.collision_sprites = collision_sprites
        self.gate_sprites = pygame.sprite.Group()

        self.kunci_collision_sprites = kunci_collision_sprites

    def kunci_collision(self):
        for sprite in self.kunci_collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    sprite.kill()
                    self.gate_info = False
                    print('kunci didapatkan')

    def update(self):
        self.kunci_collision()