# game idea
# 2-player puzzle solving game
# the 2 players are joined together by a string or something
# and then they solve some kind of puzzle
import pygame
from players import Player

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

game = pygame.sprite.Group();

player1 = Player(1, 0, 0);
player2 = Player(2, 750, 0);

game.add(player1);
game.add(player2)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False

    keys = pygame.key.get_pressed();
    
    player1.movement(keys);
    player2.movement(keys);

    # Clear the screen
    screen.fill(white)

    # Draw objects or perform additional rendering
    game.draw(screen);
    game.update();

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
=======
# if you have time create some levels
# please get a deeeck drawing to be connecting the 2 players

import pygame
from obstacles import Obstacle
from players import Player
from line import Line

pygame.init()
# Sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# put your assets 

# Create player instances and add them to the sprite group
player1 = Player(1, 100, 300)
player2 = Player(2, 700, 300)
all_sprites.add(player1, player2)

# Create obstacles and add them to both all_sprites and obstacles groups
obstacle1 = Obstacle(200, 200, 50, 50)
obstacle2 = Obstacle(400, 300, 100, 50)
all_sprites.add(obstacle1, obstacle2)
obstacles.add(obstacle1, obstacle2)


# Create the line connecting players
connecting_line = Line(player1, player2)
all_sprites.add(connecting_line)

running = True

# Main game loop
while running:
    # ... (event loop)

    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    # Update the game display and fill the screen with a color
    screen.fill((255, 255, 255))
    
    # Draw the line connecting the two players
    pygame.draw.line(screen, (0, 0, 0), player1.rect.center, player2.rect.center, 5)

    # Draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()
