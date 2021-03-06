from PIL import Image as Img
from Py2Corona.Consts import *
from Py2Corona.Behaviors import Physics
from Py2Corona.Classes import display, Text, ImageRect
import os

pyPhysics = Physics('my_physics')
display.path = r'examples/output/main.lua' # replace with the main.lua path created by your Corona SDK project
print(os.getcwd())

background = ImageRect('wall', Img.open('examples/Wallpaper-Celular.jpg'), CONTENT_WIDTH, CONTENT_HEIGHT)

megaman = ImageRect('mm', Img.open('examples/Mega_Man.png'), 50, 100)
megaman.x = CENTER_X
megaman.y = CENTER_Y - 100

hello = Text('hello', 'Olá Py2Corona!')

subtitle = Text('subtitle', 'Bem vindo ao pre-compilador!', y=CENTER_Y + 20)


@hello.onTap
def megaman_jump():
    pyPhysics.addLinearImpulse(megaman, 0, 200, megaman.x, megaman.y)
    return megaman


pyPhysics\
    .add(hello, 'static', {'friction': 1})\
    .add(megaman, 'dynamic', {'density': 5, 'friction': 1, 'bounce': 0.5})


display.add_event(megaman_jump)
display.add(background)
display.add(hello)
display.add(subtitle)
display.add(megaman)
display.add(pyPhysics)

display.compile()
