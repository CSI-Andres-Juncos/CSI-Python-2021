import pygame
#This creates the screen for the snake game
pygame.init()
#These are the dimensions of the game
dis=pygame.display.set_mode((400,300))
pygame.display.update()
#This is the name of the game, which is displayed on top of the screen
pygame.display.set_caption('Snake')
game_over=False
#This loop is to stop the game from closing immediately after you open it
while not game_over:
    for event in pygame.event.get():
        print(event)
        #This is so you can close the game when you hit the x button
        if event.type==pygame.QUIT:
            game_over=True

#This command closes the game
pygame.quit()
quit()