from models import tentacles_up_pack, dust_explosion_pack
from enemy import Enemy, Knight
import datetime


class Tentacles:
    tentacle_up_animation_count_z = 0
    tentacle_down_animation_count_z = 4
    dust_explosion_z_count = 0
    tentacle_z_current_x = 0
    explosion_z_current_x = 0
    tentacles_z_last_use = datetime.datetime.now()
    tentacles_z = False
    dust_explosion_z = False

    def __init__(self, players_x_coordinate):
        self.players_x_coordinate = players_x_coordinate

    def tentacles_up_z(self, background, right_direction, players_current_x):
        if right_direction:
            step = 250
        else:
            step = -250
        if self.tentacle_up_animation_count_z < 4:
            self.tentacle_z_current_x = 400 - players_current_x + step
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_z],
                            (self.players_x_coordinate+step, 590))
            self.tentacle_up_animation_count_z += 1
        elif self.tentacle_up_animation_count_z == 4 and self.tentacle_down_animation_count_z == 4:
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_z],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_z -= 1
        elif 0 < self.tentacle_down_animation_count_z < 4:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_z],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_z -= 1
        else:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_z],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_up_animation_count_z = 0
            self.tentacle_down_animation_count_z = 4
            self.tentacles_z = False
            self.tentacles_z_last_use = datetime.datetime.now()

    def check_hit(self, enemy: (Enemy, Knight)):
        # Возможно нужна поправка на +15
        if self.tentacle_z_current_x in range(
                enemy.x_coordinate + enemy.enemy_sprite_left_border,
                enemy.x_coordinate + enemy.enemy_sprite_right_border
        ) and not enemy.dead:
            return True
        return False

    def dust_explosion(self, background, right_direction):
        if right_direction:
            step = 175
        else:
            step = -175
        if self.dust_explosion_z_count < 5:
            background.blit(dust_explosion_pack[self.dust_explosion_z_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_z_count += 1
        else:
            background.blit(dust_explosion_pack[self.dust_explosion_z_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_z_count = 0
            self.dust_explosion_z_count = False

