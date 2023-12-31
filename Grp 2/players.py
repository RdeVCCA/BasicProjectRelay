import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, no, start_x, start_y):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.1), int(self.image.get_height() * 0.1)))
        
        self.rect = self.image.get_rect()
        self.speed = 10
        self.playerNumber = no
        self.x = start_x
        self.y = start_y

    def movement(self, keys):
        if self.playerNumber == 1:  # WASD controls for player 1
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
        elif self.playerNumber == 2:  # Arrow keys for player 2
            if keys[pygame.K_UP]:
                self.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.y += self.speed
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
                
    