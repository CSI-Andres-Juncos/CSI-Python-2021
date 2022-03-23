import pygame
import time
#This creates the screen for the snake game
pygame.init()
#These are the codes for the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
#These sets the dimensions of the game
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))
#This is the name of the game, which is displayed on top of the screen
pygame.display.set_caption('Snek')
 
game_over = False
 
x1 = dis_width/2
y1 = dis_height/2

#Variable for snake size
snake=10

#These are the empty variables that are used for the snake's movement
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock()
#This is the speed of the nake
movement_speed=30
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
#This loop are what let you move around as the snake in-game
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            #This moves the snake left
            if event.key == pygame.K_LEFT:
                x1_change = -snake
                y1_change = 0
            #This moves the snake right
            elif event.key == pygame.K_RIGHT:
                x1_change = snake
                y1_change = 0
            #This moves the snake up
            elif event.key == pygame.K_UP:
                y1_change = -snake
                x1_change = 0
            #This moves the snake down
            elif event.key == pygame.K_DOWN:
                y1_change = snake
                x1_change = 0

#This sets that if the player hits the boundary, the game is over
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    #This fills the background black
    dis.fill(black)
    #This creates the snake
    pygame.draw.rect(dis, white, [x1, y1, snake, snake])
 
    pygame.display.update()
 
    clock.tick(movement_speed)

#This is the message that will come out if you die
message("You are die",red)
pygame.display.update()
time.sleep(2)
 
#This ends the game
pygame.quit()
quit()