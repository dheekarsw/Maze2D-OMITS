import pygame
from settings import *
from support import *
from timer import Timer
import button
from ui import UI
# from level import Level

screen = pygame.display.set_mode((1600,900))
menu_state = "main"
gambar = pygame.image.load('../Awok/Cowo/Idle_CowoBawah2.png').convert_alpha
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
resume_button = button.Button(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, resume_img, 1)
gambarsoal1 = pygame.image.load('../Awok/graphics/soal1.png')
gambarsoal2 = pygame.image.load('../Awok/graphics/soal2.png')
gambarsoal3 = pygame.image.load('../Awok/graphics/soal3.png')
gambarsoal4 = pygame.image.load('../Awok/graphics/soal4.png')
gambarsoal5 = pygame.image.load('../Awok/graphics/soal5.png')

class Player(pygame.sprite.Sprite):
    #setup umum
    def __init__(self, pos, group, collision_sprites, coin_collision_sprites2, pos1_collision_sprites, pos2_collision_sprites,
                  gate_info, interaction):
        super().__init__(group)

        self.import_assets()
        self.status = 'Kanan'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = LAYERS['coin']

        self.display_soal = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT ))
    
    #gerakan
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 600

    #timers
        self.timers = {
        'tool use': Timer(350,self.use_tool)
    }
        
    #tools
        self.selected_tool = 's'
        # self.cewe = True

    #interaction
        self.interaction = interaction

    #tabrakan
        self.hitbox = self.rect.copy().inflate(-16,0)
        self.collision_sprites = collision_sprites
        self.coin_collision_sprites2 = coin_collision_sprites2
        self.coin2 = 0
        # self.kunci_collision_sprites = kunci_collision_sprites
        self.pos1_collision_sprites = pos1_collision_sprites
        self.pos2_collision_sprites = pos2_collision_sprites

        print(self.coin2)

        # if self.coin !=0:
        self.font = pygame.font.Font("assets/font.ttf", 24)
        #     self.coin_index = 1
    

        self.game_paused = False
        self.game_soal1 = False
        self.game_soal2 = False

        self.display_surface = pygame.display.get_surface()

        self.pos1 = False
        self.pos2 = False


        self.ui = UI(screen)

        bool(gate_info)
        self.gate_info = True
        
        self.kebenaran = False

        if self.coin2 == 0:
            print('a')

    def use_tool(self):
        pass
        #print(self.selected_tool)
        
    def import_assets(self):
        self.animations = {'Atas':[],'Bawah':[],'Kanan':[],'Kiri':[],'Bawah_Idle':[],'Atas_Idle':[],'Kanan_Idle':[],'Kiri_Idle':[]}

        for animation in self.animations.keys():
            full_path = '../Awok/Cowo/' + animation
            self.animations[animation] = import_folder(full_path) 

    def animate(self,dt):
        self.frame_index += 9 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['tool use'].active:
            #direction
            if self.game_soal1 == False | self.game_soal2 == False:
                if keys[pygame.K_UP]:
                    self.direction.y = -1
                    self.status = 'Atas'
                elif keys[pygame.K_DOWN]:
                    self.direction.y = 1
                    self.status = 'Bawah'
                else:
                    self.direction.y = 0

                if keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                    self.status = 'Kanan'
                elif keys[pygame.K_LEFT]:
                    self.direction.x = -1
                    self.status = 'Kiri'
                else:
                    self.direction.x = 0

            #tool use
            if keys[pygame.K_b]:
                self.timers['tool use'].activate()
            if keys[pygame.K_c]:
                self.game_paused = True
            if keys[pygame.K_ESCAPE]:
                self.game_paused = False
            if self.pos1 == True:
                if keys[pygame.K_f]:
                    self.game_soal1 = True
                    # print('soal1')
                if keys[pygame.K_ESCAPE]:
                    self.game_soal1 = False
            if self.pos2 == True:
                if keys[pygame.K_f]:
                    self.game_soal2 = True
                    # print('soal1')
                if keys[pygame.K_ESCAPE]:
                    self.game_soal2 = False
            if keys[pygame.K_ESCAPE]:
                    self.game_soal2 = False
                    self.game_soal1 = False
            # self.kebenaran = False
            if keys[pygame.K_RETURN]:
                collided_interaction_sprite = pygame.sprite.spritecollide(self, self.interaction, False)
                
                if collided_interaction_sprite:
                    
                    if collided_interaction_sprite[0].name == 'Trade':
                        pass
                    else:
                        
                        self.status = 'Kiri_Idle'
                        self.kebenaran = True
            
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def draw(self, surface):
        action = False

    def menu(self):
        if self.game_soal1 == True:
            self.display_soal.blit(gambarsoal1, (128, 100))
        elif self.pos1 == False:
            self.game_soal1 = False
        if self.game_soal2 == True:
            self.display_soal.blit(gambarsoal2, (128, 100))
        elif self.pos2 == False:
            self.game_soal2 = False

            # pygame.display.flip()
            # self.display_surface.fill(Color)
            # if menu_state == "main":
            # #draw pause screen buttons
            #     if resume_button.draw(screen):
            #         self.game_paused = False

    def get_status(self):
        #karakter idle
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_Idle'

        #tool use
        if self.timers['tool use'].active:
            print('tool is being used')

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    if direction == 'horizontal':
                        if self.direction.x > 0:
                            self.hitbox.right = sprite.hitbox.left
                        if self.direction.x < 0:
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.pos.x = self.hitbox.centerx
                    
                    if direction == 'vertical':
                        if self.direction.y > 0:
                            self.hitbox.bottom = sprite.hitbox.top
                        if self.direction.y < 0:
                            self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centery = self.hitbox.centery
                        self.pos.y = self.hitbox.centery
    
    def change_coins(self,amount):
        self.coin2 += amount

    def pos1_collision(self):
        for sprite in self.pos1_collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    self.pos1 = True
                    trigger_text = self.font.render('Tekan F untuk membuka soal', True, (255, 255, 255))
                    self.display_surface.blit(trigger_text, ((SCREEN_WIDTH/2)-300, (SCREEN_HEIGHT/2)+300))
                else:
                    self.pos1 = False

    def pos2_collision(self):
        for sprite in self.pos2_collision_sprites.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    self.pos2 = True
                    trigger_text = self.font.render('Tekan F untuk membuka soal', True, (255, 255, 255))
                    self.display_surface.blit(trigger_text, ((SCREEN_WIDTH/2)-300, (SCREEN_HEIGHT/2)+300))
                else:
                    self.pos2 = False


    def coin_collision(self):
        for sprite in self.coin_collision_sprites2.sprites():
            if hasattr(sprite, 'hitbox'):
                if sprite.hitbox.colliderect(self.hitbox):
                    # self.coin += 1
                    sprite.kill()
                    self.change_coins(1)
                    print(self.coin2)

                    

    # def change_gate_info(self, gate_info):
    #     # self.gate_info = gate_info
    #     # gate_info = False
    #     bool(gate_info)
    #     gate_info = False
    #     print(gate_info)

    # def kunci_collision(self):
    #     for sprite in self.kunci_collision_sprites.sprites():
    #         if hasattr(sprite, 'hitbox'):
    #             # self.gate_info = True
    #             if sprite.hitbox.colliderect(self.hitbox):
    #                 sprite.kill()
    #                 # bool(gate_info)
    #                 self.gate_info = False
    #                 # print(gate_info)
    #                 # self.change_gate_info(self.gate_info)
    #                 print('kunci didapatkan')
        
    
    def move(self,dt):

        #normalizing a vector
        if self.direction.magnitude()>0:
            self.direction = self.direction.normalize()
        
        #horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')
        #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')
        #coin
        self.coin_collision()
        
        
    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.ui.show_coins2(self.coin2)
        self.pos1_collision()
        self.pos2_collision()
        # self.kunci_collision()
        # print(self.gate_info)
        # self.change_gate_info(self.gate_info)
        
    
        self.move(dt)
        self.animate(dt)
        self.menu()
        self.gate_info