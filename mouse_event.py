import sys
import pygame

pygame.init()

width=400
height=600

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Event Mouse')

#RGB
white=(255,255,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print("Boton presionado")
            # print (event)
            print(event.pos)
            if event.button==1:
                print("Clic Izquierda")
            if event.button==2:
                print("Clic Centro")
            if event.button==3:
                print("Clic Derecha")
            if event.button==4:
                print("Scroll hacia arriba")
            if event.button==5:
                print("Scroll hacia abajo")
                
        if event.type == pygame.MOUSEBUTTONUP:
            # print("Boton Liberado")
            pass

    surface.fill(white)
    
    pygame.display.update()



