import datetime
from models import (mushroom_right_pack, mushroom_left_pack, mushroom_attack_right_pack, mushroom_attack_left_pack,
                    mushroom_death_pack, mushroom_dodge_right_pack, mushroom_dodge_left_pack, tentacles_up_pack,
                    mushroom_attack_tentacles_right_pack, mushroom_attack_tentacles_left_pack)


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
    tentacles_z = False
    tentacles_x = False
    tentacles_c = False
    tentacles_z_grow_up = False
    tentacles_x_grow_up = False
    tentacles_c_grow_up = False
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
    tentacle_up_animation_count_z = 0
    tentacle_down_animation_count_z = 4
    tentacle_up_animation_count_x = 0
    tentacle_down_animation_count_x = 4
    tentacle_up_animation_count_c = 0
    tentacle_down_animation_count_c = 4
    player_hp = 100
    dodge_cooldown = datetime.timedelta(seconds=2)
    dodge_last_use = datetime.datetime.now()
    dodge_underground_time = datetime.timedelta(seconds=2)
    dodge_underground_start_time = datetime.datetime.now()
    tentacles_z_cooldown = datetime.timedelta(seconds=5)
    tentacles_z_last_use = datetime.datetime.now()
    tentacles_x_cooldown = datetime.timedelta(seconds=5)
    tentacles_x_last_use = datetime.datetime.now()
    tentacles_c_cooldown = datetime.timedelta(seconds=5)
    tentacles_c_last_use = datetime.datetime.now()

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
                self.current_y += 21
            elif self.take_damage:
                self.height_count += 1
                self.current_y += 21
            else:
                self.height_count += 1
                self.current_y += 21
                background.blit(direction[0], (400, 690 - self.current_y))
        elif 7 < self.height_count <= 14:
            if self.attack:
                self.height_count += 1
                self.current_y -= 21
            elif self.take_damage:
                self.height_count += 1
                self.current_y -= 21
            else:
                self.height_count += 1
                self.current_y -= 21
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
            step = -65
        else:
            direction = mushroom_dodge_left_pack
            step = 65
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

    # def tentacles_up_z(self, background):
    #     if self.right_direction:
    #         direction = mushroom_attack_tentacles_right_pack
    #         step = 250
    #     else:
    #         direction = mushroom_attack_tentacles_left_pack
    #         step = -250
    #     if self.tentacle_up_animation_count_z < 4:
    #         background.blit(direction[self.tentacle_up_animation_count_z], (388, 675))
    #         background.blit(tentacles_up_pack[self.tentacle_up_animation_count_z], (self.x_coordinate+step, 590))
    #         self.tentacle_up_animation_count_z += 1
    #     elif self.tentacle_up_animation_count_z == 4 and self.tentacle_down_animation_count_z == 4:
    #         background.blit(direction[self.tentacle_up_animation_count_z], (388, 675))
    #         background.blit(tentacles_up_pack[self.tentacle_up_animation_count_z], (self.x_coordinate + step, 590))
    #         self.tentacle_down_animation_count_z -= 1
    #     elif 0 < self.tentacle_down_animation_count_z < 4:
    #         background.blit(direction[self.tentacle_down_animation_count_z], (388, 675))
    #         background.blit(tentacles_up_pack[self.tentacle_down_animation_count_z], (self.x_coordinate + step, 590))
    #         self.tentacle_down_animation_count_z -= 1
    #     else:
    #         background.blit(direction[self.tentacle_down_animation_count_z], (388, 675))
    #         background.blit(tentacles_up_pack[self.tentacle_down_animation_count_z], (self.x_coordinate + step, 590))
    #         self.tentacle_up_animation_count_z = 0
    #         self.tentacle_down_animation_count_z = 4
    #         self.tentacles_z = False
    #         self.tentacles_z_last_use = datetime.datetime.now()

    def use_tentacles_z(self, background, up_counter, down_counter):
        if self.right_direction:
            direction = mushroom_attack_tentacles_right_pack
        else:
            direction = mushroom_attack_tentacles_left_pack
        if up_counter < 4:
            background.blit(direction[self.tentacle_up_animation_count_z], (388, 675))
        elif up_counter == 4 and down_counter == 4:
            background.blit(direction[self.tentacle_up_animation_count_z], (388, 675))
        elif 0 < down_counter < 4:
            background.blit(direction[self.tentacle_down_animation_count_z], (388, 675))
        else:
            background.blit(direction[self.tentacle_down_animation_count_z], (388, 675))
            self.tentacles_z = False
            self.tentacles_z_last_use = datetime.datetime.now()

    def use_tentacles_x(self, background, up_counter, down_counter):
        if self.right_direction:
            direction = mushroom_attack_tentacles_right_pack
        else:
            direction = mushroom_attack_tentacles_left_pack
        if up_counter < 4:
            background.blit(direction[self.tentacle_up_animation_count_x], (388, 675))
        elif up_counter == 4 and down_counter == 4:
            background.blit(direction[self.tentacle_up_animation_count_x], (388, 675))
        elif 0 < down_counter < 4:
            background.blit(direction[self.tentacle_down_animation_count_x], (388, 675))
        else:
            background.blit(direction[self.tentacle_down_animation_count_x], (388, 675))
            self.tentacles_x = False
            self.tentacles_x_last_use = datetime.datetime.now()

    def use_tentacles_c(self, background, up_counter, down_counter):
        if self.right_direction:
            direction = mushroom_attack_tentacles_right_pack
        else:
            direction = mushroom_attack_tentacles_left_pack
        if up_counter < 4:
            background.blit(direction[self.tentacle_up_animation_count_c], (388, 675))
        elif up_counter == 4 and down_counter == 4:
            background.blit(direction[self.tentacle_up_animation_count_c], (388, 675))
        elif 0 < down_counter < 4:
            background.blit(direction[self.tentacle_down_animation_count_c], (388, 675))
        else:
            background.blit(direction[self.tentacle_down_animation_count_c], (388, 675))
            self.tentacles_c = False
            self.tentacles_c_last_use = datetime.datetime.now()

