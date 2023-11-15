import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 0, 0)):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
