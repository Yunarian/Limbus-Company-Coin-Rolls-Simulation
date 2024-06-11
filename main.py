import pygame
import random
from meursault import Meursault
from trash_crab import TrashCrab
from attack_skills import AttackSkill
from combat_starter import CombatStarter

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
# Takes two integers

def heads_tails_rolls(sanity, coins):
    coin_side_rolls = []

    for i in range(coins):
        if random.randint(1, 100) <= 50 + sanity:
            coin_side_rolls.append("Heads")
        else:
            coin_side_rolls.append("Tails")

    return coin_side_rolls


# Takes a list and a tuple as parameters.
# The first element is a list, the second is a tuple
# the last element of the tuple and sanity generate which side of the coin was rolled.
# The first two elements of the tuple generate which values were rolled
# skill_attributes = (coins, coin_power, base_power)
def coin_rolls(coin_side_rolls, skill_attributes):
    attack_rolls = []
    current_attack_power = skill_attributes[2]

    for i in range(len(coin_side_rolls)):
        if coin_side_rolls[i] == "Heads":
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
# First list in the tuple is s1, second is s2, third is s3
meursault_skills_attributes = ([2, 4, 3], [1, 9, 6], [4, 2, 4])

trash_crab = TrashCrab(800, 450)
trash_crab_gwah = AttackSkill(1075, 20, "S1", "Trash Crab ")
trash_crab_gwaaah = AttackSkill(1075, 195, "S2", "Trash Crab ")
trash_crab_shell_tackle = AttackSkill(1075, 370, "S3", "Trash Crab ")
trash_crab_foaming = AttackSkill(1075, 545, "S4", "Trash Crab ")
# Per tuple, the attributes go (coins, coin_power, base_power)
# First list in the tuple is Gwah, second is Gwaaah, third is Shell tackle, fourth is Foaming
trash_crab_skills_attributes = ([2, 2, 2], [3, 2, 3], [1, 6, 3], [1, 7, 4])

meursault_skill_description_render = [False, False, False]
trash_crab_skill_description_render = [False, False, False, False]

meursault_skill_description_render_clicked = [False, False, False]
meursault_skill_clicked = False
trash_crab_skill_description_render_clicked = [False, False, False, False]
trash_crab_skill_clicked = False

coin_heads = pygame.image.load("Images/Coin Heads.png")
coin_tails = pygame.image.load("Images/Coin Tails.png")
combat_starter = CombatStarter(450, 400)
combat_start = False
combat_ready = False
frame = 0
meursault_movement_stopped_frame = 0
meursault_coin_side_rolls = []
trash_crab_coin_side_rolls = []
coinY = 50
meursault_coinX = 200

# Clicking on the appropriate skill would have that skill be used, and the associated animation if the attack hits.

