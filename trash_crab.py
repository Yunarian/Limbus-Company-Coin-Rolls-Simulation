import pygame

class TrashCrab:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Images/Trash Crab.png")
        self.image_number = 0

        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    # Need to get a trash crab move sprite
    # def switch_image(self):
    #     if self.image_number == 0:
    #         self.image_number = 1
    #
    #     elif self.image_number == 1:
    #         self.image_number = 0
    #
    #     self.image = pygame.image.load(self.image_tuple[self.image_number])
