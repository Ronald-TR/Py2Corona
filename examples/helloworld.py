from Py2Corona.Classes import display, Text, Button
from Py2Corona.Consts import CENTER_Y

display.path = r'C:\Users\PROG-01\Documents\Corona Projects\py2corona\main.lua' # replace with the main.lua path created by your Corona SDK project
hello = Text(text='Hello World, Py2Corona!')
btn = Button(label='My button', font='FRSCRIPT.ttf', fontSize=35)
btn.left = 60
btn.top = CENTER_Y + 20

display.add(hello)
display.add(btn)
display.compile()

