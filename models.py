"""
Imported models for main file.
"""
import pygame


"""Forrest background."""
layer0 = pygame.image.load("Images/Background layers/Layer_0011_0.png")
layer1 = pygame.image.load("Images/Background layers/Layer_0010_1.png")
layer2 = pygame.image.load("Images/Background layers/Layer_0009_2.png")
layer3 = pygame.image.load("Images/Background layers/Layer_0008_3.png")
layer4 = pygame.image.load("Images/Background layers/Layer_0007_Lights.png")
layer5 = pygame.image.load("Images/Background layers/Layer_0006_4.png")
layer6 = pygame.image.load("Images/Background layers/Layer_0005_5.png")
layer7 = pygame.image.load("Images/Background layers/Layer_0004_Lights.png")
layer8 = pygame.image.load("Images/Background layers/Layer_0003_6.png")
layer9 = pygame.image.load("Images/Background layers/Layer_0002_7.png")
layer10 = pygame.image.load("Images/Background layers/Layer_0001_8.png")
layer11 = pygame.image.load("Images/Background layers/Layer_0000_9.png")

all_in_one = pygame.image.load("Images/Background layers/Background_for_forrest.png")

forrest_background = [layer0, layer2, layer3, layer4, layer5, layer6, layer7, layer8, layer9, layer10, layer11]


"""Mushroom character moves right."""
mushroom0 = pygame.image.load("Images/Mushroom_moves_right/Mushroom_stop_position.png")
mushroom1 = pygame.image.load("Images/Mushroom_moves_right/Mushroom_right_position1.png")
mushroom2 = pygame.image.load("Images/Mushroom_moves_right/Mushroom_right_position2.png")
mushroom3 = pygame.image.load("Images/Mushroom_moves_right/Mushroom_right_position3.png")
mushroom4 = pygame.image.load("Images/Mushroom_moves_right/Mushroom_right_position4.png")

mushroom_right_pack = [mushroom0, mushroom1, mushroom2, mushroom3, mushroom4]

"""Mushroom character moves left."""
mushroom0l = pygame.image.load("Images/Mushroom_moves_left/Mushroom_stop_position_left.png")
mushroom1l = pygame.image.load("Images/Mushroom_moves_left/Mushroom_left_position1.png")
mushroom2l = pygame.image.load("Images/Mushroom_moves_left/Mushroom_left_position2.png")
mushroom3l = pygame.image.load("Images/Mushroom_moves_left/Mushroom_left_position3.png")
mushroom4l = pygame.image.load("Images/Mushroom_moves_left/Mushroom_left_position4.png")

mushroom_left_pack = [mushroom0l, mushroom1l, mushroom2l, mushroom3l, mushroom4l]

"""Mushroom attack right."""
mushroom_attack1 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack1.png")
mushroom_attack2 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack2.png")
mushroom_attack3 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack3.png")
mushroom_attack4 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack4.png")
mushroom_attack5 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack5.png")
mushroom_attack6 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack6.png")
mushroom_attack7 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack7.png")
mushroom_attack8 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack8.png")
mushroom_attack9 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack9.png")
mushroom_attack10 = pygame.image.load("Images/Mushroom_attack_right/mushroom_attack10.png")

mushroom_attack_right_pack = [
    mushroom_attack1, mushroom_attack2, mushroom_attack3, mushroom_attack4,
    mushroom_attack5, mushroom_attack6, mushroom_attack7, mushroom_attack8,
    mushroom_attack9, mushroom_attack10
]

"""Mushroom attack left."""
mushroom_attack1l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack1l.png")
mushroom_attack2l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack2l.png")
mushroom_attack3l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack3l.png")
mushroom_attack4l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack4l.png")
mushroom_attack5l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack5l.png")
mushroom_attack6l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack6l.png")
mushroom_attack7l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack7l.png")
mushroom_attack8l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack8l.png")
mushroom_attack9l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack9l.png")
mushroom_attack10l = pygame.image.load("Images/Mushroom_attack_left/mushroom_attack10l.png")

mushroom_attack_left_pack = [
    mushroom_attack1l, mushroom_attack2l, mushroom_attack3l, mushroom_attack4l,
    mushroom_attack5l, mushroom_attack6l, mushroom_attack7l, mushroom_attack8l,
    mushroom_attack9l, mushroom_attack10l
]

"""Mushroom fire."""
mushroom_fire0 = pygame.image.load("Images/Mushroom_fire/mushroom_fire0.png")
mushroom_fire1 = pygame.image.load("Images/Mushroom_fire/mushroom_fire1.png")
mushroom_fire2 = pygame.image.load("Images/Mushroom_fire/mushroom_fire2.png")
mushroom_fire3 = pygame.image.load("Images/Mushroom_fire/mushroom_fire3.png")
mushroom_fire4 = pygame.image.load("Images/Mushroom_fire/mushroom_fire4.png")
mushroom_fire5 = pygame.image.load("Images/Mushroom_fire/mushroom_fire5.png")
mushroom_fire6 = pygame.image.load("Images/Mushroom_fire/mushroom_fire6.png")
mushroom_fire7 = pygame.image.load("Images/Mushroom_fire/mushroom_fire7.png")

