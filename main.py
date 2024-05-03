import pygame
import random

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Calibri', 16)
pygame.display.set_caption("Limbus Company Clash Simulation")

size = (800, 450)
screen = pygame.display.set_mode(size)
screen.fill((100, 100, 100))
run = True

while run:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("a")
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    pygame.display.update()

pygame.quit()
