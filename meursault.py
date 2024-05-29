import pygame


class Meursault:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_tuple = ("Meursault.png", "Meursault Moving.png", "Meursault Clash.png")
        self.image = pygame.image.load(self.image_tuple[0])

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def switch_image(self):
        image_number = 0

        if self.image_tuple[image_number] != "Meursault Moving.png":
            print("a")
            image_number = 1
        else:
            print("b")
            image_number = 0

        self.image = pygame.image.load(self.image_tuple[image_number])


