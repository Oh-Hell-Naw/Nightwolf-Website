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
BLUE = (0, 0, 255)

# Player properties
player_image = pygame.image.load('normal.png')
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5
player_jump_speed = -15
player_on_ground = True
player_y_velocity = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.jump_speed = -15
        self.on_ground = True
        self.y_velocity = 0

player = Player(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_image)

# Platform properties
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 100
platform_speed = 2

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

    keys = pygame.key.get_pressed()

    # Handle player movement
    if keys[pygame.K_a] and player.rect.x > 0:
        player.rect.x -= player.speed
    if keys[pygame.K_d] and player.rect.x < WIDTH - player.rect.width:
        player.rect.x += player.speed
    if keys[pygame.K_SPACE] and player.on_ground == True and player.y_velocity == 0:
        player.y_velocity = player.jump_speed

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

    # Draw player
    screen.blit(player.image, player.rect)

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