mushroom_fire_pack = [
    mushroom_fire0, mushroom_fire1, mushroom_fire2,
    mushroom_fire3, mushroom_fire4, mushroom_fire5,
    mushroom_fire6, mushroom_fire7
]

"""Villager."""
villager_stop = pygame.image.load("Images/Villager_stop/villager_stop.png")

"""Villager idle right."""
villager_idle0 = pygame.image.load("Images/Villager_idle/villager_idle0.png")
villager_idle1 = pygame.image.load("Images/Villager_idle/villager_idle1.png")
villager_idle2 = pygame.image.load("Images/Villager_idle/villager_idle2.png")
villager_idle3 = pygame.image.load("Images/Villager_idle/villager_idle3.png")
villager_idle4 = pygame.image.load("Images/Villager_idle/villager_idle4.png")
villager_idle5 = pygame.image.load("Images/Villager_idle/villager_idle5.png")
villager_idle6 = pygame.image.load("Images/Villager_idle/villager_idle6.png")
villager_idle7 = pygame.image.load("Images/Villager_idle/villager_idle7.png")

villager_idle_pack = [
    villager_idle0, villager_idle1, villager_idle2,
    villager_idle3, villager_idle4, villager_idle5,
    villager_idle6, villager_idle7
]

"""Villager idle left."""
villager_idle0l = pygame.image.load("Images/Villager_idle_left/villager_idle0l.png")
villager_idle1l = pygame.image.load("Images/Villager_idle_left/villager_idle1l.png")
villager_idle2l = pygame.image.load("Images/Villager_idle_left/villager_idle2l.png")
villager_idle3l = pygame.image.load("Images/Villager_idle_left/villager_idle3l.png")
villager_idle4l = pygame.image.load("Images/Villager_idle_left/villager_idle4l.png")
villager_idle5l = pygame.image.load("Images/Villager_idle_left/villager_idle5l.png")
villager_idle6l = pygame.image.load("Images/Villager_idle_left/villager_idle6l.png")
villager_idle7l = pygame.image.load("Images/Villager_idle_left/villager_idle7l.png")

villager_idle_left_pack = [
    villager_idle0l, villager_idle1l, villager_idle2l,
    villager_idle3l, villager_idle4l, villager_idle5l,
    villager_idle6l, villager_idle7l
]

"""Villager takes damage right."""
villager_takes_damage0 = pygame.image.load("Images/Villager_takes_damage/villager_damaged0.png")
villager_takes_damage1 = pygame.image.load("Images/Villager_takes_damage/villager_damaged1.png")
villager_takes_damage2 = pygame.image.load("Images/Villager_takes_damage/villager_damaged2.png")
villager_takes_damage3 = pygame.image.load("Images/Villager_takes_damage/villager_damaged3.png")

villager_takes_damage_pack = [
    villager_takes_damage0, villager_takes_damage1, villager_takes_damage2, villager_takes_damage3
]

"""Villager takes damage left."""
villager_takes_damage0l = pygame.image.load("Images/Villager_takes_damage_left/villager_damaged0l.png")
villager_takes_damage1l = pygame.image.load("Images/Villager_takes_damage_left/villager_damaged1l.png")
villager_takes_damage2l = pygame.image.load("Images/Villager_takes_damage_left/villager_damaged2l.png")
villager_takes_damage3l = pygame.image.load("Images/Villager_takes_damage_left/villager_damaged3l.png")

villager_takes_damage_left_pack = [
    villager_takes_damage0l, villager_takes_damage1l, villager_takes_damage2l, villager_takes_damage3l
]

"""Villager dead right."""
villager_dead0 = pygame.image.load("Images/Villager_death/villager_dead0.png")
villager_dead1 = pygame.image.load("Images/Villager_death/villager_dead1.png")
villager_dead2 = pygame.image.load("Images/Villager_death/villager_dead2.png")
villager_dead3 = pygame.image.load("Images/Villager_death/villager_dead3.png")
villager_dead4 = pygame.image.load("Images/Villager_death/villager_dead4.png")
villager_dead5 = pygame.image.load("Images/Villager_death/villager_dead5.png")

villager_dead_pack = [
    villager_dead0, villager_dead1, villager_dead2, villager_dead3, villager_dead4, villager_dead5
]

"""Villager dead left."""
villager_dead0l = pygame.image.load("Images/Villager_death_left/villager_dead0l.png")
villager_dead1l = pygame.image.load("Images/Villager_death_left/villager_dead1l.png")
villager_dead2l = pygame.image.load("Images/Villager_death_left/villager_dead2l.png")
villager_dead3l = pygame.image.load("Images/Villager_death_left/villager_dead3l.png")
villager_dead4l = pygame.image.load("Images/Villager_death_left/villager_dead4l.png")
villager_dead5l = pygame.image.load("Images/Villager_death_left/villager_dead5l.png")

