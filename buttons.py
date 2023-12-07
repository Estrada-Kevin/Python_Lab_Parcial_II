import pygame


class Button():
    #initializes the button class with the coordinates, the image we want on the button, and the scale
    def __init__(self, x, y, image, scale):
       
        img_width = image.get_width()
        img_height = image.get_height()
        self.active = True
       
        screen_width , screen_height = pygame.display.get_surface().get_size()
       
        self.image = pygame.transform.scale(image,(int(img_width * scale), int(img_height * scale)))
        self.rect = self.image.get_rect()
       
        self.rect.center = (x * screen_width,y * screen_height)
        self.clicked = False
        
    #draws the button on the screen
    #param: screen where to draw
    def draw(self,surface:pygame.Surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    #check if the button is clicked
    #return: True if cliced, False if not
    def check_click(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if not self.active:
            return False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action
    
    #setter of the activate attribute
    def activated(self,active=False):
        self.active = active