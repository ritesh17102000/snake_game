import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Title of the game
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake block size
block_size = 10

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Font for displaying score
font_style = pygame.font.SysFont(None, 30)

# Function to display score on the screen
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Function to display message on the screen
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, block_size, block_size])

# Function to start the game
def game_loop():
    game_over = False
    game_close = False

    # Initial snake position and length
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    # Food coordinates
    foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0

    # Game loop
    while not game_over:
        while game_close == True:
            # Display game over message and options
            screen.fill(black)
            display_message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Event handling for game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling during gameplay
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundary checks
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        # Update snake's position
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        # Snake's body logic
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake and food
        draw_snake(block_size, snake_list)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # Display score
        display_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
            snake_length += 1

        # Control the game speed
        clock.tick(15)

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game
game_loop()