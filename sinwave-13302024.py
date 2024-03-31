
import pygame
from pygame.locals import *
pygame.init()

xs,ys=600,800
screen=pygame.display.set_mode((xs,ys))
pygame.display.set_caption('Sounds by sine')

player_images=[
    pygame.image.load("waves.png"),
    pygame.image.load("waves.png"),
    pygame.image.load("waves.png"),
    pygame.image.load("waves.png"),
]

current_frame = 0
frame_count = len(player_images)
animation_speed = 5  # Lower values increase animation speed

# Set up the player character
player_width, player_height = 10, 10
player_x, player_y = xs // 2, ys // 2
player_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[K_a] and player_x > 0:
        player_x -= player_speed
        pygame.mixer.music.load("200.wav")
        pygame.mixer.music.set_volume(0.7)  # Set volume (optional)
        pygame.mixer.music.play()
    if keys[K_d] and player_x < xs - player_width:
        player_x += player_speed
        pygame.mixer.music.load("210.wav")
        pygame.mixer.music.set_volume(0.7)  # Set volume (optional)
        pygame.mixer.music.play()
    if keys[K_s] and player_y > 0:
        player_y -= player_speed
        pygame.mixer.music.load("220.wav")
        pygame.mixer.music.set_volume(0.7)  # Set volume (optional)
        pygame.mixer.music.play()
    if keys[K_w] and player_y < ys - player_height:
        player_y += player_speed
        pygame.mixer.music.load("230.wav")
        pygame.mixer.music.set_volume(0.7)  # Set volume (optional)
        pygame.mixer.music.play()

    # Update animation frame
    current_frame = (current_frame + 1) % frame_count

    # Render the game
    screen.fill((255, 255, 255))  # Fill the screen with black color
    screen.blit(player_images[current_frame], (player_x, player_y))  # Draw the player character
    pygame.display.flip()  # Update the screen

    clock.tick(animation_speed)
# Quit the game
pygame.quit()
