import pygame
from models import (
    forrest_background, mushroom_right_pack,
    mushroom_left_pack, mushroom_attack_right_pack, villager_stop,
    mushroom_fire_pack, mushroom_attack_left_pack, villager_idle_pack,

)

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((928, 793))
screen.fill(color=(52, 134, 235))
current_x = 0
current_y = 0
background = forrest_background[0]
pygame.display.set_caption("brave_mushroom")
running = True
right_direction = True
jump = False
attack = False
move = False
fire_animation = False
villager_under_attack = False
villager_contact_constant_x = 43
villager_contact_constant_y = 58
attack_animation_count = 0
fire_animation_count = 0
fireball_x = 0
fireball_x_previous = 0
fire_x = current_x
fire_y = current_y
height_count = 0
my_font = pygame.font.Font('Fonts/Sixtyfour.ttf', 40)
text_surface = my_font.render('Brave mushroom', True, 'Black')
protohonist_animation_count = 0
enemy_position_x = 750
enemy_position_y = 590
villager_animation_count = 0


while running:
    # Game configurations
    clock.tick(20)
    keys = pygame.key.get_pressed()
    # Background configurations
    screen.blit(background, (current_x, 0))
    for layer in forrest_background[1:]:
        background.blit(layer, (0, 0))
    screen.blit(background, (current_x + 928, 0))
    for layer in forrest_background[1:]:
        background.blit(layer, (0, 0))
    pygame.display.update()
    # Villager actions:
    if villager_animation_count == 7:
        villager_animation_count = 0
    if not villager_under_attack:
        background.blit(villager_idle_pack[villager_animation_count], (enemy_position_x, enemy_position_y))
        villager_animation_count += 1
    else:
        pass
    # Protohonist (mushroom) actions, configurations:
    if protohonist_animation_count == 4:
        protohonist_animation_count = 0
    if not jump:
        if keys[pygame.K_UP]:
            jump = True
            if right_direction:
                background.blit(mushroom_right_pack[0], (400 - current_x, 690 - current_y))
            else:
                background.blit(mushroom_left_pack[0], (400 - current_x, 690 - current_y))
    elif jump:
        if height_count <= 7:
            if right_direction:
                if attack:
                    height_count += 1
                    current_y += 10
                else:
                    height_count += 1
                    current_y += 10
                    background.blit(mushroom_right_pack[0], (400 - current_x, 690 - current_y))
            elif not right_direction:
                if attack:
                    height_count += 1
                    current_y += 10
                else:
                    height_count += 1
                    current_y += 10
                    background.blit(mushroom_left_pack[0], (400 - current_x, 690 - current_y))
        elif 7 < height_count <= 14:
            if right_direction:
                if attack:
                    height_count += 1
                    current_y -= 10
                else:
                    height_count += 1
                    current_y -= 10
                    background.blit(mushroom_right_pack[0], (400 - current_x, 690 - current_y))
            elif not right_direction:
                if attack:
                    height_count += 1
                    current_y -= 10
                else:
                    height_count += 1
                    current_y -= 10
                    background.blit(mushroom_left_pack[0], (400 - current_x, 690 - current_y))
        else:
            jump = False
            height_count = 0
            current_y = 0
    if keys[pygame.K_LEFT]:
        move = True
        right_direction = False
        if attack:
            pass
        else:
            background.blit(mushroom_left_pack[protohonist_animation_count], (400 - current_x, 690 - current_y))
            protohonist_animation_count += 1
            current_x += 5
    elif keys[pygame.K_RIGHT]:
        move = True
        right_direction = True
        if attack:
            pass
        else:
            background.blit(mushroom_right_pack[protohonist_animation_count], (400 - current_x, 690 - current_y))
            protohonist_animation_count += 1
            current_x -= 5
    else:
        move = False
    if not attack and not jump and not move:
        if right_direction:
            background.blit(mushroom_right_pack[0], (400 - current_x, 690 - current_y))
        else:
            background.blit(mushroom_left_pack[0], (400 - current_x, 690 - current_y))
    if not attack:
        if keys[pygame.K_SPACE]:
            attack = True
    elif attack:
        if right_direction:
            if attack_animation_count <= 8:
                background.blit(mushroom_attack_right_pack[attack_animation_count], (388 - current_x, 675 - current_y))
                attack_animation_count += 1
            else:
                background.blit(mushroom_attack_right_pack[attack_animation_count], (388 - current_x, 675 - current_y))
                fire_x = current_x
                fire_y = current_y
                fire_animation = True
                attack_animation_count = 0
                attack = False
        else:
            if attack_animation_count <= 8:
                background.blit(mushroom_attack_left_pack[attack_animation_count], (388 - current_x, 675 - current_y))
                attack_animation_count += 1
            else:
                background.blit(mushroom_attack_left_pack[attack_animation_count], (388 - current_x, 675 - current_y))
                fire_x = current_x
                fire_y = current_y
                fire_animation = True
                attack_animation_count = 0
                attack = False
    if fire_animation:
        if fire_animation_count <= 7:
            if right_direction:
                if ((400 - fire_x + fireball_x) <= (enemy_position_x + villager_contact_constant_x) <= (400 - fire_x + fireball_x + 50)
                        and (690 - fire_y) >= (enemy_position_y + villager_contact_constant_y)):
                    villager_under_attack = True
                    fire_animation_count = 7
                    background.blit(mushroom_fire_pack[fire_animation_count], (400 - fire_x + fireball_x, 690 - fire_y))
                else:
                    background.blit(mushroom_fire_pack[fire_animation_count], (400 - fire_x + fireball_x, 690 - fire_y))
                    fire_animation_count += 1
                    fireball_x += 50
            if not right_direction:
                background.blit(mushroom_fire_pack[fire_animation_count], (400 - fire_x - fireball_x, 690 - fire_y))
                fire_animation_count += 1
                fireball_x += 50
        else:
            fireball_x = 0
            fire_x = 0
            fire_animation = 0
            fire_animation_count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

