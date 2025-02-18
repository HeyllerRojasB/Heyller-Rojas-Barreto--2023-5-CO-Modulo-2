import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.Speed import SpeedUp
from game.utils.constants import SPACESHIP_SHIELD


class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000
    
    def __init__(self):
        self.power_ups = []
        self.when_appeats = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.duracion = random.randint(3, 5)
    
    def generate_power_up(self):
        shield = Shield()
        shield.when_appears = pygame.time.get_ticks() + random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(shield)
    
        speed_up = SpeedUp()
        speed_up.when_appears = pygame.time.get_ticks() + random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.power_ups.append(speed_up)
        
    def update(self, game):
        current_time = pygame.time.get_ticks()
        
        if len (self.power_ups) == 0 and current_time >= self.when_appeats:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.start_time + (self.duracion * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
                
        
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    
    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appeats = random.randint(now + self.MIN_TIME_POWER_UP, now + self.MAX_TIME_POWER_UP)