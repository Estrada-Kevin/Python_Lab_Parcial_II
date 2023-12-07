import pygame

#group of entities
blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_door_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
blue_blob_group = pygame.sprite.Group()
red_blob_group = pygame.sprite.Group()
metal_blob_group = pygame.sprite.Group()
fish_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()


class Entities(pygame.sprite.Sprite):

    #initialize the class with its values and the image depending o the optionas values
    def __init__(self, x, y, image,tile_size=0, isTerrain=False, isConstruction=False):
        pygame.sprite.Sprite.__init__(self)
        if isTerrain == False and isConstruction == False:
            self.image = pygame.image.load(image)
        elif isTerrain == True and isConstruction == False:
            loaded_image = pygame.image.load(image)
            self.image = pygame.transform.scale(loaded_image,(tile_size, tile_size // 2))
        elif isConstruction == True and isTerrain == False:
            loaded_image = pygame.image.load(image)
            self.image = pygame.transform.scale(loaded_image,(tile_size, int(tile_size *1.5)))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    #updates where the entity is
    #param: distance moved, direction to move, speed
    def update(self,distance, is_vertical=False, speed=1):
        if is_vertical == False:
            self.rect.x += self.move_direction * speed
            self.move_counter += 1
            if abs(self.move_counter) > distance:
                self.image = pygame.transform.flip(self.image,True,False)
                self.move_direction *= -1
                self.move_counter *= -1
        else:
            self.rect.y += self.move_direction * speed
            self.move_counter += 1
            if abs(self.move_counter) > distance:
                self.image = pygame.transform.flip(self.image,False,True)
                self.move_direction *= -1
                self.move_counter *= -1
            