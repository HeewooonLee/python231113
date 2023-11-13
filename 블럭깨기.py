# 블럭깨기.py

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 400, 10
BALL_RADIUS = 15
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30
BLOCK_ROWS = 5
BLOCK_COLS = 10
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [5, 5]

# Blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * (BLOCK_WIDTH + 5) + 5, row * (BLOCK_HEIGHT + 5) + 5, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 8

    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions
    if ball.colliderect(paddle):
        ball_speed[1] = -abs(ball_speed[1])

    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = abs(ball_speed[1])

    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = abs(ball_speed[1])

    # Game over if the ball goes below the paddle
    if ball.bottom >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    for block in blocks:
        pygame.draw.rect(screen, RED, block)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
