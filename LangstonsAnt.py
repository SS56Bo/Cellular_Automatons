import pygame
import sys

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 1440, 720
CELL_SIZE = 10
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Langton\'s Ant')

# Grid initialization
grid = [[WHITE for _ in range(COLS)] for _ in range(ROWS)]

# Ant class
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0  # 0: up, 1: right, 2: down, 3: left
        self.steps = 0

    def move(self):
        # Turn and flip color
        if grid[self.y][self.x] == WHITE:
            self.direction = (self.direction + 1) % 4
            grid[self.y][self.x] = BLACK
        else:
            self.direction = (self.direction - 1) % 4
            grid[self.y][self.x] = WHITE

        # Move forward
        if self.direction == 0:
            self.y = (self.y - 1) % ROWS
        elif self.direction == 1:
            self.x = (self.x + 1) % COLS
        elif self.direction == 2:
            self.y = (self.y + 1) % ROWS
        elif self.direction == 3:
            self.x = (self.x - 1) % COLS

        # Increment step count
        self.steps += 1

        # Update window caption
        pygame.display.set_caption(f'Langton\'s Ant - Steps: {self.steps}')

# Initialize ant
ant = Ant(COLS // 2, ROWS // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ant
    ant.move()

    # Draw grid
    for y in range(ROWS):
        for x in range(COLS):
            color = grid[y][x]
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
