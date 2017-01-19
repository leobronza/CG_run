from pygame import display


class Game_Object:
    def __init__(self, name):
        self.__name = name
        self.__screen = None
        self.__sprite = None
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.listX = list()
        self.listY = list()
        self.listZ = list()
        self.__is2D = True
        self.__is3D = False
        self.__width = 0
        self.__height = 0
        self.__thickness = 0

    # Setters and Getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, value):
        self.__sprite = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value

    @property
    def is2D(self):
        return self.__is2D

    @is2D.setter
    def is2D(self, value):
        self.__is2D = value

    @property
    def is3D(self):
        return self.__is3D

    @is3D.setter
    def is3D(self, value):
        self.__is3D = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def thickness(self):
        return self.__thickness

    @thickness.setter
    def thickness(self, value):
        self.__thickness = value


    def pos(self):
        return self.x, self.y, self.z

    def update_pos(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def get_screen_size(self):
        display_info = display.Info()
        return display_info.current_w, display_info.current_h

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self.name)


