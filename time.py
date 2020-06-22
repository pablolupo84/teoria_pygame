import sys
import pygame

pygame.init()

width=400
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Tiempo')

#RGB
red=pygame.Color(255,0,0) #0-255 
white=(255,255,255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time=pygame.time.get_ticks() //1000#milisengudos desde que se inicio la app
    print(time)
    surface.fill(white)


    pygame.display.update()



