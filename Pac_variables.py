import pygame
#Map variable (19 x 19)
#Which tileset file is 32x32 pixels
#9.2 = little coin
#7.2 = big coin
#0 = Solo

map = [
[3.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,4.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,5.0]
,[6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1]
,[6.1,7.2,7.0,10.0,9.2,7.0,8.0,10.0,9.2,6.2,9.2,7.0,8.0,10.0,9.2,7.0,10.0,7.2,6.1]
,[6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1]
,[6.1,9.2,7.0,10.0,9.2,6.0,9.2,7.0,8.0,4.0,8.0,10.0,9.2,6.0,9.2,7.0,10.0,9.2,6.1]
,[6.1,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,6.1]
,[3.2,8.0,8.0,5.0,9.2,3.1,8.0,10.0,9.2,6.2,9.2,7.0,8.0,5.1,9.2,3.0,8.0,8.0,5.2]
,[8.0,8.0,8.0,5.2,9.2,6.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.2,9.2,3.2,8.0,8.0,8.0]
,[9.2,9.2,9.2,9.2,9.2,9.2,9.2,3.0,8.0,0,8.0,5.0,9.2,9.2,9.2,9.2,9.2,9.2,9.2]
,[8.0,8.0,8.0,5.0,9.2,6.0,9.2,6.1,0,0,0,6.1,9.2,6.0,9.2,3.0,8.0,8.0,8.0]
,[3.0,8.0,8.0,5.2,9.2,6.2,9.2,3.2,8.0,8.0,8.0,5.2,9.2,6.2,9.2,3.2,8.0,8.0,5.0]
,[6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1]
,[6.1,9.2,7.0,4.0,8.0,10.0,9.2,6.0,9.2,7.1,9.2,6.0,9.2,7.0,8.0,4.0,10.0,9.2,6.1]
,[6.1,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,9.2,6.1,9.2,9.2,6.1]
,[3.1,10.0,9.2,6.2,9.2,6.0,9.2,3.2,8.0,8.0,8.0,5.2,9.2,6.0,9.2,6.2,9.2,7.0,5.1]
,[6.1,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1,9.2,9.2,9.2,9.2,6.1]
,[6.1,7.2,7.0,8.0,8.0,4.2,8.0,8.0,8.0,8.0,8.0,8.0,8.0,4.2,8.0,8.0,10.0,7.2,6.1]
,[6.1,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,0,9.2,9.2,9.2,9.2,9.2,9.2,9.2,9.2,6.1]
,[3.2,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,8.0,5.2]
]


#main variables
vel = 3
run = True
direction = 2
side = 32
x = 20
y = 20
width = 608
height = 608
mapx = 19
mapy = 19

#Pacman coord
pacman = [9*side, 17*side]
score = 0

#Ghosts coords
time_now_ghost = 0
time_passed_ghost = 0
# 10 x 10
blue = 0
ghost_blue = [9*side, 9*side]
direction_ghost_blue = 2
# 9 x 10
red = 0
ghost_red = [8*side, 9*side]
direction_ghost_red = 2
# 11 x 10
yellow = 0
ghost_yellow = [10*side, 9*side]
direction_ghost_yellow = 4

#pygame variables
screen = pygame.display.set_mode((width,height), 0, 32)
time_now_pac = 0
time_passed_pac = 0

#Map blank
map_color = (0, 0, 0)
map_blank = pygame.Surface((side,side))
map_blank.fill(map_color)