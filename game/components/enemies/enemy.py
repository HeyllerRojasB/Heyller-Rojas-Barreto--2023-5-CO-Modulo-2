import os
import pygame
import random

from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HIGHT = 60
    X_POS_LIST = list(range(50, 1050, 50))
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 2
    MOV_X = { 0 : 'left', 1: 'right' }
    
    def __init__(self):
        self.enemy_type = random.choice([ENEMY_1, ENEMY_2])
        self.image = pygame.transform.scale(self.enemy_type, (self.ENEMY_WIDTH, self.ENEMY_HIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y= self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)
        sound_dir = os.path.join('game', 'sound')
        sound_file = os.path.join(sound_dir, '11549.mp3')
        self.shoot_sound = pygame.mixer.Sound(sound_file)
        self.shoot_sound.set_volume(0.1)
        
    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)
        
        
        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
            
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10): 
            self.movement_x = 'right'
            self.index = 0
            
    def swap_enemy_type(self):   
        if self.enemy_type == ENEMY_1:
            self.enemy_type = ENEMY_2
            self.speed_x = self.SPEED_X * 2
        elif self.enemy_type == ENEMY_2:
            self.enemy_type = ENEMY_1
            self.speed_x = self.SPEED_X
        self.image = pygame.transform.scale(self.enemy_type, (self.ENEMY_WIDTH, self.ENEMY_HIGHT))

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if current_time >= self.shooting_time:
            self.shoot_sound.play()
            bullet = Bullet(self, 'enemy')
            bullet_manager.add_bullet(bullet)
            self.shooting_time = current_time + random.randint(500, 900)
