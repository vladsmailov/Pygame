import pygame
import datetime
import random
from game import Game
from player import Player
from fireball import Fireball
from background import Background

if __name__ == '__main__':
    player = Player()
    game = Game()
    fireball = None
    background = Background(game.screen)
    running = True
    enemy = None
    while game.running:
        game.set_tick(quantity=15)
        game.show_players_hp(str(player.player_hp))
        game.game_update()
        keys = pygame.key.get_pressed()
        background.show(player.current_x)
        game.check_players_area(player.current_x)
        if game.players_area == 1:
            if game.enemy_counter <= 1:
                game.generate_enemy(background.screen, player.current_x, random.randint(500, 1000), 590)
            if player.current_x <= -1000 and game.dead_enemy_counter == 0:
                if player.right_direction:
                    player.blocked = True
                else:
                    player.blocked = False
            else:
                player.blocked = False
        elif game.players_area == 2:
            if game.enemy_counter <= 3:
                for _ in range(2):
                    game.generate_enemy(background.screen, player.current_x, random.randint(1700, 2000), 590)
        if player.dodge and not player.blocked:
            player.dodge_player(background.screen)
        if player.take_damage and not player.dead:
            player.take_damage_player(background.screen)
            if player.player_hp == 0:
                player.death(background.screen)
        if player.dead:
            player.death(background.screen)
            enemy.attack = False
            enemy.under_attack = False
        if not player.jump:
            if keys[pygame.K_UP] and not player.dodge:
                player.jump = True
                player.idle_player(background.screen)
        elif player.jump and not player.dead:
            player.jump_player(background.screen)
        if keys[pygame.K_RIGHT] and not player.take_damage and not player.dead and not player.dodge and not player.blocked:
            player.move_player("right", background.screen)
        elif keys[pygame.K_LEFT] and not player.take_damage and not player.dead and not player.dodge and player.current_x < 0:
            player.move_player("left", background.screen)
        elif keys[pygame.K_DOWN] and not player.take_damage and not player.dead:
            if player.current_x > -100 and not player.right_direction or\
                    (datetime.datetime.now() - player.dodge_last_use) <= player.dodge_cooldown:
                player.idle_player(background.screen)
            else:
                player.dodge = True
                player.dodge_player(background.screen)
        else:
            player.move = False
        if not player.attack:
            if keys[pygame.K_SPACE] and not player.dodge:
                player.attack = True
                player.idle_player(background.screen)
        elif player.attack and not player.take_damage and not player.dead and not player.dodge:
            player.attack_player(background.screen)
            if player.launch:
                fireball = Fireball(player.current_x, player.current_y, player.right_direction)
                player.launch = False
        if fireball and fireball.fireball_animation:
            fireball.fire(background.screen)
        if not player.move and not player.attack and not player.jump and not player.take_damage and not player.dead \
                and not player.dodge:
            player.idle_player(background.screen)
        for enemy in game.enemies:
            if enemy and not enemy.under_attack and not enemy.dead and not enemy.run and not enemy.attack:
                enemy.idle_enemy(background.screen, player.current_x)
                enemy.check_opponent(player.current_x, player.x_coordinate, player.current_y, player.y_coordinate)
            if enemy.attack and not enemy.dead and not enemy.take_hit:
                enemy.enemy_attack(background.screen, player.current_x)
                if enemy.x_coordinate - (player.x_coordinate - player.current_x) <= 10 and not player.dodge:
                    player.take_damage = True
            if enemy and enemy.under_attack and not enemy.attack and not enemy.take_hit:
                enemy.run = True
                enemy.enemy_run(
                    background.screen, player.current_x, player.x_coordinate, player.current_y, player.y_coordinate
                )
            if enemy.dead:
                enemy.death(background.screen, player.current_x)
                if enemy.death_animation_count == 1:
                    game.dead_enemy_counter += 1
            if fireball and fireball.fireball_animation and fireball.check_hit(enemy):
                if not enemy.dead:
                    fireball = None
                    enemy.under_attack = True
                    enemy.take_hit = True
            if enemy.under_attack and not enemy.dead and enemy.take_hit:
                enemy.take_damage(background.screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.quit()
