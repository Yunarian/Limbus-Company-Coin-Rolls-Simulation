import pygame


class AttackSkill:

    def __init__(self, x, y, skill, skill_user):
        self.x = x
        self.y = y
        self.skill_used = "Images/" + skill_user + skill + ".png"

        self.image = pygame.image.load(self.skill_used)

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
