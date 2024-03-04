from models import mushroom_fire_pack
from enemy import Enemy


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
                self.fireball_x += 35
            else:
                self.fireball_x -= 35
            return
        else:
            self.fireball_x = 0
            self.fire_x = 0
            self.fire_animation_count = 0
            self.fireball_animation = False
            return

    def check_hit(self, enemy: Enemy):
        if (self.fireball_current_x - enemy.current_x) in range(
                enemy.x_coordinate + enemy.enemy_sprite_left_border,
                enemy.x_coordinate + enemy.enemy_sprite_right_border
        ) and not enemy.dead:
            return True
        return False
