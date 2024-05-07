import pygame
import random

# Setting up fonts
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Calibri', 16)
pygame.display.set_caption("Limbus Company Clash Simulation")

# Setting up the window
size = (800, 450)
screen = pygame.display.set_mode(size)
screen.fill((100, 100, 100))
run = True


# Functions used in the pygame loop
# Takes 2 integers as parameters & calculates which side of the coin was rolled
def coin_rolls(coins, sanity):
    coin_side_roll = []

    for i in range(coins):
        if random.randint(1, 100) <= 50 + sanity:
            coin_side_roll.append("Heads")
        else:
            coin_side_roll.append("Tails")

    return coin_side_roll


# Takes a tuple and 2 integers as parameters & calculates the attack's power
def add_coin_power(coin_side_list, coin_power, base_power):
    current_attack_power = base_power
    attack_rolls = []

    for i in range(len(coin_side_list)):
        if coin_side_list[i] == "Heads":
            current_attack_power += coin_power

        attack_rolls.append(current_attack_power)

    return attack_rolls


# takes 8 integer parameters, with each side of the clash having 4 parameters
def clash_calculate(ally_coins, ally_coin_power, ally_base_power, ally_sanity,
                    enemy_coins, enemy_coin_power, enemy_base_power, enemy_sanity):

    while ally_coins != 0 and enemy_coins != 0:
        ally_coin_rolls = coin_rolls(ally_coins, ally_sanity)
        enemy_coin_rolls = coin_rolls(enemy_coins, enemy_sanity)

        ally_attack_rolls = add_coin_power(ally_coin_rolls, ally_coin_power, ally_base_power)
        enemy_attack_rolls = add_coin_power(enemy_coin_rolls, enemy_coin_power, enemy_base_power)

        if ally_attack_rolls[ally_coins - 1] > enemy_attack_rolls[enemy_coins - 1]:
            print("Ally clash win. ")
            enemy_coins -= 1

        if ally_attack_rolls[ally_coins - 1] < enemy_attack_rolls[enemy_coins - 1]:
            print("Enemy clash win. ")
            ally_coins -= 1

        if ally_attack_rolls[ally_coins - 1] == enemy_attack_rolls[enemy_coins - 1]:
            print("Tie. ")

        print("Ally Attack roll: ", ally_attack_rolls)
        print("Enemy Attack roll: ", enemy_attack_rolls)
        print()

    if ally_coins == 0:
        print("Enemy's attack goes through.")
    else:
        print("Ally's attack goes through. ")


clash_calculate(3, 4, 4, 0, 4, 3, 4, 0)

# Pygame loop
while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("a")

        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    pygame.display.update()

pygame.quit()
