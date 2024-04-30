import pygame
import sys
import math
import random

# Constants
FPS = 60
WIDTH = 800
HEIGHT = 600
GRAVITY = 0.5
JUMP_FORCE = -15

# Game state
game_over = False

# Set the video mode
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE | pygame.DOUBLEBUF)
pygame.display.set_caption("Jump and Run")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)

# Player properties

player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size - 50]
player_vel = [0, 0]

# Platform properties
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 100
platform_speed = 2

# Sword properties
#sword_width = 20
#sword_height = 50
#sword_x = player_x + player_width // 2 - sword_width // 2
#sword_y = player_y - sword_height
#sword_speed = 10

# Enemy properties
#enemy_width = 50
#enemy_height = 50
#enemies = [
#    {"x": WIDTH - enemy_width, "y": HEIGHT - enemy_height - 100, "speed": -2, "direction": "left"},
    # Add more enemies here
#]

# Scoring
score = 0

# Game loop
clock = pygame.time.Clock()
running = True
while running:

    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         elif event.type == pygame.VIDEORESIZE:
            WIDTH = event.w
            HEIGHT = event.h
            
    # Handle player movement
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

    # Update sword position
    #sword_x = player_x + player_width // 2 - sword_width // 2
    #sword_y = player_y - sword_height

    # Collision detection between sword and enemies
    #for enemy in enemies:
        #if sword_y + sword_height > enemy["y"] and sword_y < enemy["y"] + enemy_height and sword_x < enemy["x"] + enemy_width and sword_x + sword_width > enemy["x"]:
            #enemies.remove(enemy)
            

    # Collision detection between enemies and player
    #for enemy in enemies:
        #if player_y + player_height > enemy["y"] and player_y < enemy["y"] + enemy_height and player_x < enemy["x"] + enemy_width and player_x + player_width > enemy["x"]:
            #game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw platforms
    pygame.draw.rect(screen, GREEN, (platform_x, platform_y, platform_width, platform_height))

    # Draw enemies
    #for enemy in enemies:
        #pygame.draw.rect(screen, RED, (enemy["x"], enemy["y"], enemy_width, enemy_height))

    # Draw sword
    #pygame.draw.rect(screen, BLUE, (sword_x, sword_y, sword_width, sword_height))

    # Draw player
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(player_pos[0], player_pos[1], player_size, player_size))
    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

    

# Quit the game
pygame.quit()
sys.exit()
os.exit()