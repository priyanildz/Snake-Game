import pygame
import sys
import random

# Initialize Pygame and must use it before any other Pygame functions
pygame.init()

# grid settings
CELL_SIZE = 25  # size of each cell in pixels
GRID_WIDTH = 40  # number of cells in the horizontal direction
GRID_HEIGHT = 30  # number of cells in the vertical direction

WIDTH = CELL_SIZE * GRID_WIDTH  # total width of the game window
HEIGHT = CELL_SIZE * GRID_HEIGHT  # total height of the game window

LINE_WIDTH = 1  # width of the grid lines in pixels

# Create a window of size WIDTH x HEIGHT pixels
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")  # Set the title of the window

snake = [
    (5, 5),
    (5, 6),
    (5, 7),
]  # Initial position of the snake (list of (x, y) tuples)

def random_food():
    while True:
        pos = (
            random.randint(0, GRID_WIDTH - 1),
            random.randint(0, GRID_HEIGHT - 1),
        )
        if pos not in snake:
            return pos

food = random_food()  # Initial position of the food (randomly generated)

# Colors
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
LIGHT_BLUE = (25, 25, 100)
DARK_BLUE = (25, 25, 112)
SNAKE_COLOR = (0, 200, 0)
HEAD_COLOR = (0, 255, 0)
EYE_COLOR = (255, 0, 0)
FOOD_COLOR = (255, 0, 0)

font = pygame.font.Font(None, 36) 


def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # Alternate colors for the grid cells
            if (row + col) % 2 == 0:
                color = LIGHT_BLUE
            else:
                color = DARK_BLUE

            rect = pygame.Rect(
                col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )  # Create a rectangle for each cell
            pygame.draw.rect(screen, color, rect)  # Draw the cell with the chosen color

    # this means start at 0 and go to WIDTH in steps of 20pixels i.e. CELL_SIZE, and do the same for HEIGHT
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen, BLACK, (x, 0), (x, HEIGHT), LINE_WIDTH
        )  # Draw vertical lines
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen, BLACK, (0, y), (WIDTH, y), LINE_WIDTH
        )  # Draw horizontal lines


def draw_snake():
    for i, segment in enumerate(snake):
        x, y = segment
        rect = pygame.Rect(
            x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )  # Create a rectangle for each snake segment
        color = (
            HEAD_COLOR if i == 0 else SNAKE_COLOR
        )  # Use HEAD_COLOR for the head and SNAKE_COLOR for the body

        pygame.draw.rect(screen, color, rect)  # Draw the snake segment


def draw_food():
    x, y = food
    rect = pygame.Rect(
        x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )  # Create a rectangle for the food
    pygame.draw.rect(screen, FOOD_COLOR, rect)  # Draw the food in red

direction = (0, -1)

clock = pygame.time.Clock()
FPS = 8

# this variable will be used to control the main loop of the game
running = True
while running:
    # Handle events (e.g., user input, window close)
    for event in pygame.event.get():

        # if the user clicks the close button on the window, we set running to False to exit the loop
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            # Handle key presses for snake movement
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)  # Move up
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)  # Move down
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)  # Move left
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)  # Move right
    # 2. Move snake
    head_x, head_y = snake[0]
    new_head = (
        head_x + direction[0],
        head_y + direction[1],
    )  # Calculate new head position
    if (
        new_head[0] < 0
        or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0
        or new_head[1] >= GRID_HEIGHT
        or new_head in snake
    ):
        running = False
    else:
        snake.insert(0, new_head)
        # Food logic
        if new_head == food:
            food = random_food()
        else:
            snake.pop()

    # Fill the screen with a color (e.g., black)
    screen.fill(BLACK)

    # Draw the grid
    draw_grid()

    # Draw the snake
    draw_snake()

    # Draw the food
    draw_food()

    score = len(snake) - 3  # initial snake length = 3
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    clock.tick(FPS)  # Control the frame rate (e.g., 10 frames per second)

pygame.quit()  # Quit Pygame when the main loop ends
sys.exit()  # Exit the program