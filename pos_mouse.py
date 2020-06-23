import sys
import pygame

pygame.init()

width=400
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Event Mouse')

#RGB
white=(255,255,255)
red=(134,45,83)

font=pygame.font.Font('freesansbold.ttf',35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pos_x,pos_y=pygame.mouse.get_pos() # Tupla (x,y)
    message='pos x: {} pos y: {}'.format(pos_x,pos_y)
    # print (message)

    text=font.render(message,True,red)
    rect=text.get_rect()
    rect.center = (width//2,height//2)
    

    surface.fill(white)

    surface.blit(text,rect)
    pygame.display.update()



