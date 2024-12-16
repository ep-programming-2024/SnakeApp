import pygame
import random
import sys

class SnakeGame:
    def __init__(self, width=640, height=480, grid_size=20):
        """
        Initialize the Snake Game with customizable parameters
        
        Args:
            width (int): Width of the game window
            height (int): Height of the game window
            grid_size (int): Size of each grid square
        """
        pygame.init()
        
        # Game window setup
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        
        # Clock for controlling game speed
        self.clock = pygame.time.Clock()
        
        # Game state variables
        self.snake = [(width // 2, height // 2)]
        self.food = self.generate_food()
        self.direction = (grid_size, 0)
        self.score = 0
        
        # Font for displaying score
        self.font = pygame.font.Font(None, 36)
    
    def generate_food(self):
        """
        Generate food at a random location within the grid
        
        Returns:
            tuple: (x, y) coordinates of food
        """
        while True:
            x = random.randrange(0, self.width, self.grid_size)
            y = random.randrange(0, self.height, self.grid_size)
            food_pos = (x, y)
            
            if food_pos not in self.snake:
                return food_pos
    
    def draw_grid(self):
        """
        Draw grid lines to help students understand grid-based movement
        """
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.height))
        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (self.width, y))
    
    def run(self):
        """
        Main game loop with core game mechanics
        """
        game_over = False
        
        while not game_over:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                
                # Handle keyboard input for snake direction
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, self.grid_size):
                        self.direction = (0, -self.grid_size)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -self.grid_size):
                        self.direction = (0, self.grid_size)
                    elif event.key == pygame.K_LEFT and self.direction != (self.grid_size, 0):
                        self.direction = (-self.grid_size, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-self.grid_size, 0):
                        self.direction = (self.grid_size, 0)
            
            # Calculate new snake head position
            new_head = (
                self.snake[0][0] + self.direction[0],
                self.snake[0][1] + self.direction[1]
            )
            
            # Game over conditions
            if (
                new_head[0] < 0 or new_head[0] >= self.width or
                new_head[1] < 0 or new_head[1] >= self.height or
                new_head in self.snake
            ):
                game_over = True
            
            # Add new head to snake
            self.snake.insert(0, new_head)
            
            # Check if snake ate food
            if self.snake[0] == self.food:
                self.score += 1
                self.food = self.generate_food()
            else:
                # Remove tail if food not eaten
                self.snake.pop()
            
            # Drawing
            self.screen.fill(self.BLACK)
            self.draw_grid()
            
            # Draw snake
            for segment in self.snake:
                pygame.draw.rect(self.screen, self.GREEN, 
                                 (*segment, self.grid_size, self.grid_size))
            
            # Draw food
            pygame.draw.rect(self.screen, self.RED, 
                             (*self.food, self.grid_size, self.grid_size))
            
            # Display score
            score_text = self.font.render(f'Score: {self.score}', True, self.WHITE)
            self.screen.blit(score_text, (10, 10))
            
            pygame.display.flip()
            self.clock.tick(10)  # Control game speed
        
        # Game over screen
        self.screen.fill(self.BLACK)
        game_over_text = self.font.render(f'Game Over! Score: {self.score}', True, self.WHITE)
        text_rect = game_over_text.get_rect(center=(self.width//2, self.height//2))
        self.screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        
        # Wait before closing
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

def main():
    """
    Entry point for the Snake Game
    """
    game = SnakeGame(width=800, height=600, grid_size=25)
    game.run()

if __name__ == "__main__":
    main()
