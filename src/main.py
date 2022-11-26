import pygame
import funtions as ft

from block import Block
from avatar import Avatar
from settings import Settings
from pygame.sprite import Group

def run_game():
    
    pygame.init()
    settings = Settings()
    pygame.display.set_caption(settings.screen_caption)
    screen = pygame.display.set_mode(settings.screen_size)

    avatar = Avatar(settings, screen)
    
    blocks = Group()
    ft.add_initial_blocks(settings, screen, avatar, blocks)

    while True:
        ft.event_check(settings, screen, avatar)
        
        if settings.game_active:
            avatar.update()
            ft.update_blocks(settings, screen, avatar, blocks)
        
        ft.update_screen(settings, screen, avatar, blocks)

if __name__ == "__main__":
    run_game()