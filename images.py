import sys
import pygame

pygame.init()

width=600
height=800

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Imagenes')

#RGB
red=pygame.Color(255,0,0) #0-255 
green=pygame.Color(52,157,89) 
blue =(59,87,181)
white=(255,255,255)

image=pygame.image.load('images/codi.png')#-> surface
rect=image.get_rect()

rect.center=(width//2,height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(image,(100,100))

    
    pygame.display.update()



