#Bibliotecas
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#Classes
from main import Main

#Variaveis globais
display = (800, 600)

#Luz ambiente e sombra
def ambient():
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_POSITION, (0, 1, 1, 0))

#Funcao Configuracoes da visao/display
def resize():
    # Normaliza as cordenadas do dispositivo para as da janela
    glViewport(0, 0, display[0], display[1])
    #Define o angulo do zoom, o tamanho do visor, a distancia da tela e a distancia do final da tela
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)

#Funcao Principal
def run():
    #Inicia a janela do pygame
    pygame.init()
    #Define o tamanho da janela e configuracoes
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    #Configuracoes da visao/display
    resize()
    #Define mouse como invisivel
    #pygame.mouse.set_visible(0)
    #Luz ambiente e sombra
    ambient()
    #chamada da main
    Main(screen)

#inicial
run()