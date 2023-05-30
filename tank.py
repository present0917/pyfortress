import pygame

class tank:
    def __init__(self, img_path, scale): #초기화
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, scale)
        self.mask = pygame.mask.from_surface(self.img)