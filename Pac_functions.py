import pygame, time, Pac_variables
from pygame.locals import *
from Pac_variables import *
from random import randint

############################FUNCOES####################################
def Moviment(direction, pacman):
    if direction == 1:
        pacman = [pacman[0], pacman[1]-side] 
    if direction == 2:
        pacman = [pacman[0]+side, pacman[1]]
    if direction == 3:
        pacman = [pacman[0], pacman[1]+side] 
    if direction == 4:
        pacman = [pacman[0]-side, pacman[1]]
    return pacman

def Teletransport(pacman):
    #[544, 256] and [0, 256]
    if pacman[0] == 0 and pacman[1] == 256:
        map[int(pacman[1] / side)][int(pacman[0] / side)] = 0
        screen.blit(map_blank,(int(pacman[0]), int(pacman[1])))
        pacman[0] = 576
    elif pacman[0] == 576 and pacman[1] == 256:
        map[int(pacman[1] / side)][int(pacman[0] / side)] = 0
        screen.blit(map_blank,(int(pacman[0]), int(pacman[1])))
        pacman[0] = 0
    return pacman

def eat_little(score, pacman):
    if int(map[int(pacman[1] / side)][int(pacman[0] / side)]) == 9:
        score +=10
    map[int(pacman[1] / side)][int(pacman[0] / side)] = 0
    screen.blit(map_blank,(int(pacman[0]), int(pacman[1])))
    return score

def Collision_wall(pacman, direction):    
    if direction == 1:
        pacman = (pacman[0], pacman[1]-side) 
    elif direction == 2:
        pacman = (pacman[0]+side, pacman[1]) 
    elif direction == 3:
        pacman = (pacman[0], pacman[1]+side) 
    elif direction == 4:
        pacman = (pacman[0]-side, pacman[1])
    
    if map[int(pacman[1] / side)][int(pacman[0] / side)] == 9.2 or map[int(pacman[1] / side)][int(pacman[0] / side)] == 7.2 or map[int(pacman[1] / side)][int(pacman[0] / side)] == 0:
        return 1 
    else:
        return 0

def Draw_block(i, j):
    if map[j][i] == 9.2:
        screen.blit(pygame.image.load('Pacman/images/Bola_peq.png'), (i*side,j*side))
    elif map[j][i] == 7.2:
        screen.blit(pygame.image.load('Pacman/images/Bola_gran.png'), (i*side,j*side))
    elif map[j][i] == 8.0:
        screen.blit(pygame.image.load('Pacman/images/Centro_hor.png'), (i*side,j*side))
    elif map[j][i] == 6.1:
        screen.blit(pygame.image.load('Pacman/images/Centro_ver.png'), (i*side,j*side))
    elif map[j][i] == 3.0:
        screen.blit(pygame.image.load('Pacman/images/Borda_sup_esq.png'), (i*side,j*side))
    elif map[j][i] == 5.0:
        screen.blit(pygame.image.load('Pacman/images/Borda_sup_dir.png'), (i*side,j*side))
    elif map[j][i] == 3.2:
        screen.blit(pygame.image.load('Pacman/images/Borda_inf_esq.png'), (i*side,j*side))
    elif map[j][i] == 5.2:
        screen.blit(pygame.image.load('Pacman/images/Borda_inf_dir.png'), (i*side,j*side))
    elif map[j][i] == 7.0:
        screen.blit(pygame.image.load('Pacman/images/Canto_esq.png'), (i*side,j*side))
    elif map[j][i] == 10.0:
        screen.blit(pygame.image.load('Pacman/images/Canto_dir.png'), (i*side,j*side))
    elif map[j][i] == 6.0:
        screen.blit(pygame.image.load('Pacman/images/Canto_sup.png'), (i*side,j*side))
    elif map[j][i] == 6.2:
        screen.blit(pygame.image.load('Pacman/images/Canto_inf.png'), (i*side,j*side))
    elif map[j][i] == 3.1:
        screen.blit(pygame.image.load('Pacman/images/Borda_esq.png'), (i*side,j*side))
    elif map[j][i] == 4.0:
        screen.blit(pygame.image.load('Pacman/images/Borda_sup.png'), (i*side,j*side))
    elif map[j][i] == 5.1:
        screen.blit(pygame.image.load('Pacman/images/Borda_dir.png'), (i*side,j*side))
    elif map[j][i] == 4.2:
        screen.blit(pygame.image.load('Pacman/images/Borda_inf.png'), (i*side,j*side))
    elif map[j][i] == 7.1:
        screen.blit(pygame.image.load('Pacman/images/Centro.png'), (i*side,j*side))
    else:
        screen.blit(map_blank,(j, i))

def Draw_map():
    for i in range(0, mapy):
        for j in range(0, mapx):
            Draw_block(i, j)
    screen.blit(pygame.image.load('Pacman/images/Ghost_blue32.png'), (ghost_blue[0], ghost_blue[1]))
    screen.blit(pygame.image.load('Pacman/images/Ghost_red32.png'), (ghost_red[0], ghost_red[1]))
    screen.blit(pygame.image.load('Pacman/images/Ghost_yellow32.png'), (ghost_yellow[0], ghost_yellow[1]))

def Print_pacman(pacman):
    if time.perf_counter()%1 > 0.5:
        screen.blit(pygame.image.load('Pacman/images/pac_aberta32.png'), (pacman[0], pacman[1]))
    else: 
        screen.blit(pygame.image.load('Pacman/images/pac_fechada32.png'), (pacman[0], pacman[1]))
def Same_move(ghost):

    return ghost

def Print_ghost(ghost, direction_ghost):
    while not Collision_wall(ghost, direction_ghost):
        direction_ghost = randint(1,4)

    if map[int(ghost[1]/side)][int(ghost[0]/side)] == 0:
        print(ghost," and ", direction_ghost)
        screen.blit(map_blank,(int(ghost[1]), int(ghost[0])))
    elif map[int(ghost[1]/side)][int(ghost[0]/side)] == 9.2:
        print("entrou no coin")
        screen.blit(map_blank,(int(ghost[1]), int(ghost[0])))
        screen.blit(pygame.image.load('Pacman/images/Bola_peq.png'), (int(ghost[1]),int(ghost[0])))
    else:
        print("nada")
        screen.blit(map_blank,(int(ghost[1]), int(ghost[0])))
        screen.blit(pygame.image.load('Pacman/images/Bola_peq.png'), (int(ghost[1]),int(ghost[0])))

    pygame.display.update()
    Teletransport(ghost)
    
    if direction_ghost == 1:
        ghost = [ghost[0], ghost[1]-side] 
    elif direction_ghost == 2:
        ghost = [ghost[0]+side, ghost[1]]
    elif direction_ghost == 3:
        ghost = [ghost[0], ghost[1]+side] 
    elif direction_ghost == 4:
        ghost = [ghost[0]-side, ghost[1]]
    print(ghost," and ", direction_ghost, " final")
    return ghost

    #use python.insert() pra colocar os locais anteriores do fantasma
    #use python.remove() pra tirar locais em excesso (>4 )
    #usar isso pro fantasma nao ficar rodando no mesmo lugar
    

#######################################################################