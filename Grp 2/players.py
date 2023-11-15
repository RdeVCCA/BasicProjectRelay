import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, no, start_x, start_y):
        super().__init__();
        self.speed = 10
        self.width = 50;
        self.height = 50;
        self.playerNumber = no
        self.x = start_x
        self.y = start_y
        self.image = pygame.Surface((self.width, self.height));
        self.rect = self.image.get_rect();
        self.rect.x = self.x;
        self.rect.y = self.y;

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
                
    