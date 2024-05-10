import pygame
import random
from meursault_skills import MeursaultSkill
from trash_crab_skills import TrashCrabSkill

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
# Takes 4 integers as parameters. The first two generate which side of the coin was rolled.
# The next two generate what power the coins rolled should have.
def coin_rolls(coins, sanity, coin_power, base_power):
    coin_side_roll = []

    for i in range(coins):
        if random.randint(1, 100) <= 50 + sanity:
            coin_side_roll.append("Heads")
        else:
            coin_side_roll.append("Tails")

    attack_rolls = []
    current_attack_power = base_power

    for i in range(len(coin_side_roll)):
        if coin_side_roll[i] == "Heads":
            current_attack_power += coin_power

        attack_rolls.append(current_attack_power)

    return attack_rolls


# takes 8 integer parameters, with each side of the clash having 4 parameters
# Print statements currently here to see if the function works (It does)
def clash_calculate(ally_coins, ally_coin_power, ally_base_power, ally_sanity,
                    enemy_coins, enemy_coin_power, enemy_base_power, enemy_sanity):
    damage_dealt = 0

    while ally_coins != 0 and enemy_coins != 0:
        ally_attack_rolls = coin_rolls(ally_coins, ally_sanity, ally_coin_power, ally_base_power)
        enemy_attack_rolls = coin_rolls(enemy_coins, enemy_sanity, enemy_coin_power, enemy_base_power)

        print("Ally Attack roll:", ally_attack_rolls[ally_coins - 1])
        print("Enemy Attack roll:", enemy_attack_rolls[enemy_coins - 1])

        if ally_attack_rolls[ally_coins - 1] > enemy_attack_rolls[enemy_coins - 1]:
            print("Ally clash win. ")
            enemy_coins -= 1

        if ally_attack_rolls[ally_coins - 1] < enemy_attack_rolls[enemy_coins - 1]:
            print("Enemy clash win. ")
            ally_coins -= 1

        if ally_attack_rolls[ally_coins - 1] == enemy_attack_rolls[enemy_coins - 1]:
            print("Tie. ")

        print()

    # Regenerates the coin rolls
    if ally_coins == 0:
        enemy_attack_rolls = coin_rolls(enemy_coins, enemy_sanity, enemy_coin_power, enemy_base_power)
        print("Enemy's attack goes through.")

        for i in range(len(enemy_attack_rolls)):
            damage_dealt += enemy_attack_rolls[i]
            print("Enemy did", damage_dealt, "damage")

    else:
        ally_attack_rolls = coin_rolls(ally_coins, ally_sanity, ally_coin_power, ally_base_power)
        print("Ally's attack goes through. ")

        for i in range(len(ally_attack_rolls)):
            damage_dealt += ally_attack_rolls[i]
            print("Ally did", damage_dealt, "damage.")


meursault = pygame.image.load("Meursault.png")
meursault_s1 = MeursaultSkill(25, 25, "S1")
meursault_s2 = MeursaultSkill(25, 285, "S2")
meursault_s3 = MeursaultSkill(25, 545, "S3")

trash_crab = pygame.image.load("Trash Crab.png")
trash_crab_gwah = TrashCrabSkill(1075, 20, "Gwah")
trash_crab_gwaaah = TrashCrabSkill(1075, 195, "Gwaaah")
trash_crab_shell_tackle = TrashCrabSkill(1075, 370, "Shell Tackle")
trash_crab_foaming = TrashCrabSkill(1075, 545, "Foaming")

# Plan: Have Meursault's three skills to the left of him, and the trash cab's skills to the right of it.
# Clicking on the appropriate skill would have that skill be used, and the associated animation if the attack hits.

# Pygame loop
while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("a")

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(meursault, (150, 400))
    screen.blit(meursault_s1.image, meursault_s1.rect)
    screen.blit(meursault_s2.image, meursault_s2.rect)
    screen.blit(meursault_s3.image, meursault_s3.rect)

    screen.blit(trash_crab, (800, 450))
    screen.blit(trash_crab_gwah.image, trash_crab_gwah.rect)
    screen.blit(trash_crab_gwaaah.image, trash_crab_gwaaah.rect)
    screen.blit(trash_crab_shell_tackle.image, trash_crab_shell_tackle.rect)
    screen.blit(trash_crab_foaming.image, trash_crab_foaming.rect)

    pygame.display.update()

pygame.quit()
