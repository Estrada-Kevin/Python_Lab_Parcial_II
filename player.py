import pygame

from entities import *
from sounds import *
from proyectile import *
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

class Player():
    
    #constructor with coordinates and the image to use
    def __init__(self,x,y,image):
        self.reset(x,y,image)

    #method used to reset the level/player/etc. also used in the constructor to initialize values
    #parametros: x,y, image to use
    def reset(self,x,y,image):
        self.image = image
        self.jumped = False
        self.vel_y = 0
        self.rect = self.image.get_rect(topleft=(x,y))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.dead_image = pygame.image.load("images/ghost.png")
        self.game_over = 0
        self.score = 0
        self.lives = 0
        self.visible = True
        self.shoot_cooldown = 0
        self.stage_end_counter = 0
    
    #selects a single part of the sprite sheet to use as an image for the player
    #param: frame , width, height -> used to select a certain part of the image, scale, color
    #return: the image cropped
    def get_image(self,frame,width,height,scale,color):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.image, (0,0) ,((frame*width),0,width,height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

    #makes all the cropped images into a list of lists to use later
    #parame: none
    #return: list of lists with the images
    def get_animation_list(self):
        BLACK_COLOR = (0,0,0)
        animation_list = []
        animation_steps = [4,6,3,4,7]
        step_counter = 0
        for animation in animation_steps:
            auxiliar_animation_list = []
            for _ in range(animation):
                auxiliar_animation_list.append(self.get_image(step_counter,24,24,1.5,BLACK_COLOR))
                step_counter += 1
            animation_list.append(auxiliar_animation_list)

        return animation_list
        
    #manages the movement, collision , deaths of the character
    #param: screen, action,frame,level,flip 
    #return: value if it died or not, used later to manage the levels
    def update(self,screen,action,frame,level,flip=False):
        
        on_ground = False
        #get list of animations, flip if necessary
        visible_rect = self.animate_player(screen,action,frame,flip)

        if self.game_over == 0:
            
            #MOVEMENT PART
            dx = 0
            dy = 0
            key = pygame.key.get_pressed()
            base_speed = 2
            if key[pygame.K_UP] and self.jumped == False:
                jump_fx.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_LSHIFT]:
                base_speed = 5
            if key[pygame.K_RIGHT]:
                dx += base_speed
            if key[pygame.K_LEFT]:
                dx -= base_speed

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y
            #check collision
            for tile in level:
                tile_rect = pygame.Rect(tile[1])
                if tile_rect.colliderect(visible_rect.move(dx,0)):
                    dx = 0
                if tile_rect.colliderect(visible_rect.move(0,dy)):
                    if self.vel_y < 0:
                        dy = tile_rect.bottom - visible_rect.top
                    elif self.vel_y >= 0:
                        dy = tile_rect.top - visible_rect.bottom
                        on_ground = True

            if not key[pygame.K_UP] and on_ground == True:
                self.jumped = False

            #colliding enemies            
            if self.collide(visible_rect,blob_group):
                self.game_over = -1
            if self.collide(visible_rect,blue_blob_group):
                self.game_over = -1
            if self.collide(visible_rect,red_blob_group):
                self.game_over = -1
            if self.collide(visible_rect,metal_blob_group):
                self.game_over = -1
            if self.collide(visible_rect,fish_group):
                self.game_over = -1                  
            if self.collide(visible_rect,lava_group):
                self.game_over = -1                   
            if self.collide(visible_rect,water_group):
                self.game_over = -1
            if self.collide(visible_rect,exit_door_group):
                self.game_over = 1

            #killing enemies
            if self.collide_and_kill_sprites(bullet_group,blob_group):
                self.score += 1
            if self.collide_and_kill_sprites(bullet_group,blue_blob_group):
                self.score += 1
            if self.collide_and_kill_sprites(bullet_group,red_blob_group):
                self.score += 1
            if self.collide_and_kill_sprites(bullet_group,metal_blob_group):
                self.score += 1
            if self.collide_and_kill_sprites(bullet_group,fish_group):
                self.score += 1
                

            auxiliar_item = self.collide_and_kill(visible_rect,coin_group)
            if auxiliar_item in coin_group:
                coin_group.remove(auxiliar_item)
                coin_fx.play()
                self.score += 1
                
            if self.game_over == -1:
                game_over_fx.play()
                self.lives -= 1
            
            
            #move
            self.rect.x += dx
            self.rect.y += dy

            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1
            
        elif self.game_over == -1:
            screen.blit(self.dead_image,(visible_rect.x,visible_rect.y))
            if self.rect.y > 500:
                self.rect.y -= 5
        
           

        return self.game_over

    #check if an entity collides with the entity group
    #param: entity, entities group
    #return: True/False depending if collided
    def collide(self,entity,entities_group):
        for item in entities_group:
            if entity.colliderect(item.rect):
                return True
        return False
    
    #same as collide but its used to "kill" an entity of the entities group if collided
    #param: entity, entities group
    #return: the entity collied if True, or None otherwise
    def collide_and_kill(self,entity,entities_group):
        for item in entities_group:
            if entity.colliderect(item.rect):
                return item
        return None
    
    #same as collide_and_kill but its used to check collision between groups of entities (sprites)
    #param: entities that "kill", entities "killed"
    #param: True if killed , False otherwise
    def collide_and_kill_sprites(self,entities_group_killer,entities_group_killed):
        for item in entities_group_killer:
            if pygame.sprite.spritecollide(item,entities_group_killed,True):
                item.kill()
                return True
        return False

    #method that animates the list of images and get the visible rect to use later
    #param: screen, actions, frame, flip
    #return: the visible rect of the image we want to use to check for collisions
    def animate_player(self,screen,action,frame,flip=False):
        
        auxiliar_list = self.get_animation_list()
    
        if flip == True:
            normal_image = pygame.transform.flip(auxiliar_list[action][frame],True,False).convert_alpha()
        else:
            normal_image = auxiliar_list[action][frame] 

        visible_rect = normal_image.get_rect(topleft=(self.rect.x - normal_image.get_width() / 2, self.rect.y - normal_image.get_height() / 2))

        screen.blit(normal_image, visible_rect.topleft)

        return visible_rect
    
    #makes the player shoot
    #param: bullet group, action, screen, frame, flip_image, shoot
    #return: None
    def shoot(self, bullet_group, action,screen, frame, flip_image, shoot):
        player_direction = 1 if not flip_image else -1
        if shoot == True:
            if self.shoot_cooldown == 0:
                self.shoot_cooldown = 20
                bullet = Proyectile(
                    self.animate_player(screen, action, frame, flip_image).centerx + (18 * player_direction),
                    self.animate_player(screen, action, frame, flip_image).centery - (5 * player_direction),
                    pygame.image.load("images/proyectile.png"),
                    player_direction
                )
                bullet_group.add(bullet)

                if flip_image:
                    bullet.rect.x -= bullet.rect.width - 10
                    bullet.rect.y -= bullet.rect.height
    
    
    #getters
    def get_score(self):
        return self.score
    
    def get_lifes(self):
        return self.lives
    