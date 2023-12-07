import pygame

from writer import *
from buttons import *
from player import Player
import re
from data_base import *

pygame.init()


#initial configuration
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
LEVEL_ONE_Y = 900
LEVEL_ONE_X = 75
LEVEL_TWO_Y = 95
LEVEL_TWO_X = 75
LEVEL_THREE_Y = 475
LEVEL_THREE_X = 475
BLACK_COLOR = (0,0,0)

fps = 60
clock = pygame.time.Clock()
last_update = pygame.time.get_ticks()
animation_cooldown = 100
tile_size = 50
frame = 0
action = 0 

score = 0
lifes = 3
game_over = 0
flip_image = False
path = "score.txt"
player_name = ""
letters_pattern = re.compile('[a-zA-Z]')
font = pygame.font.SysFont("Futura",60)
top_five = read_file(path)
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Dinorio")
running = True

#img load
def load_images(image):
    image = pygame.image.load(image).convert_alpha()
    return image


start_img = load_images("images\start_img.png")
quit_img = load_images("images\quit_img.png")
options_img = load_images("images\options_img.png")
more_info_img = load_images("images\more_info_img.png")
select_level_img = load_images("images\select_level.png")
back_img = load_images("images\\back_img.png")
restart_img = load_images("images/restart.png")
select_level_one = load_images("images/menu_select_level_one.png")
select_level_two = load_images("images/menu_select_level_two.png")
select_level_three = load_images("images/menu_select_level_three.png")

dino_sprite_sheet_image = load_images("images/dino_sprite.png")

grasslands_background_img = load_images("images/grasslands_background.png")
grasslands_background_img = pygame.transform.scale(grasslands_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))





#init. instances
writer_menu = Writer(screen, "arialblack", 50, (0,0,0))
writer_score = Writer(screen, "Futura", 30, (0,0,0))
writer_timer = Writer(screen,"Futura",30,(0,0,0))

player = Player(LEVEL_ONE_X,LEVEL_ONE_Y,dino_sprite_sheet_image)
animation_list = player.get_animation_list()


#init buttons
start_button = Button(0.2,0.4, start_img, 0.6)
options_button = Button(0.5,0.4, options_img, 0.6)
quit_button = Button(0.8,0.4, quit_img, 0.6)
top_five_button = Button(0.2,0.5, more_info_img, 0.6)
select_level_button = Button(0.5,0.5, select_level_img, 0.6)
back_to_options_button = Button(0.8,0.5, back_img, 0.6)
respawn_button = Button(0.4,0.5,restart_img,0.6)
quit_button_in_restart = Button(0.6,0.5, quit_img,0.6)
level_one_button = Button(0.2,0.6, select_level_one,0.6)
level_two_button = Button(0.5,0.6, select_level_two,0.6)
level_three_button = Button(0.8,0.6, select_level_three,0.6)
back_to_select_button = Button(0.5,0.7, back_img, 0.6)
main_menu_buttons = [start_button, options_button, quit_button]
options_buttons = [top_five_button,select_level_button,back_to_options_button]
level_select_buttons = [level_one_button,level_two_button,level_three_button,back_to_select_button]


#other methods

#activates or deactives a group of buttons
#param: buttons list, state of the button
def buttons_on_off(buttons_list, state):
    for button in buttons_list:
        button.activated(state)

#shows a group of buttons on screen
#buttons list
def buttons_on_screen(button_list):
    for button in button_list:
        button.draw(screen)

#check if is the end of the game
#return: True if ended, False if not
def end_game(current_level):
    current_level.clear()
    quit_button.draw(screen)
    quit_button.activated(True)
    if quit_button.check_click()==True:
        return False
    else:
        return True


    