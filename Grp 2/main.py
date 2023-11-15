# game idea
# 2-player puzzle solving game
# the 2 players are joined together by a string or something
# and then they solve some kind of puzzle
import pygame
from Player import Player

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

player = Player()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False

    # Game logic goes here


    # Clear the screen
    screen.fill(white)

    # Draw objects or perform additional rendering
    game.draw(screen);

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
