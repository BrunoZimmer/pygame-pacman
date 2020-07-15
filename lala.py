import pygame, time
from pygame.locals import *
############################FUNCOES####################################

def Moviment(direction):
    if direction == 1:
        print(pacman)
        pacman = (pacman[0], pacman[1]-side) 
        print(pacman)
    if direction == 2:
        pacman = (pacman[0]+side, pacman[1]) 
    if direction == 3:
        pacman = (pacman[0], pacman[1]+side) 
    if direction == 4:
        pacman = (pacman[0]-side, pacman[1])

def Draw_map():
    for i in range(0, mapy):
        for j in range(0, mapx):
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
            elif map[j][i] == 9.0:
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
            elif map[j][i] == -1:
                pass
            else:
                screen.blit(pygame.image.load('Pacman/images/Chao.png'), (i*side,j*side))

#######################################################################

#Map variable (19 x 19)
#Which tileset file is 32x32 pixels
#9.2 = little coin
#7.2 = big coin
#-1 = Solo


map = [
(3.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,4.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,5.0)
,(6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1)
,(6.1,7.2,7.0,9.0,9.2,7.0,8.0,9.0,9.2,6.2,9.2,7.0,8.0,9.0,9.2,7.0,9.0,7.2,6.1)
,(6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1)
,(6.1,9.2,7.0,9.0,9.2,6.0,9.2,7.0,8.0,4.0,8.0,9.0,9.2,6.0,9.2,7.0,9.0,9.2,6.1)
,(6.1,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,6.1)
,(3.2,8.0,8.0,5.0,9.2,3.1,8.0,9.0,9.2,6.2,9.2,7.0,8.0,5.1,9.2,3.0,8.0,8.0,5.2)
,(8.0,8.0,8.0,5.2,9.2,6.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.2,9.2,3.2,8.0,8.0,8.0)
,(9.2,9.2,9.2,9.2,9.2,9.2,9.2,3.0,8.0,-1,8.0,5.0,9.2,9.2,9.2,9.2,9.2,9.2,9.2)
,(8.0,8.0,8.0,5.0,9.2,6.0,9.2,6.1,-1,-1,-1,6.1,9.2,6.0,9.2,3.0,8.0,8.0,8.0)
,(3.0,8.0,8.0,5.2,9.2,6.2,9.2,3.2,8.0,8.0,8.0,5.2,9.2,6.2,9.2,3.2,8.0,8.0,5.0)
,(6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1)
,(6.1,9.2,7.0,4.0,8.0,9.0,9.2,6.0,9.2,7.1,9.2,6.0,9.2,7.0,8.0,4.0,9.0,9.2,6.1)
,(6.1,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,6.1)
,(3.1,9.0,9.2,6.2,9.2,6.0,9.2,3.2,8.0,8.0,8.0,5.2,9.2,6.0,9.2,6.2,9.2,7.0,5.1)
,(6.1,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,6.1)
,(6.1,7.2,7.0,8.0,8.0,4.2,8.0,8.0,8.0,8.0,8.0,8.0,8.0,4.2,8.0,8.0,9.0,7.2,6.1)
,(6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1)
,(3.2,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,5.2)
]



#Pacman coord
pacman = [(288,544)]

vel = 20
run = True
direction = 1
side = 32
x = 20
y = 20
width = 608
height = 608
mapx = 19
mapy = 19

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("PAC-MAN")


while run:
    keys = pygame.key.get_pressed()
    #Actions in the game
    for event in pygame.event.get() :
        #leave the game by the "X"
        if event.type == pygame.QUIT :
            run = False
        #Move
        if keys[pygame.K_LEFT]:
            direction = 1
        if keys[pygame.K_RIGHT]:
            direction = 2
        if keys[pygame.K_UP]:
            direction = 3
        if keys[pygame.K_DOWN]:
            direction = 4
            
    Moviment(direction)

    screen.fill((0, 0, 0))
    Draw_map()

    if time.perf_counter()%0.4 > 0.2:
        screen.blit(pygame.image.load('Pacman/images/pac_aberta32.png'), (pacman[0], pacman[1]))
    else: 
        screen.blit(pygame.image.load('Pacman/images/pac_fechada32.png'), (pacman[0], pacman[1]))

    pygame.display.update()


pygame.quit()