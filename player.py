import datetime
from models import (mushroom_right_pack, mushroom_left_pack, mushroom_attack_right_pack, mushroom_attack_left_pack,
                    mushroom_death_pack, mushroom_dodge_right_pack, mushroom_dodge_left_pack)


class Player:
    """Configuration class for player."""
    right_direction = True
    jump = False
    attack = False
    move = False
    launch = False
    take_damage = False
    dead = False
    dodge = False
    blocked = False
    x_coordinate = 400
    y_coordinate = 690
    current_x = 0
    current_y = 0
    player_animation_count = 0
    height_count = 0
    attack_animation_count = 0
    take_damage_count = 0
    death_animation_count = 0
    dodge_animation_count = 0
    dodge_up_animation_count = 4
    player_hp = 100
    dodge_cooldown = datetime.timedelta(seconds=2)
    dodge_last_use = datetime.datetime.now()
    dodge_underground_time = datetime.timedelta(seconds=2)
    dodge_underground_start_time = datetime.datetime.now()

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
            background.blit(mushroom_left_pack[self.player_animation_count],
                            (self.x_coordinate, self.y_coordinate - self.current_y)
                            )
            self.player_animation_count += 1
            self.current_x += 11
        elif button == "right":
            self.right_direction = True
            self.move = True
            background.blit(mushroom_right_pack[self.player_animation_count],
                            (self.x_coordinate, self.y_coordinate - self.current_y)
                            )
            self.player_animation_count += 1
            self.current_x -= 11
        return

    def jump_player(self, background):
        if self.right_direction:
            direction = mushroom_right_pack
        else:
            direction = mushroom_left_pack
        if self.height_count <= 7:
            if self.attack:
                self.height_count += 1
                self.current_y += 18
            elif self.take_damage:
                self.height_count += 1
                self.current_y += 18
            else:
                self.height_count += 1
                self.current_y += 15
                background.blit(direction[0], (400, 690 - self.current_y))
        elif 7 < self.height_count <= 14:
            if self.attack:
                self.height_count += 1
                self.current_y -= 18
            elif self.take_damage:
                self.height_count += 1
                self.current_y -= 18
            else:
                self.height_count += 1
                self.current_y -= 18
                background.blit(direction[0], (400, 690 - self.current_y))
        else:
            self.jump = False
            self.height_count = 0
            self.current_y = 0

    def attack_player(self, background):
        if self.right_direction:
            direction = mushroom_attack_right_pack
        else:
            direction = mushroom_attack_left_pack
        if self.attack_animation_count <= 8:
            background.blit(direction[self.attack_animation_count],
                            (388, 675 - self.current_y))
            self.attack_animation_count += 1
        else:
            background.blit(direction[self.attack_animation_count],
                            (388, 675 - self.current_y))
            self.attack_animation_count = 0
            self.attack = False
            self.launch = True

    def take_damage_player(self, background):
        if self.right_direction:
            direction = mushroom_attack_right_pack
        else:
            direction = mushroom_attack_left_pack
        if self.take_damage_count < 7:
            background.blit(direction[self.take_damage_count], (388, 675 - self.current_y))
            self.take_damage_count += 1
        else:
            self.take_damage_count = 0
            self.take_damage = False
            self.player_hp -= 10

    def death(self, background):
        if self.death_animation_count < 5:
            background.blit(mushroom_death_pack[self.death_animation_count],
                            (388, 675)
                            )
            self.death_animation_count += 1
        else:
            background.blit(mushroom_death_pack[self.death_animation_count],
                            (388, 675)
                            )
            self.dead = True

    def dodge_player(self, background):
        if self.right_direction:
            direction = mushroom_dodge_right_pack
            step = -50
        else:
            direction = mushroom_dodge_left_pack
            step = 50
        if self.dodge_animation_count <= 3:
            background.blit(direction[self.dodge_animation_count], (self.x_coordinate, self.y_coordinate))
            self.dodge_animation_count += 1
            background.blit(direction[self.dodge_animation_count], (self.x_coordinate, self.y_coordinate))
            self.dodge_underground_start_time = datetime.datetime.now()
        if datetime.datetime.now() - self.dodge_underground_start_time >= self.dodge_underground_time:
            if self.dodge_animation_count == 4 and self.dodge_up_animation_count == 4:
                self.current_x += step
                background.blit(direction[self.dodge_up_animation_count],
                                (self.x_coordinate, self.y_coordinate))
                self.dodge_up_animation_count -= 1
            elif self.dodge_animation_count == 4 and self.dodge_up_animation_count >= 1:
                self.current_x += step
                background.blit(direction[self.dodge_up_animation_count],
                                (self.x_coordinate, self.y_coordinate))
                self.dodge_up_animation_count -= 1
            else:
                background.blit(direction[self.dodge_up_animation_count],
                                (self.x_coordinate, self.y_coordinate))
                self.dodge_up_animation_count = 4
                self.dodge_animation_count = 0
                self.dodge = False
                self.dodge_last_use = datetime.datetime.now()
