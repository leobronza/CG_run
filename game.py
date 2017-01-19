import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from ground import Ground


def CanTurn(side, dir):
    if(dir == 1 or dir == 3):
        if (side == 0):
            for ground in grounds:
                pass
        else:
            for ground in grounds:
                pass
    #olhar eixo x
    elif(dir == 0 or dir == 2):
        #olha eixo x negativo
        if (side == 0):
            for ground in grounds:
                for i in range(0, 8):
                    listx = list(ground.listX)
                    listz = list(ground.listZ)
                    if -3 in listx:
                        for z in listz:
                            if (z == 0.7):
                                return True;
        #olhar eixo x positivo
        else:
            for ground in grounds:
                for i in range(0, 8):
                    listx = list(ground.listX)
                    listz = list(ground.listZ)
                    if 3 in listx:
                        for z in listz:
                            if( z > 0.7):
                                 return True;

ground0 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (1, 1, 1, 1, 3, 3, 3, 3),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground1 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-1, -1, -1, -1, 1, 1, 1, 1),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground2 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-3, -3, -3, -3, -1, -1, -1, -1),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground3 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-5, -5, -5, -5, -3, -3, -3, -3),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground4 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-7, -7, -7, -7, -5, -5, -5, -5),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground5 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-9, -9, -9, -9, -7, -7, -7, -7),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground6 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-11, -11, -11, -11, -9, -9, -9, -9),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground7 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-13, -13, -13, -13, -11, -11, -11, -11),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground8 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-15, -15, -15, -15, -13, -13, -13, -13),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground9 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-17, -17, -17, -17, -15, -15, -15, -15),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground10 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-19, -19, -19, -19, -17, -17, -17, -17),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground11 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-21, -21, -21, -21, -19, -19, -19, -19),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground12 = Ground((1, 1, -1, -1, 1, 1, -1, -1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground13 = Ground((3, 3, 1, 1, 3, 3, 1, 1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground14 = Ground((5, 5, 3, 3, 5, 5, 3, 3), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground15 = Ground((7, 7, 5, 5, 7, 7, 5, 5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground16 = Ground((9, 9, 7, 7, 9, 9, 7, 7), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground17 = Ground((11, 11, 9, 9, 11, 11, 9, 9), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
ground18 = Ground((-3, -3, 1, 1, -3, -3, 1, 1), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-23, -23, -23, -23, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)))
grounds = (ground0, ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8, ground9, ground10, ground11, ground12, ground13, ground14, ground15, ground16,ground17, ground18)
def Grounds():
    glColor3b(0, 1, 0);
    glBegin(GL_QUADS)
    for ground in grounds:
        for surface in ground.surface:
            for vertex in surface:
                glVertex3fv((ground.listX[vertex], ground.listY[vertex], ground.listZ[vertex]))
    glEnd()


def Game():

    glTranslatef(0, -0.4, -5)
    glRotatef(12, 1, 0, 0)
    dir = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                quit()
            elif event.type == KEYUP and event.key == K_LEFT:
                if(CanTurn(0, dir) == True):
                    if(dir == 0):
                        dir = 3
                    else:
                        dir = dir -1
                    glRotatef(-90, 0, 1, 0)
            elif event.type == KEYUP and event.key == K_RIGHT:
                if (CanTurn(1, dir) == True):
                    if ( dir == 3):
                        dir = 0
                    else:
                        dir = dir + 1
                    glRotatef(90, 0, 1, 0)


        #Atualizacao Grounds
        if(dir == 0):
            for ground in grounds:
                for i in range(0, len(ground.listZ)):
                    listz = list(ground.listZ)
                    listz[i] = listz[i] + 0.1
                    ground.listZ = listz
        elif(dir == 1):
            for ground in grounds:
                for i in range(0, len(ground.listX)):
                    listx = list(ground.listX)
                    listx[i] = listx[i] - 0.1
                    ground.listX = listx
        elif (dir == 2):
            for ground in grounds:
                for i in range(0, len(ground.listZ)):
                    listz = list(ground.listZ)
                    listz[i] = listz[i] - 0.1
                    ground.listZ = listz
        elif (dir == 3):
            for ground in grounds:
                for i in range(0, len(ground.listX)):
                    listx = list(ground.listX)
                    listx[i] = listx[i] + 0.1
                    ground.listX = listx

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Grounds()
        pygame.display.flip()
        #pygame.time.wait(50)
