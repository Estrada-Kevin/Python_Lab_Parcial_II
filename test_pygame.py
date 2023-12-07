import pygame
from configuration import *
from levels import *
from sounds import *
from proyectile import *



#states of games
game_in_principal_menu = True
game_in_options = False
game_in_select_level = False
game_in_game = False
game_in_write_text = False
game_in_top_five = False
shoot = False
menu_principal = 1

level_changed = True
file_saved = False
game_level_one = Level(level_one,LEVEL_ONE_X,LEVEL_ONE_Y)
game_level_two = Level(level_two,LEVEL_TWO_X,LEVEL_TWO_Y)
game_level_three = Level(level_three,LEVEL_THREE_X,LEVEL_THREE_Y)
current_level = game_level_one
#logic
while running:
    #timer logic
    key = pygame.key.get_pressed()
    clock.tick(fps)
    current_time = pygame.time.get_ticks()
    current_time_seconds = int(current_time / 1000)

    if current_time - last_update >= animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    
    #background drawing
    screen.blit(grasslands_background_img,(0,0))  
    
    #Menu 
    #Main menu        
    if game_in_principal_menu == True:
        buttons_on_screen(main_menu_buttons)
        buttons_on_off(main_menu_buttons,True)
    if game_in_principal_menu == False:
        buttons_on_off(main_menu_buttons,False)

    if start_button.check_click():
        game_in_principal_menu = False
        # game_in_game = True
        game_in_write_text = True
    if quit_button.check_click():
        running = False
    if options_button.check_click():
        game_in_options = True
        game_in_principal_menu = False

    
    #Write name menu
    if game_in_write_text == True:
        writer_menu.write_text("Write your name:",300,400,True)
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT and len(player_name)<10:
                if letters_pattern.match(event.text):
                    player_name += event.text
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                if event.key == K_RETURN and len(player_name) > 0:
                    game_in_write_text = False
                    game_in_game = True
        writer_menu.write_text(player_name,350,500,True)
        
    #Option Menu
    if game_in_options == True:
        buttons_on_screen(options_buttons)
        buttons_on_off(options_buttons,True)
    if game_in_options == False:
        buttons_on_off(options_buttons,False)

    if top_five_button.check_click():
        game_in_top_five = True
        
    if select_level_button.check_click():
        game_in_select_level = True
        game_in_options = False
        game_in_top_five = False
    if back_to_options_button.check_click():
        game_in_principal_menu = True
        game_in_options = False
        game_in_top_five = False

    #Level select menu
    if game_in_select_level == True:
        buttons_on_screen(level_select_buttons)
        buttons_on_off(level_select_buttons,True)
    if game_in_select_level == False:
        buttons_on_off(level_select_buttons,False)
    
    if level_one_button.check_click():
        game_in_select_level = False
        current_level = game_level_one
        game_in_game = True
        player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)
    if level_two_button.check_click():
        game_in_select_level = False
        current_level = game_level_two
        game_in_game = True
        player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)
    if level_three_button.check_click():
        game_in_select_level = False
        current_level = game_level_three
        game_in_game = True
        player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)
    if back_to_select_button.check_click():
        game_in_select_level = False
        game_in_options = True

    #top five
    if game_in_top_five == True:
        writer_score.write_text_list(top_five,500,300)



    #in game logic
    if game_in_game == True:
        current_level.draw()
        
        if game_over == 0:
            blob_group.update(50)
            blue_blob_group.update(50)
            red_blob_group.update(50)
            metal_blob_group.update(50,False,3)
            fish_group.update(50,True,3)
            bullet_group.update()


            
        coin_group.draw(screen)
        blob_group.draw(screen)
        blue_blob_group.draw(screen)
        red_blob_group.draw(screen)
        fish_group.draw(screen)
        lava_group.draw(screen)
        water_group.draw(screen)
        metal_blob_group.draw(screen)
        exit_door_group.draw(screen)
        bullet_group.draw(screen)
        game_over = player.update(screen,action,frame,current_level.tile_list,flip_image)

        if game_over == -1:
            writer_menu.write_text("GAME OVER",320,400, True)
            respawn_button.draw(screen)
            quit_button_in_restart.draw(screen)
            if respawn_button.check_click():
                score += player.get_score()
                lifes += player.get_lifes()
                player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)
            if quit_button_in_restart.check_click():
                running = False
        if game_over == 1:
            if current_level == game_level_one:
                current_level = game_level_two
                level_changed = True
                score += player.get_score()
                lifes += player.get_lifes()
                player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)
            elif current_level == game_level_two:
                current_level = game_level_three
                level_changed = True    
                score += player.get_score()
                lifes += player.get_lifes()
                player = Player(current_level.start_x,current_level.start_y,dino_sprite_sheet_image)

        if lifes == 0:  
            writer_menu.write_text(f"NO MORE LIFES LEFT",230,300,True)
            writer_menu.write_text(f"Score: {score}",230,250,True)
            if file_saved == False:
                save_file(path,f"Player: {capitalize_words(player_name)} - Score: {score}")
                file_saved = True
            running = end_game(current_level)

        if current_level == game_level_three and game_over == 1:
            writer_menu.write_text(f"Score: {score}",320,400,True)
            writer_menu.write_text(f"CONGRATS YOU WON!!",SCREEN_WIDTH,SCREEN_HEIGHT)
            visible_rect = player.animate_player(screen,action,frame,flip_image)
            if player.collide(visible_rect,exit_door_group):
                if file_saved == False:
                    save_file(path,f"Player: {capitalize_words(player_name)} - Score: {score}")
                    file_saved = True
            running = end_game(current_level)

        if level_changed == True:
            current_level.clear()
            current_level.load_level()
            level_changed=False
        
        writer_menu.write_text(f"LIFES: {lifes}",750,900,True)


        #shooting mechanic
        player.shoot(bullet_group, action,screen, frame, flip_image,shoot)
        #end of shooting mechanic
        
        
    

    #buttons logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action >0 :
                action = 0
                frame = 0
            if event.key == pygame.K_RIGHT: 
                action = 1
                frame = 0
                flip_image = False
            if event.key == pygame.K_LEFT:
                flip_image = True
                action = 1
                frame = 0
            if event.key == pygame.K_UP:
                action = 2
                frame = 0
            if event.key == pygame.K_SPACE:
                shoot = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                action = 0
                frame = 0
            if event.key == pygame.K_SPACE:
                shoot=False
    
        
    writer_timer.write_text(f"{current_time_seconds}",5,1,True) 
    pygame.display.update()

pygame.quit()



