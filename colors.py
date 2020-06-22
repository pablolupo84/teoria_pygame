import sys
import pygame

pygame.init()

width = 400
height=500

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Colores')

#RGB
red=pygame.Color(255,0,0) #0-255 
green=pygame.Color(0,250,0) 
blue=pygame.Color(0,0,255)  

white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)

#Colores utiles
Aqua    =( 0, 255, 255)
Fuchsia	=(255, 0, 255)
Gray    =(128, 128, 128)
Green   =(0,128,0)
Maroon  =(128, 0, 0)
Navy_Blue=( 0, 0,128)
Olive   =(128, 128, 0)
Purple  =(128, 0, 128)
Silver  =(192, 192, 192)
Teal	=( 0, 128, 128)
Yellow  =(255, 255, 0)

my_color =(57,25,77)

# https://color.hailpixel.com/
# https://www.webpagefx.com/web-design/hex-to-rgb/
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    pygame.display.update()



