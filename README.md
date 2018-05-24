[![Build Status](https://www.travis-ci.org/Ronald-TR/Py2Corona.svg?branch=master)](https://www.travis-ci.org/Ronald-TR/Py2Corona)
# Py2Corona
Transpiler from Python to Corona SDK for building Mobile Apps

# Requirements 
* Python 3.6+
* Pillow (pip install pillow)
* Corona SDK

# Install
$ pip install pyforcorona

# The principle
* It's a transpiler who have the goal to code your application in Python, and interprete/build them in Corona SDK Engine

# What you need
* To make a hello word is very simple

```Python
from Py2Corona import *
# here, you will set the path of your lua file in the project
# are two ways: the first is using the singleton display
# display.path = r'your_corona_project\main.lua'
# or, just using a single string variable
# mypath = r'your_corona_project\main.lua'

Text('Hello World, Py2Corona!')

if __name__ == '__main__':
    # if not parameter especified for the function
    # this will use the display.path directory
    py2Compile()
```

  and you'll have the behavior below:
  
![helloworld.png](https://github.com/Ronald-TR/Py2Corona/blob/master/examples/helloworld.png)


* And with a button

```Python
from Py2Corona import *

mypath = r'your_corona_project\main.lua'

hello = Text('Hello World, Py2Corona!')
btn = Button('My button')

btn.left = 60
btn.top = CENTER_Y + 20

if __name__ == '__main__':
    # if not parameter especified for the function
    # this will use the display.path directory
    py2Compile(mypath)

# you can change the color of the label and the background of your button passing a tuple in RGBA color
# btn.labelColor = (255, 255, 255, 1)
# btn.fillColor = (25, 25, 255, 1)
# the values above are the default values for Py2Corona Button Element
```

  and, the result are the below:
  
![helloworld.png](https://github.com/Ronald-TR/Py2Corona/blob/master/examples/helloworld_with_button.png)

## Build to be simple and generate clean lua code


* With the main.py example, you have physics behavior and responsive backgrounds, as shown below:

![py2corona_example](https://github.com/Ronald-TR/Py2Corona/blob/master/examples/main_example.gif)

.. to do the rest of the docs

**strict alpha**
