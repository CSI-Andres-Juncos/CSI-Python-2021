import pygame
#This creates the screen for the snake game
pygame.init()
#These are the dimensions of the game
dis=pygame.display.set_mode((400,300))
#This is the name of the game, which is displayed on top of the screen
pygame.display.set_caption('Snake')

#This sets the colors that will be used in the game
white=(255,255,255)
red=(255,0,0)

game_over=False
#This loop is to stop the game from closing immediately after you open it
while not game_over:
    for event in pygame.event.get():
        print(event)
        #This is so you can close the game when you hit the x button
        if event.type==pygame.QUIT:
            game_over=True
    #This code creates th snake itself with the draw.rect function
    pygame.draw.rect(dis,white,[200,150,10,10])
    pygame.display.update()
#This command closes the game
pygame.quit()
quit()