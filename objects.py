import pygame

class Ship:
    def __init__(self, position_x, position_y, name, health):
        self.position_x = position_x
        self.position_y = position_y
        self.sprite = pygame.transform.scale(pygame.image.load('sprites/blackwing.png'), (70, 70))
        self.name = name
        self.health = health
    def draw(self, screen):
        screen.blit(self.sprite, (self.position_x, self.position_y))
        self.hitbox = (self.position_x, self.position_y, 70, 70)
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)
    def movement(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:#Movimientos rectos
            self.position_x -= 3
        elif  keys[pygame.K_d]:
            self.position_x += 3
        elif  keys[pygame.K_w]:
            self.position_y -= 3
        elif  keys[pygame.K_s]:
            self.position_y += 3

        if  keys[pygame.K_s] and keys[pygame.K_d]:#Movimientos diagonales
            self.position_y += 3
            self.position_x += 3
        elif  keys[pygame.K_s] and keys[pygame.K_a]:
            self.position_y += 3
            self.position_x -= 3
        elif  keys[pygame.K_w] and keys[pygame.K_a]:
            self.position_y -= 3
            self.position_x -= 3
        elif  keys[pygame.K_w] and keys[pygame.K_d]:
            self.position_y -= 3
            self.position_x += 3
        pygame.display.update()