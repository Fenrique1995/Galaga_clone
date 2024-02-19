import pygame

WIDTH = 800
HEIGHT = 600

def window():
    screen = pygame.display.set_mode([WIDTH,HEIGHT])
    return screen

def controls():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("A")
