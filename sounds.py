import sys
import pygame

pygame.init()

width=400
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Sounds')

#RGB
red=pygame.Color(255,0,0) #0-255 
white=(255,255,255)

pygame.mixer.music.load('sounds/Haggstrom.mp3')
pygame.mixer.music.set_volume(1.0) #Float 0.0-1.0
pygame.mixer.music.play(-1,0.0)

# pygame.mixer.music.rewind()
# pygame.mixer.music.pause()
# pygame.mixer.music.stop()
# pygame.mixer.music.fadeout(5000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(white)
    
    
    pygame.display.update()



