import pygame


class TrashCrabSkills:

    def __init__(self, x, y, skill):
        self.x = x
        self.y = y

        if skill == "Gwah":
            self.image = pygame.image.load("Trash Crab Gwah.png")
        elif skill == "Shell Tackle":
            self.image = pygame.image.load("Trash Crab Shell Tackle.png")
        elif skill == "Gwaaah":
            self.image = pygame.image.load("Trash Crab Gwaaah.png")
        elif skill == "Foaming":
            self.imamge = pygame.image.load("Trash Crab Foaming.png")

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])