from game_object import Game_Object


class Ground(Game_Object):
    def __init__(self, listx, listy, listz, surface, dir):
        Game_Object.__init__(self, 'ground')
        #self.sprite = pygame.image.load("imgs/Menu.png").convert()
        self.is2D = False
        self.is3D = True
        self.listX = listx
        self.listY = listy
        self.listZ = listz
        self.surface = surface
        self.dir = dir