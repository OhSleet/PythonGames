# imports
import pygame
import time
import random
import sys

pygame.init()

# Screen + Font
Screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Reaction Time!")

font = pygame.font.SysFont("Roboto", 90)
# Title
title = font.render("Reaction Time Game" , True, "blue")
title_rect = title.get_rect(center=(360, 50))

# Click to Start
click_to_start = font.render("Click To Start" , True, "black")
click_to_start_rect = click_to_start.get_rect(center=(360, 360))


# Waiting
waiting = font.render("Wait..." , True, "black")
waiting_rect = waiting.get_rect(center=(360, 360))


# Click
click = font.render("CLICK NOW!" , True, "black")
click_rect = click.get_rect(center=(360, 360))


# Score
score = font.render("Score :1000ms" , True, "black")
score_rect = score.get_rect(center=(360, 360))


# Game Score
game_state = "Click To Start"

# Made By
mat = font.render("Made By Matt" , True, "blue")#
mat_rect = mat.get_rect(center = (360, 680))

# Times
start_time, end_time = 0, 0



#Game loop
while True:
    # Events and buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Click To Start":
                game_state = "Waiting"
            elif game_state == "Test Starting":
                    end_time = time.time()
                    game_state = "Showing Results"
            elif game_state == "Showing Results":
                game_state = "Click To Start"


        Screen.fill("white")

        Screen.blit(title, title_rect)
        Screen.blit(mat, mat_rect)

    # Game State Logic
    if game_state == "Click To Start":
        Screen.blit(click_to_start, click_to_start_rect)
    elif game_state == "Waiting":
        Screen.fill("yellow")

        Screen.blit(waiting, waiting_rect)

        pygame.display.update()

        delay_time = random.uniform(1, 10)
        
        time.sleep(delay_time)

        game_state = "Test Starting"

        starting_time = time.time()
    elif game_state == "Test Starting":
        Screen.fill("green")
        Screen.blit(click, click_rect)
    elif game_state == "Showing Results":
        reaction_time = round((end_time - starting_time) * 1000)
        score_text = font.render(f"Speed: {reaction_time} ms", True, "black")
        Screen.blit(score_text, score_rect)






    # Update Display
    pygame.display.update()