# Pygame loop
while run:
    pygame.time.Clock().tick(120)
    for event in pygame.event.get():  # User did something
        # Mouse hover-over detection with Meursault's skills
        # first element is s1, second is s2, third is s3
        meursault_skill_description_render = [False, False, False]

        if combat_start is False:
            if meursault_s1.rect.collidepoint(pygame.mouse.get_pos()):
                meursault_skill_description_render[0] = True
                meursault_selected_skill_attributes = meursault_skills_attributes[0]

            elif meursault_s2.rect.collidepoint(pygame.mouse.get_pos()):
                meursault_skill_description_render[1] = True
                meursault_selected_skill_attributes = meursault_skills_attributes[1]

            elif meursault_s3.rect.collidepoint(pygame.mouse.get_pos()):
                meursault_skill_description_render[2] = True
                meursault_selected_skill_attributes = meursault_skills_attributes[2]

        # Mouse hover-over detection with trash crab skills
        # first is gwah, second is gwaaah, third is shell tackle, fourth is foaming.
        trash_crab_skill_description_render = [False, False, False, False]

        if combat_start is False:
            if trash_crab_gwah.rect.collidepoint(pygame.mouse.get_pos()):
                trash_crab_skill_description_render[0] = True
                trash_crab_selected_skill_attributes = trash_crab_skills_attributes[0]

            elif trash_crab_gwaaah.rect.collidepoint(pygame.mouse.get_pos()):
                trash_crab_skill_description_render[1] = True
                trash_crab_selected_skill_attributes = trash_crab_skills_attributes[1]

            elif trash_crab_shell_tackle.rect.collidepoint(pygame.mouse.get_pos()):
                trash_crab_skill_description_render[2] = True
                trash_crab_selected_skill_attributes = trash_crab_skills_attributes[2]

            elif trash_crab_foaming.rect.collidepoint(pygame.mouse.get_pos()):
                trash_crab_skill_description_render[3] = True
                trash_crab_selected_skill_attributes = trash_crab_skills_attributes[3]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(len(meursault_skill_description_render)):
                    if meursault_skill_description_render[i] is True:
                        meursault_skill_clicked = True
                        meursault_skill_description_render_clicked = [False, False, False]
                        meursault_skill_description_render_clicked[i] = True

                for i in range(len(trash_crab_skill_description_render)):
                    if trash_crab_skill_description_render[i] is True:
                        trash_crab_skill_clicked = True
                        trash_crab_skill_description_render_clicked = [False, False, False, False]
                        trash_crab_skill_description_render_clicked[i] = True

                if combat_starter.rect.collidepoint(event.pos) and combat_ready is True:
                    combat_start = True
                    combat_ready = False
                    meursault.switch_image(1)
                    # clash_calculate(0, meursault_selected_skill_attributes, 0, trash_crab_selected_skill_attributes)

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((100, 100, 100))

    if meursault.rect.colliderect(trash_crab.rect):
        meursault.move("Left")
        meursault.switch_image(2)
        meursault_movement_stopped_frame = frame
        meursault_coin_side_rolls = heads_tails_rolls(0, meursault_skills_attributes[selected_meursault_skill][0])
        trash_crab_coin_side_rolls = heads_tails_rolls(0, trash_crab_skills_attributes[selected_trash_crab_skill][0])

    elif (combat_start is True and frame >= meursault_movement_stopped_frame + 40) or meursault.image_number == 1:
        meursault.move("Right")
        meursault.switch_image(1)

    screen.blit(meursault.image, meursault.rect)
    screen.blit(meursault_s1.image, meursault_s1.rect)
    screen.blit(meursault_s2.image, meursault_s2.rect)
    screen.blit(meursault_s3.image, meursault_s3.rect)

    screen.blit(trash_crab.image, trash_crab.rect)
    screen.blit(trash_crab_gwah.image, trash_crab_gwah.rect)
    screen.blit(trash_crab_gwaaah.image, trash_crab_gwaaah.rect)
    screen.blit(trash_crab_shell_tackle.image, trash_crab_shell_tackle.rect)
    screen.blit(trash_crab_foaming.image, trash_crab_foaming.rect)

    # Blitting for Meursault's skills
    if meursault_skill_clicked is True:
        for i in range(len(meursault_skill_description_render_clicked)):
            if meursault_skill_description_render_clicked[i] is True:
                screen.blit(pygame.image.load("Images/Meursault S" + str(i + 1) + " Description.png"), (200, 50))
                selected_meursault_skill = i

    else:
        for i in range(len(meursault_skill_description_render)):
            if meursault_skill_description_render[i] is True:
                screen.blit(pygame.image.load("Images/Meursault S" + str(i + 1) + " Description.png"), (200, 50))
                selected_meursault_skill = i

    # Blitting for trash crab's skills
    if trash_crab_skill_clicked is True:
        for i in range(len(trash_crab_skill_description_render_clicked)):
            if trash_crab_skill_description_render_clicked[i] is True:
                screen.blit(pygame.image.load("Images/Trash Crab S" + str(i + 1) + " Description.png"), (800, 50))
                selected_trash_crab_skill = i

    else:
        for i in range(len(trash_crab_skill_description_render)):
            if trash_crab_skill_description_render[i] is True:
                screen.blit(pygame.image.load("Images/Trash Crab S" + str(i + 1) + " Description.png"), (800, 50))
                selected_trash_crab_skill = i

    if (meursault_skill_clicked is True and trash_crab_skill_clicked is True) and combat_start is False:
        combat_ready = True
        screen.blit(combat_starter.image, combat_starter.rect)

    if combat_start is True:
        for i in range(len(meursault_coin_side_rolls)):
            if meursault_coin_side_rolls[i] == "Heads":
                screen.blit(coin_heads, (300 + 27 * i, coinY))

            elif meursault_coin_side_rolls[i] == "Tails":
                screen.blit(coin_tails, (300 + 27 * i, coinY))

        for i in range(len(trash_crab_coin_side_rolls)):
            if trash_crab_coin_side_rolls[i] == "Heads":
                screen.blit(coin_heads, (900 + 27 * i, coinY))

            elif trash_crab_coin_side_rolls[i] == "Tails":
                screen.blit(coin_tails, (900 + 27 * i, coinY))

    pygame.display.update()

    frame += 1

pygame.quit()
