import pygame
import math
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_FORCE = -15

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)
SKY = (135, 206, 250)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size - 50]
player_vel = [0, 0]

# Platform properties
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 100
platform_speed = 2


# Game loop
running = True
while running:
    # Keep the loop running at the right speed
    clock.tick(FPS)
    
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_vel[0] = -5
    elif keys[pygame.K_d]:
        player_vel[0] = 5
    else:
        player_vel[0] = 0

    if keys[pygame.K_SPACE] and player_vel[1] == 0:
        player_vel[1] = JUMP_FORCE

    player_vel[1] += GRAVITY
    player_pos[1] += player_vel[1]
    player_pos[0] += player_vel[0]

    # Check for collision with the ground
    if player_pos[1] + player_size > HEIGHT:
        player_pos[1] = HEIGHT - player_size
        player_vel[1] = 0

        # update platform
    platform_x += platform_speed
    if platform_x + platform_width > WIDTH:
        platform_x = 0
    # Clear the screen
    screen.fill((SKY))

    # Draw platforms
    pygame.draw.rect(screen, GREEN, (platform_x, platform_y, platform_width, platform_height))
    
    

    # Draw / render
    
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()

pygame.quit()