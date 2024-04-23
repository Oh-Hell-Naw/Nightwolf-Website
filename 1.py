import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
Gravity = 0.5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer")

# Player properties
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_jump_speed = -15
player_on_ground = True

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
    if keys[pygame.K_LEFT] and player_x > 0:
        print(player_y)
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        print(player_y)
        player_x += player_speed
    if player_on_ground:
        if keys[pygame.K_UP] and player_y > 0:
            player_y = player_jump_speed
            print(player_y)
    if player_y + player_height > HEIGHT:
        player_y = HEIGHT - player_height
        player_on_ground = True

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
    pygame.draw.rect(screen, RED, (platform_x, platform_y, platform_width, platform_height))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()