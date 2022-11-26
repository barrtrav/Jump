import sys
import pygame

from block import Block
from typing import List
from avatar import Avatar
from time import time
from pygame import Surface
from settings import Settings
from pygame.sprite import Group

def event_keyup_ckeck(event, settings : Settings, screen : Surface, avatar : Avatar):
    if event.key == pygame.K_SPACE:
        avatar.state = 2

def event_keydown_ckeck(event, settings : Settings, screen : Surface, avatar : Avatar):
    if event.key == pygame.K_SPACE and avatar.state != 2:
        avatar.state = 1

def event_check(settings : Settings, screen : Surface, avatar : Avatar):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYUP:
            event_keyup_ckeck(event, settings, screen, avatar)
        elif event.type == pygame.KEYDOWN:
            event_keydown_ckeck(event, settings, screen, avatar)           

def update_screen(settings : Settings, screen : Surface, avatar : Avatar, blocks : Group):
    screen.fill(settings.screen_color)
    
    for block in blocks:
        block.draw_block()
    
    avatar.blitme()
    
    pygame.display.flip()

def update_blocks(settings : Settings, screen : Surface, avatar : Avatar, blocks : Group):
    blocks.update()
    
    blocks_list = blocks.sprites()
    
    if blocks_list[0].rect.right <= 0:
        blocks.remove(blocks_list[0])

    if blocks_list[-1].rect.right <= screen.get_rect().right:
        blocks.add(Block(settings, screen, blocks_list[-1].rect.right + 200, 600 - int(time() % 3) * 200))

    check_avatar_blocks_collisions(settings, screen, avatar, blocks)

def check_avatar_blocks_collisions(settings : Settings, screen : Surface, avatar : Avatar, blocks : Group):
    collision = pygame.sprite.spritecollideany(avatar, blocks)

    if collision:
        if avatar.state == 3: pass
        elif avatar.state == 2 and \
            avatar.rect.bottom >= collision.rect.top and \
            avatar.rect.centerx + 20 >= collision.rect.left and \
            avatar.rect.bottom <= collision.rect.bottom :
                avatar.state = 3
        elif avatar.state == 1 and \
            avatar.rect.top >= collision.rect.top and \
            avatar.rect.centerx + 20 >= collision.rect.left and \
            avatar.rect.top <= collision.rect.bottom :
                avatar.state = 2
        elif (avatar.state == 1 or avatar.state == 2) and \
            avatar.rect.right >= collision.rect.left and \
            avatar.rect.centerx + 20 <= collision.rect.left:
                settings.game_active = False
    elif not collision and avatar.state == 3: 
        avatar.state = 2

def add_initial_blocks(settings : Settings, screen : Surface, avatar : Avatar, blocks : Group):
    blocks.add(Block(settings, screen, avatar.rect.left, avatar.rect.bottom))
    blocks.add(Block(settings, screen, avatar.rect.left + 600, avatar.rect.bottom - 200))
    blocks.add(Block(settings, screen, avatar.rect.left + 1200, avatar.rect.bottom - 400))