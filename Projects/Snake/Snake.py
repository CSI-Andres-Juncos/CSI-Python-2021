from time import sleep
import pygame
import random
 
pygame.init()
 
white = (255, 255, 255)
blue = (66, 138, 246)
black = (0, 0, 0)
red = (246, 66, 84)

width = 800
height = 600 
dis = pygame.display.set_mode((width, width))
pygame.display.set_caption('Budget Metal Gear Solid')

clock = pygame.time.Clock()

snake=10
movement_speed=30

font = pygame.font.SysFont(None, 50)

def message(msg,color):
    mesg = font.render(msg, True, color)
    dis.blit(mesg, [width/3, height/3])

def gameLoop():
    game_over=False
    game_close=False

    x1 = width / 2
    y1 = height / 2
 
    x1_change = 0
    y1_change = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake
                    x1_change = 0
 

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, blue, [x1, y1, snake, snake])
    
        pygame.display.update()

        clock.tick(snake)
    message("You lost get gud",white)
    pygame.display.update()

    sleep(2)
    pygame.quit()
    quit()

gameLoop()