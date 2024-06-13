import pygame, sys, random
from pygame.math import Vector2

# Class to manage the snake's properties and behaviors
class SNAKE:
    def __init__(self):
        # Initialize the snake's body as a list of vectors and its initial direction
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        # Load images for different parts of the snake
        self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
        
        self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('graphics/body_bl.png').convert_alpha()
        
        # Load the sound effect for eating an apple
        self.sound = pygame.mixer.Sound('sound/crunch.wav')
        
    # Draw the snake on the screen
    def draw_snake(self):
        self.head_direction()
        self.tail_direction()
        
        for index, block in enumerate(self.body):
           x_pos = int(block.x * cell_size)
           y_pos = int(block.y * cell_size) 
           block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        
           if index == 0:
               screen.blit(self.head, block_rect)
           elif index == len(self.body) - 1:  
               screen.blit(self.tail, block_rect) 
           else:
               pre_block = self.body[index + 1] - block
               next_block =  self.body[index - 1] - block 
               if pre_block.x == next_block.x:
                   screen.blit(self.body_vertical, block_rect)
               elif pre_block.y == next_block.y:
                   screen.blit(self.body_horizontal, block_rect)  
               else:
                   if pre_block.x == -1 and next_block.y == -1 or pre_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                   elif pre_block.x == -1 and next_block.y == 1 or pre_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                   elif pre_block.x == 1 and next_block.y == -1 or pre_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                   elif pre_block.x == 1 and next_block.y == 1 or pre_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    # Play the sound effect when the snake eats an apple
    def play_sound(self):
        self.sound.play()               
    
    # Reset the snake to its initial state
    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

    # Update the direction of the snake's head
    def head_direction(self):
        head_relation = self.body[1] - self.body[0]    
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    # Update the direction of the snake's tail
    def tail_direction(self):
        tail_relation = self.body[-2] - self.body[-1]    
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

    # Move the snake in the current direction and possibly add a new block
    def move(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    # Set a flag to add a new block to the snake's body
    def add_block(self):
        self.new_block = True

# Class to manage the fruit properties and behaviors
class FRUIT:
    def __init__(self):
        self.randomize()
        
    # Draw the fruit on the screen
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
        
    # Randomize the fruit's position
    def randomize(self):
        self.x = random.randint(0, cell_num - 1)
        self.y = random.randint(0, cell_num - 1)
        self.pos = Vector2(self.x, self.y)

# Class to manage button properties and behaviors
class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # Update the button's appearance
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    # Check if the button is being clicked
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    # Change the button's color when hovered over
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

# Class to manage the main game properties and behaviors
class MAIN:
    def __init__(self):
        self.fruit = FRUIT()
        self.snake = SNAKE()
        
    # Update the game state
    def update(self):
        self.snake.move()
        self.collision()
        self.dead()
        
    # Draw all game elements on the screen
    def draw_elements(self):
        self.grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.score()
        
    # Handle collision detection between the snake and fruit
    def collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_sound()
           
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()   
           
    # Check if the snake is dead (hit the wall or itself)
    def dead(self):
        if not 0 <= self.snake.body[0].x < cell_num or not 0 <= self.snake.body[0].y < cell_num:
            self.game_over()
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
                
    # Handle the game over state
    def game_over(self):
        self.snake.reset()
        while True:
            screen.blit(BG, (0, 0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
                    
            MENU_TEXT = get_font(50).render("GAME OVER!", True, "#f50202")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))
            
            PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), 
                                text_input="PLAY AGAIN", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 500), 
                                text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
    
            screen.blit(MENU_TEXT, MENU_RECT)
    
            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        main()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()
            
    # Draw the grass background
    def grass(self):
        grass_color = (167,209,61)
        for row in range(cell_num):
            if row % 2 == 0:
                for col in range(cell_num):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_num):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
                        
    # Display the score on the screen
    def score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_num - 60)
        score_y = int(cell_size * cell_num - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

# Initialize pygame
pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
clock = pygame.time.Clock()
apple = pygame.image.load('graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('font/PoetsenOne-Regular.ttf', 25)
BG = pygame.image.load("assets/Background.png")

# Function to get font for rendering text
def get_font(size):
    return pygame.font.Font("font/font.ttf", size)

# Main function to run the game
def main():
    main_game = MAIN()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        screen.fill((175,215,70))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(60)

# Entry point of the script
if __name__ == '__main__':
    main()
