import pygame
import random
import sys 

pygame.init()

def main():
    
    def gameOver():
        font = pygame.font.SysFont('times new roman', 30)
        gameover = font.render("Press R to Respawn", False, (255, 255, 255))
        rect = gameover.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(gameover, rect)
   
    done = False
    clock = pygame.time.Clock()

    #Define Windows Dimensions
    windows_w = 500
    windows_h = 500

    #Colors 
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    green = pygame.Color(0, 255, 0)

    #Game Variables
    snake_p = [100, 50]
    snake = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_p = [random.randrange(1, (windows_w//10)) * 10, random.randrange(1, (windows_h//10)) * 10]
    food_s = True
    direc = 'RIGHT'
    change_dir = direc
    screen = pygame.display.set_mode((windows_w,windows_h)) #Set Display Dimension
    title = pygame.display.set_caption("Sneaky") #Set Title of the window
    
    #Main loop
    while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    sys.exit()
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: change_dir = 'UP'
            if pressed[pygame.K_DOWN]: change_dir = 'DOWN'
            if pressed[pygame.K_LEFT]: change_dir = 'LEFT'
            if pressed[pygame.K_RIGHT]: change_dir = 'RIGHT'
            if pressed[pygame.K_ESCAPE]: pygame.event.post(pygame.event.Event(pygame.QUIT))
            if pressed[pygame.K_r]: main()
            
            # Making sure the snake cannot move in the opposite direction instantaneously
            if change_dir == 'UP' and direc != 'DOWN':
                direc = 'UP'
            if change_dir == 'DOWN' and direc != 'UP':
                direc = 'DOWN'
            if change_dir == 'LEFT' and direc != 'RIGHT':
                direc = 'LEFT'
            if change_dir == 'RIGHT' and direc != 'LEFT':
                direc = 'RIGHT'
            # Moving the snake
            if direc == 'UP': snake_p[1] -= 10
            if direc == 'DOWN': snake_p[1] += 10
            if direc == 'LEFT': snake_p[0] -= 10
            if direc == 'RIGHT': snake_p[0] += 10
            
            # Snake body growing mechanism
            snake.insert(0, list(snake_p))
            if snake_p[0] == food_p[0] and snake_p[1] == food_p[1]:
                food_s = False
            else:
                snake.pop()
            
            #Snake food spawn
            if not food_s:
                food_p = [random.randrange(1, (windows_w//10)) * 10, random.randrange(1, (windows_h//10)) * 10]
            food_s = True

            #Initialize screen
            screen.fill(black)
                    
            # Snake food
            pygame.draw.rect(screen, white, pygame.Rect(food_p[0], food_p[1], 10, 10))
            
            #Player
            for pos in snake:
                pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
            
            #Adding collision with screen
            if snake_p[0] < 0 or snake_p[0] > windows_w-10:
                gameOver()
            if snake_p[1] < 0 or snake_p[1] > windows_h-10:
                gameOver()
            #Collision with snake 
            for block in snake[1:]:
                if snake_p[0] == block[0] and snake_p[1] == block[1]:
                    gameOver()
                
            pygame.display.update() 
            clock.tick(15)
main()                