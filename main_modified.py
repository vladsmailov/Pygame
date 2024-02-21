import random
import pygame
from models import (
    all_in_one,
    forrest_background, mushroom_right_pack,
    mushroom_left_pack, mushroom_attack_right_pack, villager_stop,
    mushroom_fire_pack, mushroom_attack_left_pack, villager_idle_pack,
    villager_takes_damage_pack, villager_dead_pack, villager_idle_left_pack,
    villager_takes_damage_left_pack, villager_dead_left_pack, villager_run_right_pack,
    villager_run_left_pack, villager_attack_right_pack, villager_attack_left_pack,
    villager_attack_right2_pack, villager_attack_left2_pack,
)


class Game:
    """Configuration class for game object."""
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((928, 793))
    enemy_counter = 0
    running = True

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


class Background:
    def __init__(self, screen):
        self.screen = screen

    def show(self, x_coordinate=0):
        """Method for creating background layer."""
        self.screen.blit(all_in_one, (x_coordinate, 0))
        return


class Player:
    """Configuration class for player."""
    right_direction = True
    jump = False
    attack = False
    move = False
    launch = False
    x_coordinate = 400
    y_coordinate = 690
    current_x = 0
    current_y = 0
    player_animation_count = 0
    height_count = 0
    attack_animation_count = 0

    def idle_player(self, background):
        if self.right_direction:
            return background.blit(mushroom_right_pack[0], (self.x_coordinate, self.y_coordinate - self.current_y))
        else:
            return background.blit(mushroom_left_pack[0], (self.x_coordinate, self.y_coordinate - self.current_y))

    def move_player(self, button, background):
        """Players move method."""
        if self.attack:
            return
        if self.player_animation_count == 4:
            self.player_animation_count = 0
        if button == "left":
            self.right_direction = False
            self.move = True
            background.blit(mushroom_left_pack[self.player_animation_count], (self.x_coordinate, self.y_coordinate - self.current_y))
            self.player_animation_count += 1
            self.current_x += 8
        elif button == "right":
            self.right_direction = True
            self.move = True
            background.blit(mushroom_right_pack[self.player_animation_count], (self.x_coordinate, self.y_coordinate - self.current_y))
            self.player_animation_count += 1
            self.current_x -= 8
        return

    def jump_player(self, background):
        if self.right_direction:
            direction = mushroom_right_pack
        else:
            direction = mushroom_left_pack
        if self.height_count <= 7:
            if self.attack:
                self.height_count += 1
                self.current_y += 15
            else:
                self.height_count += 1
                self.current_y += 15
                background.blit(direction[0], (400, 690 - self.current_y))
        elif 7 < self.height_count <= 14:
            if self.attack:
                self.height_count += 1
                self.current_y -= 15
            else:
                self.height_count += 1
                self.current_y -= 15
                background.blit(direction[0], (400, 690 - self.current_y))
        else:
            self.jump = False
            self.height_count = 0
            self.current_y = 0

    def attack_player(self, background):
        if player.right_direction:
            direction = mushroom_attack_right_pack
        else:
            direction = mushroom_attack_left_pack
        if player.attack_animation_count <= 8:
            background.blit(direction[self.attack_animation_count],
                            (388, 675 - self.current_y))
            self.attack_animation_count += 1
        else:
            background.blit(direction[self.attack_animation_count],
                            (388, 675 - self.current_y))
            self.attack_animation_count = 0
            self.attack = False
            self.launch = True


class Fireball:
    fireball_x = 0
    fireball_y = 0
    fireball_current_x = 0
    fireball_current_y = 0
    fireball_animation = True
    fire_animation_count = 0

    def __init__(self, fire_x, fire_y, right_direction):
        self.fire_x = fire_x
        self.fire_y = fire_y
        self.right_direction = right_direction

    def fire(self, background):
        if self.fire_animation_count <= 7:
            self.fireball_current_x = 400 + self.fireball_x
            background.blit(mushroom_fire_pack[self.fire_animation_count], (400 + self.fireball_x, 690 - self.fire_y))
            self.fire_animation_count += 1
            if self.right_direction:
                self.fireball_x += 50
            else:
                self.fireball_x -= 50
            return
        else:
            self.fireball_x = 0
            self.fire_x = 0
            self.fire_animation_count = 0
            self.fireball_animation = False
            return


