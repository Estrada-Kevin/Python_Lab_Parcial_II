import pygame
from configuration import *
from entities import *



level_one = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 1],
    [1, 23, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 11, 0, 0, 0, 0, 0, 2, 1],
    [1, 2, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 1],
    [1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 3, 3, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 2, 2, 2, 2, 2, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

level_two = [
    [1, 8, 8, 8, 10, 9, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8, 8, 8, 8, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 23, 1, 1, 10, 0, 0, 0, 0, 0, 0, 1],
    [1, 7, 7, 0, 0, 0, 9, 1, 0, 1, 1, 10, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 12, 1],
    [1, 0, 0, 5, 5, 0, 0, 9, 1, 1, 1, 1, 10, 0, 0, 0, 6, 7, 7, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 10, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 5, 0, 0, 0, 0, 0, 1],
    [1, 7, 7, 6, 0, 0, 0, 0, 1, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 20, 0, 1, 10, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 23, 0, 0, 0, 5, 1],
    [1, 0, 0, 7, 7, 6, 7, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [1, 0, 0, 0, 0, 6, 0, 0, 20, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 1],
    [1, 5, 5, 0, 0, 0, 0, 0, 1, 0, 20, 0, 0, 0, 0, 0, 0, 5, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 19, 0, 0, 0, 1],
    [1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 1, 3, 3, 5, 5, 5, 5, 5, 3, 1],
    [1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1],
    [1, 4, 4, 4, 4, 4, 4, 4, 1, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

level_three = [
    [13, 0, 0, 0, 21, 0, 0, 0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13],
    [13, 0, 0, 0, 23, 0, 0, 0, 17, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 14, 0, 0, 14, 0, 17, 0, 0, 0, 0, 0, 14, 15, 15, 14, 0, 13],
    [13, 0, 14, 17, 0, 0, 17, 0, 17, 0, 0, 0, 14, 0, 17, 14, 14, 14, 0, 13],
    [13, 0, 0, 17, 0, 14, 0, 0, 0, 0, 0, 0, 17, 0, 17, 14, 0, 0, 0, 13],
    [13, 14, 0, 17, 23, 17, 0, 0, 18, 23, 14, 14, 14, 14, 14, 14, 12, 0, 0, 13],
    [13, 0, 0, 17, 0, 17, 0, 14, 14, 14, 17, 0, 0, 0, 0, 17, 14, 14, 14, 13],
    [13, 0, 14, 17, 0, 17, 0, 0, 17, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 17, 14, 15, 17, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 13],
    [13, 14, 0, 0, 0, 17, 16, 16, 17, 0, 14, 15, 15, 15, 14, 14, 14, 14, 0, 13],
    [13, 0, 0, 0, 14, 17, 17, 17, 17, 14, 17, 17, 17, 17, 17, 17, 0, 0, 0, 13],
    [13, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 14, 14, 14, 13],
    [13, 14, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 22, 0, 17, 0, 14, 22, 0, 0, 0, 0, 18, 0, 0, 0, 0, 13],
    [13, 15, 14, 15, 15, 14, 17, 15, 17, 15, 14, 15, 15, 14, 14, 14, 15, 15, 15, 13],
    [13, 16, 16, 16, 16, 16, 17, 16, 17, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16, 13],
    [13, 16, 16, 16, 16, 16, 17, 16, 17, 16, 17, 16, 16, 16, 16, 16, 16, 16, 16, 13],
    [13, 13, 13, 13, 13, 13, 17, 13, 17, 13, 17, 13, 13, 13, 13, 13, 13, 13, 13, 13],
]


class Level:
    def __init__(self,data,start_x,start_y):
        self.tile_list = []
        self.data=data
        self.dirt_img = pygame.image.load("images/dirt.png")
        self.grass_img = pygame.image.load("images/grass.png")
        self.lava_interior_img = pygame.image.load("images/lava_interior.png")
        self.metal_plataform_img = pygame.image.load("images/metal_plataform.png")
        self.metal_img = pygame.image.load("images/metal.png")
        self.metal_with_wire_img = pygame.image.load("images/metal_with_wire.png")
        self.dirt_border_img = pygame.image.load("images/dirt_border.png")
        self.dirt_corner_left_img = pygame.image.load("images/dirt_corner_left.png")
        self.dirt_corner_right_img = pygame.image.load("images/dirt_corner_right.png")
        self.ice_block_img = pygame.image.load("images/ice_block.png")
        self.ice_floor_img = pygame.image.load("images/ice_floor.png")
        self.ice_center_img = pygame.image.load("images/ice_center.png")
        self.water_deep_img = pygame.image.load("images/water_deep.png")
        self.metal_block_img = pygame.image.load("images/metal_block.png")
        self.start_x = start_x        
        self.start_y = start_y        
    
    #draws the level based on the tiles from the data
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])
            # pygame.draw.rect(screen,(255,255,255),tile[1],2)
    
    #if used, draws a grid for better understanding of the screen
    def draw_grid(self):
         for line in range(0, 20):
              pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (SCREEN_WIDTH, line * tile_size))
              pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, SCREEN_HEIGHT))

    #loads the tile with the image we want
    #param: image we want to use, size of the image, and the coordinates from the columns / rows
    def load_tiles(self,image,tile_size,col_count,row_count):
        img = pygame.transform.scale(image,(tile_size,tile_size))
        img_rect = img.get_rect()
        img_rect.x = col_count * tile_size
        img_rect.y = row_count * tile_size
        tile = (img,img_rect)
        self.tile_list.append(tile)

    #use the function from before to load everything based on the specified tile
    def load_level(self):
        row_count = 0

        for row in self.data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.load_tiles(self.dirt_img,tile_size,col_count,row_count)
                if tile == 2:
                    self.load_tiles(self.grass_img,tile_size,col_count,row_count)
                if tile == 3:
                    lava = Entities(col_count * tile_size, row_count * tile_size + (tile_size // 2),"images/lava.png",tile_size,True)
                    lava_group.add(lava)
                if tile == 4:
                    self.load_tiles(self.lava_interior_img,tile_size,col_count,row_count)
                if tile == 5:
                    self.load_tiles(self.metal_plataform_img,tile_size,col_count,row_count)
                if tile == 6:
                    self.load_tiles(self.metal_with_wire_img,tile_size,col_count,row_count)
                if tile == 7:
                    self.load_tiles(self.metal_img,tile_size,col_count,row_count)
                if tile == 8:
                    self.load_tiles(self.dirt_border_img,tile_size,col_count,row_count)
                if tile == 9:
                    self.load_tiles(self.dirt_corner_left_img,tile_size,col_count,row_count)
                if tile == 10:
                    self.load_tiles(self.dirt_corner_right_img,tile_size,col_count,row_count)
                if tile == 11:
                    blob = Entities(col_count * tile_size, row_count * tile_size + 15,"images/blob.png",tile_size)
                    blob_group.add(blob)
                if tile == 12:
                    exit_door = Entities(col_count * tile_size, row_count * tile_size - (tile_size // 2), "images/exit_door.png",tile_size,False,True)
                    exit_door_group.add(exit_door)
                if tile == 13:
                    self.load_tiles(self.ice_block_img,tile_size,col_count,row_count)
                if tile == 14:
                    self.load_tiles(self.ice_floor_img,tile_size,col_count,row_count)
                if tile == 15:
                    water = Entities(col_count * tile_size, row_count * tile_size + (tile_size // 2),"images/water.png",tile_size,True)
                    water_group.add(water)
                if tile == 16:
                    self.load_tiles(self.water_deep_img,tile_size,col_count,row_count)
                if tile == 17:
                    self.load_tiles(self.ice_center_img,tile_size,col_count,row_count)
                if tile == 18:
                    blue_blob = Entities(col_count * tile_size, row_count * tile_size + 15,"images/blue_blob.png",tile_size)
                    blue_blob_group.add(blue_blob)
                if tile == 19:
                    red_blob = Entities(col_count * tile_size, row_count * tile_size + 15,"images/red_blob.png",tile_size)
                    red_blob_group.add(red_blob)
                if tile == 20:
                    self.load_tiles(self.metal_block_img,tile_size,col_count,row_count)
                if tile == 21:
                    metal_blob = Entities(col_count * tile_size, row_count * tile_size + 15,"images/metal_blob.png",tile_size)
                    metal_blob_group.add(metal_blob)
                if tile == 22:
                    fish = Entities(col_count * tile_size, row_count * tile_size + 15,"images/fish_down.png",tile_size)
                    fish_group.add(fish)
                if tile == 23:
                    coin = Entities(col_count * tile_size - 10, row_count * tile_size - 10,"images/coin.png",tile_size)
                    coin_group.add(coin)
                col_count += 1
            row_count += 1


    #clear everything loaded, so we can change levels
    def clear(self):
        self.tile_list = []
        lava_group.empty()
        blob_group.empty()
        fish_group.empty()
        water_group.empty()
        blue_blob_group.empty()
        red_blob_group.empty()
        metal_blob_group.empty()
        exit_door_group.empty()
        coin_group.empty()

    
                
            