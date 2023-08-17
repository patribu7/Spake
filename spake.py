import pygame
from random import randrange

#colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 70)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
SPEED = 8
cell = 20
size_x = 500
size_y = 500
size = (size_x, size_y)
screen = pygame.display.set_mode((size_x + cell, size_y + cell))
pygame.display.set_caption('spake')

pygame.init()


class Snake:
    def __init__(self):
        self.x = 240
        self.y = 240
        
        self.longtail = 6

        self.moves = []
        for i in range(self.longtail):
            self.moves.append((self.x + cell*i, self.y))        

    def draw(self):  
        self.head = pygame.draw.rect(screen, GREEN, (self.x, self.y, cell, cell))
        self.tail = []
        for move in self.moves:
            self.tail.insert(0, pygame.draw.rect(screen, GREEN, (move, (cell, cell))))
    
    def get_direction(self):
        global direction
        
        for event in pygame.event.get():
        
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    direction = "up"
                                                                
                if event.key == pygame.K_DOWN:
                    direction = "down"
                    
                if event.key == pygame.K_LEFT:
                    direction = "left"
                                                
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                
        return direction


    def move(self, direction):
        if direction == "up":
            self.y -= cell
            
        if direction == "down":
            self.y += cell
            
        if direction == "left":
            self.x -= cell
            
        if direction == "right":
            self.x += cell
        
        #registro le mosse per le code
        self.moves.insert(0,(self.x, self.y))
        if len(self.moves) > self.longtail:
            self.moves.pop()


    def eat(self, thing):
        if self.head.collidelist(thing) == -1:
            return False
        else:
            return True
    
class Apple:
    def __init__(self):
        self.x = randrange(0 + cell, size_x, cell)
        self.y = randrange(0 + cell, size_y, cell)
        self.coord_apple = pygame.Rect(self.x, self.y, cell, cell)

    def draw(self):
        return [pygame.draw.rect(screen, RED, self.coord_apple)]
        
        
class Wall:
    def __init__(self):
        self.top_wall = pygame.Rect(0, 0, size_x, cell)
        self.bottom_wall = pygame.Rect(0, size_y, size_x, cell)
        self.left_wall = pygame.Rect(0, 0, cell, size_y)
        self.right_wall = pygame.Rect(size_x, 0, cell, size_y + cell)

    def draw(self):    
        return [pygame.draw.rect(screen, WHITE, self.top_wall),
        pygame.draw.rect(screen, WHITE, self.bottom_wall),
        pygame.draw.rect(screen, WHITE, self.left_wall),
        pygame.draw.rect(screen, WHITE, self.right_wall),
            ]

def menu():
    font = pygame.font.Font(None, 40)
    text = font.render("PAUSE", 1, BLUE)
    text1 = font.render("PRESS Q TO QUIT", 1, BLUE)
    screen.blit(text, (190, 240))
    screen.blit(text1, (190, 300))
    pygame.display.flip()
    

def play():
    
    global apple
     
    while 1:
        clock.tick(SPEED)
        screen.fill(BLACK)
        
        wall_ = wall.draw()
        
        snake.draw()
        
        apple_ = apple.draw()
        
        direction = snake.get_direction()
        
        snake.move(direction)
        for event in pygame.event.get():
        
            if event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_SPACE:
                    menu()
                    break
        
        if snake.eat(apple_):
            apple = Apple()
            
        if snake.eat(wall_):
            print("wall")
                    
        pygame.display.flip()
        


direction = "left"
wall = Wall()
snake = Snake()
apple = Apple()

play()
