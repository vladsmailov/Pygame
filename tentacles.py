from models import tentacles_up_pack, dust_explosion_pack
from enemy import Enemy, Knight
import datetime


class Tentacles:
    tentacle_up_animation_count_z = 0
    tentacle_down_animation_count_z = 4
    tentacle_up_animation_count_x = 0
    tentacle_down_animation_count_x = 4
    tentacle_up_animation_count_c = 0
    tentacle_down_animation_count_c = 4
    dust_explosion_z_count = 0
    dust_explosion_x_count = 0
    dust_explosion_c_count = 0
    tentacle_z_current_x = 0
    explosion_z_current_x = 0
    tentacle_x_current_x = 0
    explosion_x_current_x = 0
    tentacle_c_current_x = 0
    explosion_c_current_x = 0
    tentacles_z_last_use = datetime.datetime.now()
    tentacles_x_last_use = datetime.datetime.now()
    tentacles_c_last_use = datetime.datetime.now()
    tentacles_z = False
    dust_explosion_z = False
    tentacles_x = False
    dust_explosion_x = False
    tentacles_c = False
    dust_explosion_c = False

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

    def tentacles_up_x(self, background, right_direction, players_current_x):
        if right_direction:
            step = 150
        else:
            step = -150
        if self.tentacle_up_animation_count_x < 4:
            self.tentacle_x_current_x = 400 - players_current_x + step
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_x],
                            (self.players_x_coordinate+step, 590))
            self.tentacle_up_animation_count_x += 1
        elif self.tentacle_up_animation_count_x == 4 and self.tentacle_down_animation_count_x == 4:
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_x],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_x -= 1
        elif 0 < self.tentacle_down_animation_count_x < 4:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_x],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_x -= 1
        else:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_x],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_up_animation_count_x = 0
            self.tentacle_down_animation_count_x = 4
            self.tentacles_x = False
            self.tentacles_x_last_use = datetime.datetime.now()

    def tentacles_up_c(self, background, right_direction, players_current_x):
        if right_direction:
            step = 50
        else:
            step = -50
        if self.tentacle_up_animation_count_c < 4:
            self.tentacle_c_current_x = 400 - players_current_x + step
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_c],
                            (self.players_x_coordinate+step, 590))
            self.tentacle_up_animation_count_c += 1
        elif self.tentacle_up_animation_count_c == 4 and self.tentacle_down_animation_count_c == 4:
            background.blit(tentacles_up_pack[self.tentacle_up_animation_count_c],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_c -= 1
        elif 0 < self.tentacle_down_animation_count_c < 4:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_c],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_down_animation_count_c -= 1
        else:
            background.blit(tentacles_up_pack[self.tentacle_down_animation_count_c],
                            (self.players_x_coordinate + step, 590))
            self.tentacle_up_animation_count_c = 0
            self.tentacle_down_animation_count_c = 4
            self.tentacles_c = False
            self.tentacles_c_last_use = datetime.datetime.now()

    def check_hit(self, enemy: (Enemy, Knight), button):
        if button == 'z':
            coordinate = self.tentacle_z_current_x
        elif button == 'x':
            coordinate = self.tentacle_x_current_x
        else:
            coordinate = self.tentacle_c_current_x
        # Возможно нужна поправка на +15
        if coordinate in range(
                enemy.x_coordinate + enemy.enemy_sprite_left_border,
                enemy.x_coordinate + enemy.enemy_sprite_right_border
        ) and not enemy.dead:
            return True
        return False

    def dust_explosion_z_animation(self, background, right_direction):
        if right_direction:
            step = 175
        else:
            step = -325
        if self.dust_explosion_z_count < 5:
            background.blit(dust_explosion_pack[self.dust_explosion_z_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_z_count += 1
        else:
            background.blit(dust_explosion_pack[self.dust_explosion_z_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_z_count = 0
            self.dust_explosion_z_count = False

    def dust_explosion_x_animation(self, background, right_direction):
        if right_direction:
            step = 75
        else:
            step = -225
        if self.dust_explosion_x_count < 5:
            background.blit(dust_explosion_pack[self.dust_explosion_x_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_x_count += 1
        else:
            background.blit(dust_explosion_pack[self.dust_explosion_x_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_x_count = 0
            self.dust_explosion_x_count = False

    def dust_explosion_c_animation(self, background, right_direction):
        if right_direction:
            step = -25
        else:
            step = -125
        if self.dust_explosion_c_count < 5:
            background.blit(dust_explosion_pack[self.dust_explosion_c_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_c_count += 1
        else:
            background.blit(dust_explosion_pack[self.dust_explosion_c_count], (self.players_x_coordinate + step, 630))
            self.dust_explosion_c_count = 0
            self.dust_explosion_c_count = False
