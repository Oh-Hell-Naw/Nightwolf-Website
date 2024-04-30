import pygame
import math

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
JUMP_FORCE = -15

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size - 50]
player_vel = [0, 0]

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
    if keys[pygame.K_LEFT]:
        player_vel[0] = -5
    elif keys[pygame.K_RIGHT]:
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

    # Draw / render
    screen.fill((135, 206, 250))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_pos[0], player_pos[1], player_size, player_size))
    pygame.display.flip()

pygame.quit()