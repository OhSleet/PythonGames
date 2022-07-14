#  _______                    __       __________                 
#  \      \    ____  _____  _/  |_     \______   \ __ __   ____   
#  /   |   \ _/ __ \ \__  \ \   __\     |       _/|  |  \ /    \  
# /    |    \\  ___/  / __ \_|  |       |    |   \|  |  /|   |  \ 
# \____|__  / \___  >(____  /|__|       |____|_  /|____/ |___|  / 
#         \/      \/      \/                   \/             \/  
                                                                
from tkinter import CENTER
from xmlrpc.client import FastUnmarshaller
import pygame
from sys import exit
from random import randint

def display_score():

    
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    text_surface = test_font.render(f'Score:{current_time}',False,(64,64,64))
    text_rect = text_surface.get_rect(center =(400,50))
    screen.blit(text_surface,text_rect)
    return current_time

def obstacle_movement(obstacal_list):
    if obstacal_list:
        for obstacle_rect in obstacal_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surface,obstacle_rect)
            else: screen.blit(fly_surface,obstacle_rect)

        obstacal_list = [obstacle for obstacle in obstacal_list if obstacle.x > -100]

        return obstacal_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Neat Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Obstacles
sky_surface = pygame.image.load('graphics/sky1.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

fly_surface = pygame.image.load('graphics/fly/fly1.png').convert_alpha()


obstacle_rect_list = []

# text_surface = test_font.render('Neat Run', False,(64,64,64))
# text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0, 2)
player_stand_rect = player_stand.get_rect(center=(400,200))

game_name = test_font.render('Neat Run', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_maker = test_font.render('Made By Sleet', False,(111,196,169))
game_maker_rect = game_maker.get_rect(center = (400,360))

game_message = test_font.render('Press Space To Run', False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,310))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos)and player_rect.bottom >= 300:
                    player_gravity = -20
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
       
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
        else:
            obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))

        
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec', text_rect)
        # pygame.draw.rect(screen,'#c0e8ec', text_rect, 15)
        # screen.blit(text_surface,text_rect)
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface,(snail_rect))



        #player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface,(player_rect))

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collisions
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render (f'Your Score:{score}', False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)
        screen.blit(game_maker,game_maker_rect)

        if score == 0:
            screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message,score_message_rect)


    # keys = pygame.key.get_pressed()
    # if keys pygame.K_SPACE:
    #     print('jump')



    # if player_rect.colliderect(snail_rect):
    #     print('collision')
        
    

    

    pygame.display.update()
    clock.tick(60)