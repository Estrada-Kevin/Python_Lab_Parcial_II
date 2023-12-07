import pygame
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
bullet_group = pygame.sprite.Group()


class Proyectile(pygame.sprite.Sprite):
    def __init__(self,x,y,image,direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    
    #updates where the proyectile 
    def update(self):
        self.rect.x += (self.direction * self.speed) 
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

