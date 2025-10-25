import pygame, sys
from settings import *
from level import Level
from button2 import Button

BG = pygame.image.load("assets/Background.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


class Game:
    def __init__(self):
        pygame.init()
        # self.screen = pygame .display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.screen = pygame.display.set_mode((SCREEN_WIDTH ,SCREEN_HEIGHT))
        # self.screen = pygame .display.set_mode((SCREEN_WIDTH -80 ,SCREEN_HEIGHT - 130),pygame.RESIZABLE)
        pygame.display.set_caption('OMITS 16')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.user_text = ''
        self.input_rect = pygame.Rect((SCREEN_WIDTH/2)-500, (SCREEN_HEIGHT/2)-150,1000,48)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')
        self.color = self.color_passive
        self.waktu = 0


    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass

            dt = self.clock.tick() / 1000
            self.level.run(dt)
            pygame.display.update()

    def main_menu(self):
        active = False
        while True:
            self.waktu = pygame.time.get_ticks()/1000
            self.level.time_menu(self.waktu)

            self.screen.blit(BG, (0, 0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-300))

            KETERANGAN_TEXT = get_font(50).render("NAMA :", True, "#b68f40")
            KETERANGAN_RECT = KETERANGAN_TEXT.get_rect(center=(SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)-188))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)
            self.screen.blit(KETERANGAN_TEXT, KETERANGAN_RECT)

            for button in [PLAY_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            self.user_text += event.unicode


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.run()

            if active:
                self.color = self.color_active
            else:
                self.color = self.color_passive

            pygame.draw.rect(self.screen, self.color, self.input_rect, 2)

            text_surface = get_font(32).render(self.user_text, True, (255,255,255))
            self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))

            self.input_rect.w = max(1000, text_surface.get_width()+10)

            self.level.get_username(self.user_text)

            pygame.display.update()
    

if __name__ == '__main__':
    game = Game()
    game.main_menu()
    game.run()