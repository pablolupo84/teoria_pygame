import sys
import pygame

pygame.init()

width = 400
height=500

surface = pygame.display.set_mode((width,height)) # surface
pygame.display.set_caption('Mi primer Juego')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()