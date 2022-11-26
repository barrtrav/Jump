import pygame

from pygame.sprite import Sprite

from pygame import Surface
from settings import Settings

class Block(Sprite):
    def __init__(self, settings : Settings, screen : Surface, xpos : int, ypos : int) -> None:
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(xpos, ypos, settings.block_width, settings.block_height)
        self.x = float(self.rect.x)

    def draw_block(self):
        pygame.draw.rect(self.screen, self.settings.block_color, self.rect)

    def update(self):
        self.x -= self.settings.block_speed
        self.rect.x = self.x
