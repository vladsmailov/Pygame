import pygame
import random
from enemy import Enemy


class Game:
    """Configuration class for game object."""
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((928, 793))
    enemy_counter = 0
    dead_enemy_counter = 0
    players_area = 1
    running = True
    game_font = pygame.font.Font('Fonts/Sixtyfour.ttf', 40)
    enemies = []

    def set_tick(self, quantity):
        """Method for definition of tick (delay) in game process."""
        return self.clock.tick(quantity)

    @staticmethod
    def game_update():
        """Update method."""
        return pygame.display.update()

    @staticmethod
    def quit():
        """Game session ending."""
        return pygame.quit()

    def show_players_hp(self, hp):
        players_hp = self.game_font.render(hp, True, 'Black')
        self.screen.blit(players_hp, (20, 20))

    def check_players_area(self, player_current_x):
        if player_current_x >= -1000:
            self.players_area = 1
        elif -1000 >= player_current_x >= -2000:
            self.players_area = 2

    def generate_enemy(self, background, player_current_x, enemies_x, enemies_y):
        self.enemy_counter += 1
        enemy = Enemy(10, 0, enemies_x, enemies_y)
        self.enemies.append(enemy)
        enemy.current_x = player_current_x
        enemy.idle_enemy(background, player_current_x)
        return enemy
