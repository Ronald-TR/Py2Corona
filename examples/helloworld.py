from Py2Corona.Classes import display, Text, Button
from Py2Corona.Consts import CENTER_Y

display.path = r'C:\py2Corona\main.lua' # replace with the main.lua path created by your Corona SDK project
hello = Text('hello', 'Hello World, Py2Corona!')
btn = Button('btn', 'My button')
btn.left = 60
btn.top = CENTER_Y + 20
display.add(hello)
display.add(btn)
display.compile()

