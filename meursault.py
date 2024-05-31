import pygame


class Meursault:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_tuple = ("Meursault.png", "Meursault Moving.png", "Meursault Clash.png")
        self.image = pygame.image.load(self.image_tuple[0])
        self.image_number = 0
        self.delta = 1

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        if self.image_number == 0:
            self.image_number = 1

        elif self.image_number == 1:
            self.image_number = 0

        self.image = pygame.image.load(self.image_tuple[self.image_number])

    def move(self, direction, ):
        if self.image_number == 1 and direction == "Right":
            self.x += self.delta

        elif direction == "Left":
            self.x -= 125 * self.delta

        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
