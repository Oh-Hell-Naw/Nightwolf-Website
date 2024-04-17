import pygame # type: ignore
import sys
import os 

# Initialize Pygame
pygame.init()

# Constants
FPS = 60
Gravity = 0.5
WIDTH = 800
HEIGHT = 600

# Set the video mode
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Load player image
#player_image = pygame.image.load(os.path.join('C:\projekt Informatik\graphics\png\idle\normal.png'))
#player_image = player_image.convert()
pygame.display.set_caption("Jump and Run")

# Player properties
player_width = 50 #player_image.get_width()
player_height = 50 #player_image.get_height()
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_jump_speed = -15
player_on_ground = True
player_y_velocity = 0

# Platform properties
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 100
platform_speed = 2

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed # könnt print(player_x) in den code rein machen wenn ihr die x koordinate sehen wollt oder statt x dann y  
    if keys[pygame.K_d] and player_x < WIDTH - player_width:
        player_x += player_speed
    if player_on_ground:
        if keys[pygame.K_SPACE]:
            player_y_velocity = player_jump_speed
            player_on_ground = False
    if player_y + player_height > HEIGHT:
        player_y = HEIGHT - player_height
        player_on_ground = True
    player_y_velocity += Gravity
    player_y += player_y_velocity
    if player_on_ground:
        player_y_velocity = 0 

    # Move platforms
    platform_x += platform_speed
    if platform_x + platform_width > WIDTH:
        platform_x = 0

    # Collision detection
    if player_y + player_height > platform_y and player_y + player_height < platform_y + platform_height and player_x < platform_x + platform_width and player_x + player_width > platform_x:
        player_on_ground = True
        player_y = platform_y - player_height

    # Clear the screen
    screen.fill(WHITE)

    # Draw platforms
    pygame.draw.rect(screen, GREEN, (platform_x, platform_y, platform_width, platform_height))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
os.exit()