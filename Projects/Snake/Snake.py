import pygame
#This creates the screen for the snake game
pygame.init()

#These are the codes for the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#These are the dimensions of the game
dis = pygame.display.set_mode((800, 600))
#This is the name of the game, which is displayed on top of the screen
pygame.display.set_caption('Snek')
 
game_over = False

#This is where the snake starts
x1 = 300
y1 = 300

#These are the empty variables that are used for the snake's movement
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
#This loop are what let you move around as the snake in-game
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            #This moves snake left
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            #This moves snake right
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            #This moves snake up
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            #This moves snake down
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    #This fills the background a certain color
    dis.fill(black)
    #This creates the snake itself
    pygame.draw.rect(dis, white, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
#This command closes the game
pygame.quit()
quit()