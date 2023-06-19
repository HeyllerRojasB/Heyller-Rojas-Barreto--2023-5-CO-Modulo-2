from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        
    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
                
    def add_enemy(self):
        if len(self.enemies) < 1:
            enemy = Enemy()
            enemy.swap_enemy_type()
            self.enemies.append(enemy)
            
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
        
    def reset(self):
        self.enemies = []
        
    
            