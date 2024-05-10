import pygame


class TrashCrabSkill:

    def __init__(self, x, y, skill):
        self.x = x
        self.y = y
        self.skill_used = "Trash Crab " + skill + ".png"

        self.image = pygame.image.load(self.skill_used)

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])