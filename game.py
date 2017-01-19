import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies0 = (
    (1, -1, 1),
    (1, 0.15,  1),
    (-1, 0.15, 1),
    (-1, -1, 1),
    (1, -1, 3),
    (1, 0.15, 3),
    (-1, -1, 3),
    (-1, 0.15, 3),
)

verticies = (
    (1, -1, -1),
    (1, 0.15,  -1),
    (-1, 0.15, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 0.15, 1),
    (-1, -1, 1),
    (-1, 0.15, 1),
)
verticies2 = (
    (1, -1, -3),
    (1, 0.15,  -3),
    (-1, 0.15, -3),
    (-1, -1, -3),
    (1, -1, -1),
    (1, 0.15, -1),
    (-1, -1, -1),
    (-1, 0.15, -1),
)
verticies3 = (
    (1, -1, -5),
    (1, 0.15,  -5),
    (-1, 0.15, -5),
    (-1, -1, -5),
    (1, -1, -3),
    (1, 0.15, -3),
    (-1, -1, -3),
    (-1, 0.15, -3),
)
verticies4 = (
    (1, -1, -7),
    (1, 0.15,  -7),
    (-1, 0.15, -7),
    (-1, -1, -7),
    (1, -1, -5),
    (1, 0.15, -5),
    (-1, -1, -5),
    (-1, 0.15, -5),
)


surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
)

def Cube():
    glColor3b(0, 1, 0);
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies0[vertex])

    glColor3b(0, 0, 1);
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies[vertex])

    glColor3b(1, 0, 0 );
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies2[vertex])

    glColor3b(1, 1, 0);
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies3[vertex])

    glColor3b(0, 1, 1);
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies4[vertex])


    glEnd()



def Game():
    glTranslatef(0, 0, -5)

    glRotatef(12, 1, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                quit()

        glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)
