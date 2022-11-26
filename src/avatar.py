import pygame

from typing import List
from settings import Settings
from pygame import Surface, Rect

class Avatar:
    def __init__(self, settings : Settings, screen : Surface) -> None:
        
        self.state = 3
        self.steps = 0

        self.screen : Surface = screen
        self.settings : Settings = settings
        self.screen_ret : Rect = screen.get_rect()

        self.load_image()
        self.update_image()
        
        self.y = float(self.rect.y)

    def blitme(self):
        self.update_image()
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.state == 1:
            if self.rect.top <= 0: self.state = 2
            self.y -= self.settings.avatar_jump_speed
        if self.state == 2:
            self.y += self.settings.avatar_jump_speed

        if self.rect.bottom >= self.screen_ret.bottom:
            self.settings.game_active = False

    def update_image(self):
        if self.state == 0:
            self.image : Surface = self.img_run[0]
        elif self.state == 1:
            self.image : Surface = self.img_jump_up
        elif self.state == 2:
            self.image : Surface = self.img_jump_down
        else:
            if self.steps > (len(self.img_run) * self.settings.avatar_speed - 1): self.steps = 0
            self.image : Surface = self.img_run[self.steps // self.settings.avatar_speed]
            self.steps += 1

        self.rect  : Rect = self.image.get_rect()
        self.rect.x = 100
        try: self.rect.y = self.y
        except AttributeError: self.rect.y = 476

    def load_image(self):
        self.img_run : List[Surface] = [
            pygame.image.load("../images/run_1.bmp"),
            pygame.image.load("../images/run_2.bmp"),
            pygame.image.load("../images/run_3.bmp"),
            pygame.image.load("../images/run_4.bmp"),
            pygame.image.load("../images/run_5.bmp"),
            pygame.image.load("../images/run_6.bmp"),
        ]
        self.img_jump_up : Surface = pygame.image.load("../images/jump_up.bmp")
        self.img_jump_down : Surface = pygame.image.load("../images/jump_down.bmp")