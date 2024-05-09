import pygame


class MeursaultSkill:

    def __init__(self, x, y, skill):
        self.x = x
        self.y = y

        if skill == "S1":
            self.image = pygame.image.load("Meursault S1.png")
        elif skill == "S2":
            self.image = pygame.image.load("Meursault S2.png")
        elif skill == "S3":
            self.image = pygame.image.load("Meursault S3.png")

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
