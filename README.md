# Py2Corona
Transpiler from Python to Corona SDK for building Mobile Apps

# Requirements 
* Python 3.6+
* Corona SDK

# The principle
* It's a transpiler who have the goal to code your application in Python, and interprete/build them in Corona SDK Engine

# What you need
* To make a hello word it's very simple

```Python
from Py2Corona.Py2Corona.Classes import display, Text

display.path = r'your_corona_project\main.lua'
# the first parameter it's the name of your element id for Py2Corona,
# be sure to put it in every object declaration
hello = Text('hello', 'Hello World, Py2Corona!')
display.add(hello)
display.compile()

```

  and you'll have the behavior below:
  
![helloworld.png](https://github.com/Ronald-TR/Py2Corona/blob/master/examples/helloworld.png)


## All work arround display singleton


* With the main.py example, you have physics behavior and responsive backgrounds, as shown below:

![py2corona_example](https://github.com/Ronald-TR/Py2Corona/blob/master/examples/main_example.gif)

.. to do the rest of the docs

**strict alpha**
