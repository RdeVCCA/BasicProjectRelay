import pygame

class Line(pygame.sprite.Sprite):
    def __init__(self, start_sprite, end_sprite, width=5, color=(0, 0, 0)):
        super().__init__()
        self.start_sprite = start_sprite
        self.end_sprite = end_sprite
        self.width = width
        self.color = color
        self.image = pygame.Surface((0, 0))  # Placeholder surface
        self.rect = self.image.get_rect()

    def update(self):
        # Calculate the line's rect
        start_pos = self.start_sprite.rect.center
        end_pos = self.end_sprite.rect.center
        x = min(start_pos[0], end_pos[0])
        y = min(start_pos[1], end_pos[1])
        width = max(start_pos[0], end_pos[0]) - x
        height = max(start_pos[1], end_pos[1]) - y

        # Update the line's rect size and position
        self.rect.update(x, y, width, height)

    def draw(self, screen):
        # Draw the line (this does not use the rect)
        pygame.draw.line(screen, self.color, self.start_sprite.rect.center, self.end_sprite.rect.center, self.width)
