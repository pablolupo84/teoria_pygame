import sys
import pygame

pygame.init()

width=600
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Collition Circle')

#RGB
white=(255,255,255)
red=(134,45,83)
green=(52,157,89)
blue=(59,87,181)

rect1=pygame.Rect(0,0,100,80)
rect1.center=(width//2,height//2)

surface2=pygame.Surface((rect1.width,rect1.height),pygame.SRCALPHA)
surface2.fill((0,0,0,50))

rect2=surface2.get_rect()
rect2.center=rect1.center

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill(white)

    surface.blit(image1,rect1)
    surface.blit(surface2,rect2)


    pygame.display.update()



