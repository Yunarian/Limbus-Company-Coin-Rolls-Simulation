import pygame
import random
from meursault import Meursault
from trash_crab import TrashCrab
from attack_skills import AttackSkill

# Setting up fonts
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Calibri', 16)
pygame.display.set_caption("Limbus Company Clash Simulation")

# Setting up the window
size = (1200, 675)
screen = pygame.display.set_mode(size)
screen.fill((100, 100, 100))
run = True


# Functions used in the pygame loop
# Takes a tuple and an integer as parameters.
# the last element of the tuple and sanity generate which side of the coin was rolled.
# The first two elements of the tuple generate which values were rolled
# skill_attributes = (coins, coin_power, base_power)
def coin_rolls(sanity, skill_attributes):
    coin_side_roll = []

    for i in range(skill_attributes[0]):
        if random.randint(1, 100) <= 50 + sanity:
            coin_side_roll.append("Heads")
        else:
            coin_side_roll.append("Tails")

    attack_rolls = []
    current_attack_power = skill_attributes[2]

    for i in range(len(coin_side_roll)):
        if coin_side_roll[i] == "Heads":
            current_attack_power += skill_attributes[1]

        attack_rolls.append(current_attack_power)

    return attack_rolls


# takes 4 parameters, with _sanity being integers, and _skill_attributes being lists
# ally_skill_attributes = (ally_coins, ally_coin_power, ally_base_power)
# enemy_skill_attributes = (enemy_coins, enemy_coin_power, enemy_base_power)
def clash_calculate(ally_sanity, ally_skill_attributes, enemy_sanity, enemy_skill_attributes):
    damage_dealt = 0

    while ally_skill_attributes[0] != 0 and enemy_skill_attributes[0] != 0:
        ally_attack_rolls = coin_rolls(ally_sanity, ally_skill_attributes)
        enemy_attack_rolls = coin_rolls(enemy_sanity, enemy_skill_attributes)

        print("Ally Attack roll:", ally_attack_rolls[ally_skill_attributes[0] - 1])
        print("Enemy Attack roll:", enemy_attack_rolls[enemy_skill_attributes[0] - 1])

        if ally_attack_rolls[ally_skill_attributes[0] - 1] > enemy_attack_rolls[enemy_skill_attributes[0] - 1]:
            print("Ally clash win. ")
            enemy_skill_attributes[0] -= 1

        elif ally_attack_rolls[ally_skill_attributes[0] - 1] < enemy_attack_rolls[enemy_skill_attributes[0] - 1]:
            print("Enemy clash win. ")
            ally_skill_attributes[0] -= 1

        elif ally_attack_rolls[ally_skill_attributes[0] - 1] == enemy_attack_rolls[enemy_skill_attributes[0] - 1]:
            print("Tie. ")

        print()

    # Regenerates the coin rolls
    if ally_skill_attributes[0] == 0:
        enemy_attack_rolls = coin_rolls(enemy_sanity, enemy_skill_attributes)
        print("Enemy's attack goes through.")

        for i in range(len(enemy_attack_rolls)):
            damage_dealt += enemy_attack_rolls[i]
            print("Enemy did", damage_dealt, "damage")

    else:
        ally_attack_rolls = coin_rolls(ally_sanity, ally_skill_attributes)
        print("Ally's attack goes through. ")

        for i in range(len(ally_attack_rolls)):
            damage_dealt += ally_attack_rolls[i]
            print("Ally did", damage_dealt, "damage.")


meursault = Meursault(150, 400)
meursault_s1 = AttackSkill(25, 25, "S1", "Meursault ")
meursault_s2 = AttackSkill(25, 285, "S2", "Meursault ")
meursault_s3 = AttackSkill(25, 545, "S3", "Meursault ")
# Per tuple, the attributes go (coins, coin_power, base_power)
# First tuple in the tuple is s1, second is s2, third is s3
meursault_skills_attributes = ((2, 4, 3), (1, 9, 6), (4, 2, 4))

