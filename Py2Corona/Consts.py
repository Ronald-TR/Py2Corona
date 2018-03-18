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

    def __div__(self, other):
        aux = self.name + '/' + str(other)
        return aux

    def __str__(self):
        return self.name

# CONSTANTES DE OBJETOS BAIXO


RECT = 'display.newRect'
EMITER = 'display.newEmiter'
IMAGE = 'display.newImage'
IMAGE_RECT = 'display.newImageRect'
TEXT = 'display.newText'

# DIMENSOES

CENTER_X = Constantes('display.contentCenterX')
CENTER_Y = Constantes('display.contentCenterY')
CONTENT_HEIGHT = Constantes('display.contentHeight')
CONTENT_WIDTH = Constantes('display.contentWidth')
DEFAULT_FONT = Constantes('native.SystemFont')
