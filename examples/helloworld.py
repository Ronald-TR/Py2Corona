from Py2Corona.Py2Corona.Classes import display, Text

display.path = r'your_corona_project\main.lua'
hello = Text('hello', 'Hello World, Py2Corona!')
display.add(hello)

display.compile()

