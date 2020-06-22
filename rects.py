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
my_color =(0,0,128)

# pygame.Rect(x,y,width,height)
rect=pygame.Rect(100,150,120,60)
rect.center=(width//2,height//2)

print(rect.x)
print(rect.y)

# rect2=(x,y,width,height)
rect2=(100,100,80,40)


# https://color.hailpixel.com/
# https://www.webpagefx.com/web-design/hex-to-rgb/
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)

    #Pintamos el rectangulo
    pygame.draw.rect(surface,red,rect)
    pygame.draw.rect(surface,green,rect2)
    
    pygame.display.update()



