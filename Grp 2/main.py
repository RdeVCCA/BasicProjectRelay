# game idea
# 2-player puzzle solving game
# the 2 players are joined together by a string or something
# and then they solve some kind of puzzle

import pygame
# from players import Player
from obstacles import Obstacle
from line import Line
# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("people joined with chords")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up game loop
clock = pygame.time.Clock()
run = True

game = pygame.sprite.Group()

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

player1 = Player(1, 0, 0)
player2 = Player(2, 750, 0)
# Player settings
player_size = 50
player1_x = width // 2 - player_size // 2
player1_y = height // 2 - player_size // 2
player2_x = width // 2 - player_size // 2
player2_y = height // 2 - player_size // 2
player_speed = 5

game.add(player1)
game.add(player2)

# Create walls
wall1 = pygame.Rect(200, 150, width, height)
wall2 = pygame.Rect(400, 300, width, height)
walls = [wall1, wall2]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False

    keys = pygame.key.get_pressed()

    # Initialize the next positions to the current positions
    next_player1_x = player1.x
    next_player1_y = player1.y
    next_player2_x = player2.x
    next_player2_y = player2.y

    if player1.playerNumber == 1:  # WASD controls for player 1
        if keys[pygame.K_w]:
            next_player1_y -= player1.speed
        if keys[pygame.K_s]:
            next_player1_y += player1.speed
        if keys[pygame.K_a]:
            next_player1_x -= player1.speed
        if keys[pygame.K_d]:
            next_player1_x += player1.speed
    if player2.playerNumber == 2:  # Arrow keys for player 2
        if keys[pygame.K_UP]:
            next_player2_y -= player2.speed
        if keys[pygame.K_DOWN]:
            next_player2_y += player2.speed
        if keys[pygame.K_LEFT]:
            next_player2_x -= player2.speed
        if keys[pygame.K_RIGHT]:
            next_player2_x += player2.speed

    # Create Rect objects for the next position of the players
    next_player1_rect = pygame.Rect(next_player1_x, next_player1_y, player_size, player_size)
    next_player2_rect = pygame.Rect(next_player2_x, next_player2_y, player_size, player_size)

    # Check for collision with the walls
    player1_collision = False
    player2_collision = False
    for wall in walls:
        if next_player1_rect.colliderect(wall):
            player1_collision = True
        if next_player2_rect.colliderect(wall):
            player2_collision = True

    # If no collision would occur, move the player
    if not player1_collision:
        player1.x = next_player1_x
        player1.y = next_player1_y
    if not player2_collision:
        player2.x = next_player2_x
        player2.y = next_player2_y

    player1.rect.x = player1.x
    player1.rect.y = player1.y
    player2.rect.x = player2.x
    player2.rect.y = player2.y

    # Check for collision between the players
    if player1.rect.colliderect(player2.rect):
        run = False

    # Clear the screen
    screen.fill(white)

    # Draw objects or perform additional rendering
    game.draw(screen)
    game.update()

    for wall in walls:
        pygame.draw.rect(screen, black, wall)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

# if you have time create some levels
# please get a deeeck drawing to be connecting the 2 players