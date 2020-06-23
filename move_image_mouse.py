import sys
import pygame

pygame.init()

width=600
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Mover Imagen')

#RGB
white=(255,255,255)
red=(134,45,83)

image=pygame.image.load('images/medium_circle.png')
rect=image.get_rect()
rect.center = (width//2,height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center=pygame.mouse.get_pos() #Tupla -> (x,y)
    
    #validaciones
    if rect.left<0:
        rect.left=0
    if rect.right>width:
        rect.right=width
    if rect.top<0:
        rect.top=0
    if rect.bottom>height:
        rect.bottom=height
        
    surface.fill(white)

    surface.blit(image,rect)

    pygame.display.update()



