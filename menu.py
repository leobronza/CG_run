import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from game_object import Game_Object
import math

class Menu(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'menu_screen')
        self.screen = screen
        self.spriteStart = pygame.image.load("imgs/Menu_Start.png").convert()
        self.spriteInstructions = pygame.image.load("imgs/Menu_Instructions.png").convert()
        self.spriteQuit = pygame.image.load("imgs/Menu_Quit.png").convert()
        self.spriteInstMenu = pygame.image.load("imgs/instructions.png").convert()
        self.textureDataStart = pygame.image.tostring(self.spriteStart, "RGB", 1)
        self.textureDataInstructions = pygame.image.tostring(self.spriteInstructions, "RGB", 1)
        self.textureDataQuit = pygame.image.tostring(self.spriteQuit, "RGB", 1)
        self.textureDataInstMenu = pygame.image.tostring(self.spriteInstMenu, "RGB", 1)
        self.width, self.height = self.spriteStart.get_size()
        self.__selection = Selection()

    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, value):
        self.__selection = value

    def render(self, state):

        im = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, im)
        '''
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        '''
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        if state == 0:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width, self.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
                         self.textureDataStart)
        elif state == 1:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width, self.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
                         self.textureDataInstructions)
        elif state == 2:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width, self.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
                         self.textureDataQuit)
        elif state == 3:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width, self.height, 0, GL_RGB, GL_UNSIGNED_BYTE,
                         self.textureDataInstMenu)

        glEnable(GL_TEXTURE_2D)
        glLoadIdentity()
        '''
        gluOrtho2D(0, 800, 0, 600)
        glScale(1, -1, 1)
        glTranslatef(0, -600, 0)
        glMatrixMode(GL_MODELVIEW)
        '''
        gluPerspective(45, 1, 0.05, 100)
        glTranslatef(0, 0, -5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # creating wall for GLUT

        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-2, -2, 0.3)       # vertice esquerdo baixo
        glTexCoord2f(0, 1)
        glVertex3f(-2, 2, 0.3)          # vertice esquerdo cima
        glTexCoord2f(1, 1)
        glVertex3f(2, 2, 0.3)            # vertice direito cima
        glTexCoord2f(1, 0)
        glVertex3f(2, -2, 0.3)           # vertice direito baixo
        glEnd()

        pygame.display.flip()
        # pygame.time.wait(1000)

        '''

        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw background
        self.screen.blit(self.sprite, self.pos())
        # Draw selection
        self.screen.blit(self.selection.sprite, self.selection.pos())
        # Update screen
        pygame.display.flip()

        '''

    def loop(self):
        while True:
            self.render(self.__selection.state)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.selection.state_up()
                    if event.key == pygame.K_UP:
                        self.selection.state_down()
                    if event.key == pygame.K_RETURN:
                        if self.selection.state == self.selection.START:
                            '''
                            # Start the game
                            in_menu, score = self.game_screen.loop()
                            # Game Over
                            if in_menu:
                                self.game_over_screen.render(score)
                                in_menu = self.game_over_screen.loop()
                            '''
                            return True
                        elif self.selection.state == self.selection.INSTRUCTION:
                            '''
                            # Load the instruction Screen
                            self.instruction_screen.render()
                            in_menu = self.instruction_screen.loop()
                            '''
                            self.selection.state = self.selection.InstMenu
                        elif self.selection.state == self.selection.EXIT:
                            # Exit game
                            return False
                        elif self.selection.state == self.selection.InstMenu:
                            self.selection.state = self.selection.START

                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    return False

class Selection(Game_Object):
    def __init__(self):
        Game_Object.__init__(self, 'menu_selection')
        # self.screen = screen
        # self.sprite = pygame.image.load("imgs/SetaTemplate.jpg")
        self.START = 0
        self.INSTRUCTION = 1
        self.EXIT = 2
        self.InstMenu = 3
        self.__state = self.START
        # self.x, self.y, self.z = self.get_state_pos(self.state)
        # self.width, self.height = self.sprite.get_size()

    # Setters and getters
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    '''
    def get_state_pos(self, state):
        if state == self.START:
            return -1, 0, 0
        elif state == self.INSTRUCTION:
            return 21, 400
        elif state == self.EXIT:
            return 165, 569
        else:
            return 0, 0


    def update_position(self, state):
        self.x, self.y, self.z = self.get_state_pos(state)
    '''

    def state_up(self):
        if self.state < 2:
            self.state += 1
            # self.update_position(self.state)

    def state_down(self):
        if self.state > 0 and self.state != 3:
            self.state -= 1
            # self.update_position(self.state)
