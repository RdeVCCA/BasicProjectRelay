# game idea
# 2-player puzzle solving game
# the 2 players are joined together by a string or something
# and then they solve some kind of puzzle

import pygame
from obstacles import Obstacle
from players import Player


# Sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player instances and add them to the sprite group
player1 = Player(1, 100, 300)
player2 = Player(2, 700, 300)
all_sprites.add(player1, player2)

# Create obstacles and add them to both all_sprites and obstacles groups
obstacle1 = Obstacle(200, 200, 50, 50)
obstacle2 = Obstacle(400, 300, 100, 50)
all_sprites.add(obstacle1, obstacle2)
obstacles.add(obstacle1, obstacle2)

# Main game loop
while running:
    # ... (event loop)

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # Update the game display and fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()