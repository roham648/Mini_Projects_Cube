import pygame
import random
import sys
import time

pygame.init()

# --- Screen and Grid Settings ---
CELL_SIZE = 30
GRID_WIDTH = 20
GRID_HEIGHT = 10

WIDTH = GRID_WIDTH * CELL_SIZE
HEIGHT = GRID_HEIGHT * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Grid Mode")

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
EYE_COLOR = (255, 255, 0)
GRID_LINE_COLOR = (50, 50, 50)

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_LINE_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_LINE_COLOR, (0, y), (WIDTH, y))

def draw_snake(snake_list, dx, dy):
    for i, (x, y) in enumerate(snake_list):
        color = GREEN
        if i == len(snake_list) - 1: # Snake head
            pygame.draw.rect(screen, color, [x, y, CELL_SIZE, CELL_SIZE])
            # --- Draw Eye on Snake Head ---
            eye_radius = CELL_SIZE // 6
            eye_offset_x = CELL_SIZE // 4
            eye_offset_y = CELL_SIZE // 4

            if dx > 0: # Moving Right
                eye_x = x + CELL_SIZE - eye_offset_x
                eye_y = y + eye_offset_y
            elif dx < 0: # Moving Left
                eye_x = x + eye_offset_x
                eye_y = y + eye_offset_y
            elif dy > 0: # Moving Down
                eye_x = x + eye_offset_x
                eye_y = y + CELL_SIZE - eye_offset_x
            else: # Moving Up (dy < 0)
                eye_x = x + eye_offset_x
                eye_y = y + eye_offset_y
            
            pygame.draw.circle(screen, EYE_COLOR, (int(eye_x), int(eye_y)), eye_radius)
            # ----------------------------
        else:
            pygame.draw.rect(screen, color, [x, y, CELL_SIZE, CELL_SIZE])

def message(text, color, x, y):
    msg = font.render(text, True, color)
    screen.blit(msg, (x, y))

def game_loop():
    x = (GRID_WIDTH // 2) * CELL_SIZE
    y = (GRID_HEIGHT // 2) * CELL_SIZE

    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, GRID_WIDTH) * CELL_SIZE
    food_y = random.randrange(0, GRID_HEIGHT) * CELL_SIZE

    game_over = False
    timer_duration = 30 # seconds
    start_time = time.time()
    current_time = timer_duration

    # --- New: Auto-restart timer set to 1 second ---
    AUTO_RESTART_DELAY = 1 # seconds after game over
    auto_restart_time = None
    # --------------------------------------------

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and dx == 0:
                        dx = -CELL_SIZE
                        dy = 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx = CELL_SIZE
                        dy = 0
                    elif event.key == pygame.K_UP and dy == 0:
                        dy = -CELL_SIZE
                        dx = 0
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dy = CELL_SIZE
                        dx = 0

        if game_over:
            if auto_restart_time is None:
                auto_restart_time = time.time()

            screen.fill(BLACK)
            message("Game Over!", RED, WIDTH // 3, HEIGHT // 3)
            message(f"Final Score: {snake_length - 1}", WHITE, WIDTH // 3, HEIGHT // 2)
            
            remaining_restart_time = AUTO_RESTART_DELAY - int(time.time() - auto_restart_time)
            if remaining_restart_time > 0:
                message(f"Restarting in {remaining_restart_time}...", WHITE, 50, HEIGHT // 2 + 30)
            else:
                message("Restarting...", WHITE, 50, HEIGHT // 2 + 30)
                pygame.display.update()
                time.sleep(0.5) # Shorter pause before restart
                game_loop() 

            pygame.display.update()
            continue 

        elapsed_time = time.time() - start_time
        current_time = timer_duration - int(elapsed_time)

        if current_time <= 0:
            game_over = True
            continue 

        x += dx
        y += dy

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True
            continue

        screen.fill(BLACK)
        draw_grid()

        pygame.draw.rect(screen, RED, [food_x, food_y, CELL_SIZE, CELL_SIZE])

        snake_list.append([x, y])

        if len(snake_list) > snake_length:
            del snake_list[0] 

        for i, block in enumerate(snake_list[:-1]):
            if block == [x, y]:
                game_over = True
                break 

        if game_over:
            continue

        draw_snake(snake_list, dx, dy)

        message(f"Time: {current_time}", BLUE, WIDTH - 150, 10)
        message(f"Score: {snake_length - 1}", WHITE, 10, 10)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, GRID_WIDTH) * CELL_SIZE
            food_y = random.randrange(0, GRID_HEIGHT) * CELL_SIZE
            snake_length += 1
            start_time = time.time()
            current_time = timer_duration

        clock.tick(7) # Slower speed

# --- Initial call to start the game ---
game_loop()
