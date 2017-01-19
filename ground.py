from game_object import Game_Object


class Ground(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'ground', screen)
        #self.sprite = pygame.image.load("imgs/Menu.png").convert()