trash_crab = TrashCrab(800, 450)
trash_crab_gwah = AttackSkill(1075, 20, "Gwah", "Trash Crab ")
trash_crab_gwaaah = AttackSkill(1075, 195, "Gwaaah", "Trash Crab ")
trash_crab_shell_tackle = AttackSkill(1075, 370, "Shell Tackle", "Trash Crab ")
trash_crab_foaming = AttackSkill(1075, 545, "Foaming", "Trash Crab ")
# Per tuple, the attributes go (coins, coin_power, base_power)
# First tuple in the tuple is Gwah, second is Gwaaah, third is Shell tackle, fourth is Foaming
trash_crab_skill_attributes = ((2, 2, 2), (3, 2, 3), (1, 6, 3), (1, 7, 4))

meursault_skill_description_render = [False, False, False]
trash_crab_skill_description_render = [False, False, False, False]

# Clicking on the appropriate skill would have that skill be used, and the associated animation if the attack hits.

# Pygame loop
while run:

    for event in pygame.event.get():  # User did something
        # Mouse hover-over detection with Meursault's skills
        # first element is s1, second is s2, third is s3
        meursault_skill_description_render = [False, False, False]
        if meursault_s1.rect.collidepoint(pygame.mouse.get_pos()):
            meursault_skill_description_render[0] = True

        if meursault_s2.rect.collidepoint(pygame.mouse.get_pos()):
            meursault_skill_description_render[1] = True

        if meursault_s3.rect.collidepoint(pygame.mouse.get_pos()):
            meursault_skill_description_render[2] = True

        # Mouse hover-over detection with trash crab skills
        # first is gwah, second is gwaaah, third is shell tackle, fourth is foaming.
        trash_crab_skill_description_render = [False, False, False, False]
        if trash_crab_gwah.rect.collidepoint(pygame.mouse.get_pos()):
            trash_crab_skill_description_render[0] = True

        if trash_crab_gwaaah.rect.collidepoint(pygame.mouse.get_pos()):
            trash_crab_skill_description_render[1] = True

        if trash_crab_shell_tackle.rect.collidepoint(pygame.mouse.get_pos()):
            trash_crab_skill_description_render[2] = True

        if trash_crab_foaming.rect.collidepoint(pygame.mouse.get_pos()):
            trash_crab_skill_description_render[3] = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(meursault_skill_description_render)):
                    if meursault_skill_description_render[i] is True:
                        print(i)

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((100, 100, 100))

    screen.blit(meursault.image, meursault.rect)
    screen.blit(meursault_s1.image, meursault_s1.rect)
    screen.blit(meursault_s2.image, meursault_s2.rect)
    screen.blit(meursault_s3.image, meursault_s3.rect)

    screen.blit(trash_crab.image, trash_crab.rect)
    screen.blit(trash_crab_gwah.image, trash_crab_gwah.rect)
    screen.blit(trash_crab_gwaaah.image, trash_crab_gwaaah.rect)
    screen.blit(trash_crab_shell_tackle.image, trash_crab_shell_tackle.rect)
    screen.blit(trash_crab_foaming.image, trash_crab_foaming.rect)

    if meursault_skill_description_render[0] is True:
        screen.blit(pygame.image.load("Meursault S1 Description.png"), (200, 50))

    if meursault_skill_description_render[1] is True:
        screen.blit(pygame.image.load("Meursault S2 Description.png"), (200, 50))

    if meursault_skill_description_render[2] is True:
        screen.blit(pygame.image.load("Meursault S3 Description.png"), (200, 50))

    if trash_crab_skill_description_render[0] is True:
        screen.blit(pygame.image.load("Trash Crab Gwah Description.png"), (800, 50))

    if trash_crab_skill_description_render[1] is True:
        screen.blit(pygame.image.load("Trash Crab Gwaaah Description.png"), (800, 50))

    if trash_crab_skill_description_render[2] is True:
        screen.blit(pygame.image.load("Trash Crab Shell Tackle Description.png"), (800, 50))

    if trash_crab_skill_description_render[3] is True:
        screen.blit(pygame.image.load("Trash Crab Foaming Description.png"), (800, 50))

    pygame.display.update()

pygame.quit()
