import sys
import pygame

pygame.init()

width=400
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Text')

#RGB
red=pygame.Color(255,0,0) #0-255 
white=(255,255,255)

#1.-Obtener una fuente
# font=pygame.font.Font('freesansbold.ttf',48)
font=pygame.font.Font('roboto/Roboto-Thin.ttf',48)

#2--Crear Texto
text=font.render('Hola Mundo',True,red) #-> surface
rect=text.get_rect()
rect.center=(width//2,height//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)

    surface.blit(text,rect)
    pygame.display.update()



