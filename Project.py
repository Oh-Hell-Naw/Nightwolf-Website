import pygame
import sys

# Constants
FPS = 60
Gravity = 0.5
WIDTH = 800
HEIGHT = 600

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
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_jump_speed = -15
player_on_ground = True
player_y_velocity = -15

# Platform properties
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 100
platform_speed = 2

# Sword properties
sword_width = 15
sword_height = 45
sword_x = player_x + player_width // 2 - sword_width // 2
sword_y = player_y - sword_height
sword_speed = 10

# Enemy properties
enemy_width = 50
enemy_height = 50
enemies = [
    {"x": WIDTH - enemy_width, "y": HEIGHT - enemy_height - 100, "speed": -2, "direction": "left"},
    # Add more enemies here
]

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
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
        sword_x -= player_speed
    if keys[pygame.K_d] and player_x < WIDTH - player_width:
        player_x += player_speed
        sword_x += player_speed
    if keys[pygame.K_SPACE] and player_on_ground == True:
        print("Jumping!")
        player_y_velocity = player_jump_speed
    if player_x + player_width > WIDTH:
        player_x = 0    
    
    # update platform
    platform_x += platform_speed
    if platform_x + platform_width > WIDTH:
        platform_x = 0

    # Update sword position
    sword_x = player_x + player_width // 2 - sword_width // 2
    sword_y = player_y - sword_height

    # Collision detection between sword and enemies
    for enemy in enemies:
        if sword_y + sword_height > enemy["y"] and sword_y < enemy["y"] + enemy_height and sword_x < enemy["x"] + enemy_width and sword_x + sword_width > enemy["x"]:
            enemies.remove(enemy)
            score += 100

    # Collision detection between enemies and player
    for enemy in enemies:
        if player_y + player_height > enemy["y"] and player_y < enemy["y"] + enemy_height and player_x < enemy["x"] + enemy_width and player_x + player_width > enemy["x"]:
            game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw platforms
    pygame.draw.rect(screen, GREEN, (platform_x, platform_y, platform_width, platform_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy["x"], enemy["y"], enemy_width, enemy_height))

    # Draw sword
    pygame.draw.rect(screen, BLUE, (sword_x, sword_y, sword_width, sword_height))

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

    # Game over screen
    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! Your score: " + str(score), True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

# Quit the game
pygame.quit()
sys.exit()
os.exit()