villager_dead_left_pack = [
    villager_dead0l, villager_dead1l, villager_dead2l, villager_dead3l, villager_dead4l, villager_dead5l
]

"""Villager moves right."""
villager_run_right0 = pygame.image.load("Images/Villager_run/villager_run0.png")
villager_run_right1 = pygame.image.load("Images/Villager_run/villager_run1.png")
villager_run_right2 = pygame.image.load("Images/Villager_run/villager_run2.png")
villager_run_right3 = pygame.image.load("Images/Villager_run/villager_run3.png")
villager_run_right4 = pygame.image.load("Images/Villager_run/villager_run4.png")
villager_run_right5 = pygame.image.load("Images/Villager_run/villager_run5.png")
villager_run_right6 = pygame.image.load("Images/Villager_run/villager_run6.png")
villager_run_right7 = pygame.image.load("Images/Villager_run/villager_run7.png")

villager_run_right_pack = [
    villager_run_right0, villager_run_right1, villager_run_right2, villager_run_right3,
    villager_run_right4, villager_run_right5, villager_run_right6, villager_run_right7
]

"""Villager moves right."""
villager_run_left0 = pygame.image.load("Images/Villager_run _left/villager_run0l.png")
villager_run_left1 = pygame.image.load("Images/Villager_run _left/villager_run1l.png")
villager_run_left2 = pygame.image.load("Images/Villager_run _left/villager_run2l.png")
villager_run_left3 = pygame.image.load("Images/Villager_run _left/villager_run3l.png")
villager_run_left4 = pygame.image.load("Images/Villager_run _left/villager_run4l.png")
villager_run_left5 = pygame.image.load("Images/Villager_run _left/villager_run5l.png")
villager_run_left6 = pygame.image.load("Images/Villager_run _left/villager_run6l.png")
villager_run_left7 = pygame.image.load("Images/Villager_run _left/villager_run7l.png")

villager_run_left_pack = [
    villager_run_left0, villager_run_left1, villager_run_left2, villager_run_left3,
    villager_run_left4, villager_run_left5, villager_run_left6, villager_run_left7
]

"""Villager attack right."""
villager_attack_right0 = pygame.image.load("Images/Villager_attack_right/villager_attack0.png")
villager_attack_right1 = pygame.image.load("Images/Villager_attack_right/villager_attack1.png")
villager_attack_right2 = pygame.image.load("Images/Villager_attack_right/villager_attack2.png")
villager_attack_right3 = pygame.image.load("Images/Villager_attack_right/villager_attack3.png")

villager_attack_right_pack = [
    villager_attack_right0, villager_attack_right1, villager_attack_right2, villager_attack_right3
]

"""Villager attack left."""
villager_attack_left0 = pygame.image.load("Images/Villager_attack_left/villager_attack0l.png")
villager_attack_left1 = pygame.image.load("Images/Villager_attack_left/villager_attack1l.png")
villager_attack_left2 = pygame.image.load("Images/Villager_attack_left/villager_attack2l.png")
villager_attack_left3 = pygame.image.load("Images/Villager_attack_left/villager_attack3l.png")

villager_attack_left_pack = [
    villager_attack_left0, villager_attack_left1, villager_attack_left2, villager_attack_left3
]

"""Villager attack right 2."""
villager_attack_right_1_0 = pygame.image.load("Images/Villager_attack_right2/villager_attack_right_1_0.png")
villager_attack_right_1_1 = pygame.image.load("Images/Villager_attack_right2/villager_attack_right_1_1.png")
villager_attack_right_1_2 = pygame.image.load("Images/Villager_attack_right2/villager_attack_right_1_2.png")
villager_attack_right_1_3 = pygame.image.load("Images/Villager_attack_right2/villager_attack_right_1_3.png")

villager_attack_right2_pack = [
    villager_attack_right_1_0, villager_attack_right_1_1,
    villager_attack_right_1_2, villager_attack_right_1_3
                               ]

"""Villager attack left 2."""
villager_attack_left_1_0 = pygame.image.load("Images/Villager_attack_left2/villager_attack_left_1_0.png")
villager_attack_left_1_1 = pygame.image.load("Images/Villager_attack_left2/villager_attack_left_1_1.png")
villager_attack_left_1_2 = pygame.image.load("Images/Villager_attack_left2/villager_attack_left_1_2.png")
villager_attack_left_1_3 = pygame.image.load("Images/Villager_attack_left2/villager_attack_left_1_3.png")

villager_attack_left2_pack = [
    villager_attack_left_1_0, villager_attack_left_1_1,
    villager_attack_left_1_2, villager_attack_left_1_3
                               ]
