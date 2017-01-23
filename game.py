import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from ground import Ground

def CanTurn(side, groundCurrent, groundCurrentPlus):
    if side == 0:
        if grounds[groundCurrent].dir == 0 and grounds[groundCurrentPlus].dir == 3:
            return True
        if grounds[groundCurrent].dir == 1 and grounds[groundCurrentPlus].dir == 0:
            return True
        if grounds[groundCurrent].dir == 2 and grounds[groundCurrentPlus].dir == 1:
            return True
        if grounds[groundCurrent].dir == 3 and grounds[groundCurrentPlus].dir == 2:
            return True
    else:
        if grounds[groundCurrent].dir == 0 and grounds[groundCurrentPlus].dir == 1:
            return True
        if grounds[groundCurrent].dir == 1 and grounds[groundCurrentPlus].dir == 2:
            return True
        if grounds[groundCurrent].dir == 2 and grounds[groundCurrentPlus].dir == 3:
            return True
        if grounds[groundCurrent].dir == 3 and grounds[groundCurrentPlus].dir == 0:
            return True

ground0 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (2, 2, 2, 2, 5, 5, 5, 5),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground1 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-3, -3, -3, -3, 0, 0, 0, 0),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground2 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-6, -6, -6, -6, -3, -3, -3, -3),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground3 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-9, -9, -9, -9, -6, -6, -6, -6),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground4 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-12, -12, -12, -12, -9, -9, -9, -9),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground5 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-15, -15, -15, -15, -12, -12, -12, -12),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground6 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-18, -18, -18, -18, -15, -15, -15, -15),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground7 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-21, -21, -21, -21, -18, -18, -18, -18),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground8 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-24, -24, -24, -24, -21, -21, -21, -21),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground9 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-27, -27, -27, -27, -24, -24, -24, -24),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground10 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-30, -30, -30, -30, -27, -27, -27, -27),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground11 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-33, -33, -33, -33, -30, -30, -30, -30),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground12 = Ground((1.5, 1.5, -1.5, -1.5, 1.5, 1.5, -1.5, -1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)
ground13 = Ground((4.5, 4.5, 1.5, 1.5, 4.5, 4.5, 1.5, 1.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 1)
ground14 = Ground((7.5, 7.5, 4.5, 4.5, 7.5, 7.5, 4.5, 4.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 1)
ground15 = Ground((10.5, 10.5, 7.5, 7.5, 10.5, 10.5, 7.5, 7.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 1)
ground16 = Ground((13.5, 13.5, 10.5, 10.5, 13.5, 13.5, 10.5, 10.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 1)
ground17 = Ground((16.5, 16.5, 13.5, 13.5, 16.5, 16.5, 13.5, 13.5), (-1, 0.15, 0.15, -1, -1, 0.15, -1, 0.15), (-36, -36, -36, -36, -33, -33, -33, -33),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 1)
grounds = (ground0, ground1, ground2, ground3, ground4, ground5, ground6, ground7, ground8, ground9, ground10, ground11, ground12, ground13, ground14, ground15, ground16,ground17)

groundP = Ground((0.1, 0.1, -0.1, -0.1, 0.1, 0.1, -0.1, -0.1), (0.15, 0.6, 0.6, 0.15, 0.15, 0.6, 0.15, 0.6), (0.1, 0.1, 0.1, 0.1, 0, 0, 0, 0),((0,1,2,3),(3,2,7,6),(6,7,5,4),(4,5,1,0),(1,5,7,2),(4,0,3,6)), 0)

def Player():
    glColor3b(1, 0, 0)
    glBegin(GL_QUADS)
    for surface in groundP.surface:
        for vertex in surface:
            glVertex3fv((groundP.listX[vertex], groundP.listY[vertex], groundP.listZ[vertex]))
    glEnd()

# def PlayerKeepMoving(player):


def MovGrounds(groundCurrentPlus):
    if (grounds[groundCurrentPlus].dir == 0):
        for ground in grounds:
            for i in range(0, len(ground.listZ)):
                listz = list(ground.listZ)
                listz[i] = listz[i] + 0.1
                ground.listZ = listz
    elif (grounds[groundCurrentPlus].dir == 1):
        for ground in grounds:
            for i in range(0, len(ground.listX)):
                listx = list(ground.listX)
                listx[i] = listx[i] - 0.1
                ground.listX = listx
    elif (grounds[groundCurrentPlus].dir == 2):
        for ground in grounds:
            for i in range(0, len(ground.listZ)):
                listz = list(ground.listZ)
                listz[i] = listz[i] - 0.1
                ground.listZ = listz
    elif (grounds[groundCurrentPlus].dir == 3):
        for ground in grounds:
            for i in range(0, len(ground.listX)):
                listx = list(ground.listX)
                listx[i] = listx[i] + 0.1
                ground.listX = listx

# Printa os Grounds
def Grounds():
    glColor3b(0, 1, 0)
    glBegin(GL_QUADS)
    for ground in grounds:
        for surface in ground.surface:
            for vertex in surface:
                glVertex3fv((ground.listX[vertex], ground.listY[vertex], ground.listZ[vertex]))
    glEnd()

# Funcao Principal
def Game():
    glTranslatef(0, -0.5, -5)
    glRotatef(12, 1, 0, 0)
    contaux = 0
    groundCurrent = 1
    margem = 0
    wait4right = False
    wait4left = False

    while True:
        if groundCurrent == 17:
            groundCurrentPlus = 0
        else:
            groundCurrentPlus = groundCurrent + 1

        if groundCurrentPlus == 17:
            groundCurrentPlusPlus = 0
        else:
            groundCurrentPlusPlus = groundCurrentPlus + 1

        # Captura teclas
        for event in pygame.event.get():
            # Finaliza se Pressinado "Esc" ou fechado a janela
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                quit()
            # Vira camera ao pressinar LEFT
            elif event.type == KEYUP and event.key == K_LEFT:
                if grounds[groundCurrent].dir != grounds[groundCurrentPlusPlus].dir:
                    wait4left = True
                if CanTurn(0, groundCurrent, groundCurrentPlus) == True:
                    glRotatef(-90, 0, 1, 0)
                    grounds[groundCurrent].dir = grounds[groundCurrentPlus].dir
                    contaux = 1.5
            # Vira camera ao pressinar RIGHT
            elif event.type == KEYUP and event.key == K_RIGHT:
                if CanTurn(1, groundCurrent, groundCurrentPlus ) == True:
                    wait4right = True
                    # if margem > 1.5:
                    #     pass



        if(grounds[groundCurrent].dir == grounds[groundCurrentPlus].dir):
            # Atualizacao posicao dos Grounds
            MovGrounds(groundCurrentPlus)

            # Atualiza qual eh o bloco atual
            if contaux >= 3:
                if groundCurrent == 17:
                    groundCurrent = 0
                    contaux = 0.1
                else:
                    groundCurrent = groundCurrent + 1
                    contaux = 0.1
            else:
                contaux = contaux + 0.1
        # elif grounds[groundCurrent].dir != grounds[groundCurrentPlusPlus].dir:
        #     # vai precisar fazer a curva
        #     pass
        #

        else:

            if wait4right and margem >= 1.5:
                glRotatef(90, 0, 1, 0)
                grounds[groundCurrent].dir = grounds[groundCurrentPlus].dir
                contaux = 1.5
                wait4right = False

            if margem < 1.5:
                MovGrounds(groundCurrent)
                margem = margem + 0.1
                # if wait4right:



            # if margem >= 1.5:
            #     if groundCurrent == 17:
            #         groundCurrent = 0
            #         contaux = 1.6
            #     else:
            #         groundCurrent = groundCurrent + 1
            #         contaux = 1.6
            #     margem = 0
            # else:
            #     MovGrounds(groundCurrent)
            #     margem = margem + 0.1


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Grounds()
        Player()
        pygame.display.flip()
        #pygame.time.wait(50)
