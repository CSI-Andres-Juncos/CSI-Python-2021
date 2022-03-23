import pygame
import time
import random
#This creates the screen for the snake game
pygame.init()
#These are the codes for the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
#These sets the dimensions of the game
dis_width = 800
dis_height = 600
#This is the name of the game, which is displayed on top of the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snek')
 
clock = pygame.time.Clock()

#Variable for snake size and speed
snake = 10
movement_speed = 30
#This determines the font for text
font_style = pygame.font.SysFont(None, 30)
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])
 
 
def gameLoop():  #This is the loop that makes the game continue until you die
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    #These are the empty variables that are used for the snake's movement
    x1_change = 0
    y1_change = 0
    #This is the randomizer for the food
    foodx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
 

    while not game_over:
    #This displays the death message
        while game_close == True:
            dis.fill(black)
            message("You are die. Press Q to quit or E to play again", red)
            pygame.display.update()
        #This forloop is to exit and retry the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_e:
                        gameLoop()
    #This loop are what let you move around as the snake in-game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                #Moves left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                #Moves right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                #Moves up
                elif event.key == pygame.K_UP:
                    y1_change = -snake
                    x1_change = 0
                #Moves down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake
                    x1_change = 0
        #This sets that if the player hits the boundary, the game is over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        #This spawns the food
        pygame.draw.rect(dis, blue, [foodx, foody, snake, snake])
        #This spawns the snake
        pygame.draw.rect(dis, white, [x1, y1, snake, snake])
        pygame.display.update()
        #This displays the message every time you eat somthing
        if x1 == foodx and y1 == foody:
            print("Nom")
        clock.tick(movement_speed)
    #This close the game
    pygame.quit()
    quit()
 
#This restarts the game entirely
gameLoop()