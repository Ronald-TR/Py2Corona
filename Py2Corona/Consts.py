class Constantes:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        aux = self.name + '+' + str(other)
        return aux

    def __sub__(self, other):
        aux = self.name + '-' + str(other)
        return aux

    def __mul__(self, other):
        aux = self.name + '*' + str(other)
        return aux

    def __floordiv__(self, other):
        aux = self.name + '/' + str(other)
        return aux

    def __truediv__(self, other):
        aux = self.name + '/' + str(other)
        return aux

    def __str__(self):
        return self.name

# CLASS OBJECT CONSTANTS

RECT = 'display.newRect'
EMITER = 'display.newEmiter'
IMAGE = 'display.newImage'
IMAGE_RECT = 'display.newImageRect'
TEXT = 'display.newText'

# CONSTANTS OF DIMENSIONS

CENTER_X = Constantes('display.contentCenterX')
CENTER_Y = Constantes('display.contentCenterY')
CONTENT_HEIGHT = Constantes('display.contentHeight')
CONTENT_WIDTH = Constantes('display.contentWidth')
DEFAULT_FONT = Constantes('native.SystemFont')