class Enemy:

    dead = False
    under_attack = False
    right_direction = False
    run = False
    attack = False
    take_hit = False
    current_y = 0
    current_x = 0
    idle_animation_count = 0
    takes_damage_animation = 0
    death_animation_count = 0
    run_animation_count = 0
    attack_animation_count = 0
    enemy_sprite_left_border = 43
    enemy_sprite_right_border = 93

    def __init__(self, hp, power, x_coordinate, y_coordinate, mp=0):
        self.hp = hp
        self.mp = mp
        self.power = power
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def idle_enemy(self, background, player_current_x):
        self.current_x = player_current_x
        if self.right_direction:
            direction = villager_idle_pack
        else:
            direction = villager_idle_left_pack
        if self.idle_animation_count < 7:
            background.blit(direction[self.idle_animation_count],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
            self.idle_animation_count += 1
        else:
            background.blit(direction[self.idle_animation_count],
                        (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
            self.idle_animation_count = 0

    def take_damage(self, background):
        if self.right_direction:
            direction = villager_takes_damage_pack
            idle_direction = villager_idle_pack
        else:
            direction = villager_takes_damage_left_pack
            idle_direction = villager_idle_left_pack
        if self.takes_damage_animation < 3:
            self.takes_damage_animation += 1
            background.blit(direction[self.takes_damage_animation],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
        else:
            self.takes_damage_animation = 0
            self.hp -= 10
            if self.hp <= 0:
                self.dead = True
            self.under_attack = True
            self.take_hit = False
            background.blit(idle_direction[0],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
        return

    def death(self, background, player_current_x):
        self.under_attack = False
        if self.right_direction:
            direction = villager_dead_pack
        else:
            direction = villager_dead_left_pack
        self.current_x = player_current_x
        if self.death_animation_count < 5:
            self.death_animation_count += 1
            background.blit(direction[self.death_animation_count],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
        else:
            background.blit(direction[self.death_animation_count],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y))
            return

    def enemy_run(self, background, player_current_x, player_x_coordinate, player_current_y, player_y_coordinate):
        if player_x_coordinate - player_current_x >= self.x_coordinate + 90:
            self.right_direction = True
        elif player_x_coordinate - player_current_x <= self.x_coordinate:
            self.right_direction = False
        if self.right_direction:
            direction = villager_run_right_pack
        else:
            direction = villager_run_left_pack
        self.current_x = player_current_x
        if (abs(player_current_x + self.x_coordinate - player_x_coordinate) >= 10 and
            not self.right_direction and
                player_y_coordinate - player_current_y >= 615) or\
                (abs(player_current_x + self.x_coordinate - player_x_coordinate) >= 150 and
                    self.right_direction and
                 player_y_coordinate - player_current_y >= 615):
            if self.run_animation_count < 7:
                background.blit(direction[self.run_animation_count],
                                (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y)
                                )
                self.run_animation_count += 1
                if self.right_direction:
                    self.x_coordinate += 10
                else:
                    self.x_coordinate -= 10
            else:
                background.blit(direction[self.run_animation_count],
                                (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y)
                                )
                self.run_animation_count = 0
        elif player_y_coordinate - player_current_y <= 615:
            self.run = False
            self.under_attack = False
            self.run_animation_count = 0
        else:
            self.run = False
            self.attack = True
            self.run_animation_count = 0

    def enemy_attack(self, background, player_current_x):
        attack_style = random.randint(0, 1)
        if self.right_direction:
            if attack_style == 0:
                direction = villager_attack_right_pack
            else:
                direction = villager_attack_right2_pack
        else:
            if attack_style == 0:
                direction = villager_attack_left_pack
            else:
                direction = villager_attack_left2_pack
        self.current_x = player_current_x
        if self.attack_animation_count < 3:
            background.blit(direction[self.attack_animation_count],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y)
                            )
            self.attack_animation_count += 1
        else:
            background.blit(direction[self.attack_animation_count],
                            (self.x_coordinate + self.current_x, self.y_coordinate - self.current_y)
                            )
            self.attack_animation_count = 0
            self.attack = False

    def check_opponent(self, player_current_x, player_x_coordinate, player_current_y, player_y_coordinate):
        if player_x_coordinate - player_current_x >= self.x_coordinate + 90:
            self.right_direction = True
        elif player_x_coordinate - player_current_x <= self.x_coordinate:
            self.right_direction = False
        self.current_x = player_current_x
        if (abs(player_current_x + self.x_coordinate - player_x_coordinate) <= 300 and
            not self.right_direction and
            player_y_coordinate - player_current_y >= 615) or \
                (abs(player_current_x + self.x_coordinate - player_x_coordinate) <= 300 and
                 self.right_direction and
                 player_y_coordinate - player_current_y >= 615):
            self.under_attack = True
        else:
            pass

if __name__ == '__main__':
    player = Player()
    game = Game()
    fireball = None
    pygame.init()
    background = Background(game.screen)
    running = True
    enemy = None
    while game.running:
        game.set_tick(quantity=15)
        game.game_update()
        keys = pygame.key.get_pressed()
        background.show(player.current_x)
        if player.x_coordinate in range(928) and game.enemy_counter == 0:
            game.enemy_counter += 1
            enemy = Enemy(30, 0, random.randint(500, 928), 590)
            enemy.current_x = player.current_x
            enemy.idle_enemy(background.screen, player.current_x)
        if enemy and not enemy.under_attack and not enemy.dead and not enemy.run and not enemy.attack:
            enemy.idle_enemy(background.screen, player.current_x)
            enemy.check_opponent(background.screen, player.current_x, player.x_coordinate, player.current_y, player.y_coordinate)
        if enemy.attack and not enemy.dead and not enemy.take_hit:
            enemy.enemy_attack(background.screen, player.current_x)
        if enemy and enemy.under_attack and not enemy.attack and not enemy.take_hit:
            enemy.run = True
            enemy.enemy_run(background.screen, player.current_x, player.x_coordinate, player.current_y, player.y_coordinate)
        if enemy.dead:
            enemy.death(background.screen, player.current_x)
        if not player.jump:
            if keys[pygame.K_UP]:
                player.jump = True
                player.idle_player(background.screen)
        elif player.jump:
            player.jump_player(background.screen)
        if keys[pygame.K_RIGHT]:
            player.move_player("right", background.screen)
        elif keys[pygame.K_LEFT]:
            player.move_player("left", background.screen)
        else:
            player.move = False
        if not player.attack:
            if keys[pygame.K_SPACE]:
                player.attack = True
                player.idle_player(background.screen)
        elif player.attack:
            player.attack_player(background.screen)
            if player.launch:
                fireball = Fireball(player.current_x, player.current_y, player.right_direction)
                player.launch = False
        if fireball and fireball.fireball_animation:
            fireball.fire(background.screen)
            if (fireball.fireball_current_x - player.current_x) in range(
                    enemy.x_coordinate + enemy.enemy_sprite_left_border,
                    enemy.x_coordinate + enemy.enemy_sprite_right_border
            ) and not enemy.dead:
                fireball = None
                enemy.under_attack = True
                enemy.take_hit = True
        if enemy.under_attack and not enemy.dead and enemy.take_hit:
            enemy.take_damage(background.screen)
        if not player.move and not player.attack and not player.jump:
            player.idle_player(background.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.quit()
