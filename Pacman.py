import Pac_functions, Pac_variables
from Pac_variables import * 
from Pac_functions import * 

pygame.init()
pygame.display.set_caption("PAC-MAN")
screen.fill(map_color)
Draw_map()
while run:
    #Actions in the game
    for event in pygame.event.get() :
        #leave the game by the "X"
        if event.type == pygame.QUIT :
            run = False
        #Move
        if event.type == KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP] and Collision_wall(pacman, 1):
                direction = 1
            if pygame.key.get_pressed()[pygame.K_RIGHT] and Collision_wall(pacman, 2):
                direction = 2
            if pygame.key.get_pressed()[pygame.K_DOWN] and Collision_wall(pacman, 3):
                direction = 3
            if pygame.key.get_pressed()[pygame.K_LEFT] and Collision_wall(pacman, 4):
                direction = 4

    #testing move of pacman
    time_now_pac = pygame.time.get_ticks()
    if Collision_wall(pacman, direction) and (time_now_pac - time_passed_pac) > 500:
        score = eat_little(score, pacman)
        pacman = Moviment(direction, pacman)
        Teletransport(pacman)
        Print_pacman(pacman)
        
        time_passed_pac = time_now_pac 
    
    #Allow ghosts to go
    if int(time.perf_counter()) > 5:
        blue = 1
    if int(time.perf_counter()) > 10:

        red = 1
    if int(time.perf_counter()) > 15:
        yellow = 1

    #Printing ghosts
    time_now_ghost = pygame.time.get_ticks()
    if (time_now_ghost -time_passed_ghost) > 800:
        if blue==1:
            ghost_blue = [9*side, 7*side]
            ghost_blue = Print_ghost(ghost_blue, direction_ghost_blue)
            screen.blit(pygame.image.load('Pacman/images/Ghost_blue32.png'), (ghost_blue[0], ghost_blue[1]))
        """ if red==1:
            ghost_red = [9*side, 8*side]
            ghost_red = Print_ghost(ghost_red, direction_ghost_red)
            screen.blit(pygame.image.load('Pacman/images/Ghost_red32.png'), (ghost_red[0], ghost_red[1]))
        if yellow==1:
            ghost_yellow= [9*side, 8*side]
            ghost_yellow = Print_ghost(ghost_yellow, direction_ghost_yellow)
            screen.blit(pygame.image.load('Pacman/images/Ghost_yellow32.png'), (ghost_yellow[0], ghost_yellow[1]))"""
        time_passed_ghost = time_now_ghost 
    #print(pygame.time.get_ticks())
    pygame.display.update()
pygame.quit()