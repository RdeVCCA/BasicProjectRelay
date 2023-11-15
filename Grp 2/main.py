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
