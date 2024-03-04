import random
from models import (villager_idle_pack, villager_takes_damage_pack, villager_dead_pack, villager_idle_left_pack,
                    villager_takes_damage_left_pack, villager_dead_left_pack, villager_run_right_pack,
                    villager_run_left_pack, villager_attack_right_pack, villager_attack_left_pack,
                    villager_attack_right2_pack, villager_attack_left2_pack)


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
    enemy_sprite_left_border = 40
    enemy_sprite_right_border = 95

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
        if player_x_coordinate - player_current_x >= self.x_coordinate + self.enemy_sprite_right_border:
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
                (abs(player_current_x + self.x_coordinate - player_x_coordinate) <= 200 and
                 self.right_direction and
                 player_y_coordinate - player_current_y >= 615):
            self.under_attack = True
        else:
            pass
