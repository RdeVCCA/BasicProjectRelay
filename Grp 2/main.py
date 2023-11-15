# game idea
# 2-player puzzle solving game
# the 2 players are joined together by a string or something
# and then they solve some kind of puzzle

import pygame
from players import Player
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
    
    player1.movement(keys)
    player2.movement(keys)

    player1_rect = pygame.Rect(player1_x, player1_y, player_size, player_size)
    player2_rect = pygame.Rect(player2_x, player2_y, player_size, player_size)

    for wall in walls:
        if player1_rect.colliderect(wall):
            # Handle collision (you can adjust this part according to your game logic)
            if keys[pygame.K_LEFT] and player1_x + player_speed > wall.right:
                player1_x = wall.right
            if keys[pygame.K_RIGHT] and player1_x < wall.left - player_size:
                player1_x = wall.left - player_size
            if keys[pygame.K_UP] and player1_y + player_speed > wall.bottom:
                player1_y = wall.bottom
            if keys[pygame.K_DOWN] and player1_y < wall.top - player_size:
                player1_y = wall.top - player_size
        if player2_rect.colliderect(wall):
            # Handle collision (you can adjust this part according to your game logic)
            if keys[pygame.K_LEFT] and player2_x + player_speed > wall.right:
                player2_x = wall.right
            if keys[pygame.K_RIGHT] and player2_x < wall.left - player_size:
                player2_x = wall.left - player_size
            if keys[pygame.K_UP] and player2_y + player_speed > wall.bottom:
                player2_y = wall.bottom
            if keys[pygame.K_DOWN] and player2_y < wall.top - player_size:
                player2_y = wall.top - player_size

    # Clear the screen
    screen.fill(white)

    # Draw objects or perform additional rendering
    game.draw(screen)
    game.update()

    for wall in walls:
        pygame.draw.rect(screen, white, wall)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()

# if you have time create some levels
# please get a deeeck drawing to be connecting the 2 players