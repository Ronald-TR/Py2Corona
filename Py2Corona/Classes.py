import os
import shutil

from Py2Corona.Py2Corona.Consts import *

r_words = ['varname', 'width', 'height']
r_code = ['filename', 'varname', 'temp_event']

def get_button_color(color):
    default_color = ','.join([(i / 255) for i in color[:-1]]) + f',{str(color[-1])}'
    over = default_color.split(',')[]

def validate_args(i, v): return (str(v) != '') and not (i in r_words)


def validate_code(i, v): return (str(v) != '') and not (i in r_code)


def class_to_code(self, CONST_TYPE):
    code = '\n'.join([f'{self.varname}.{i}={v}' for i, v in self.__dict__.items() if validate_code(i, v)])
    args = ','.join([str(v) for i, v in self.__dict__.items() if validate_args(i, v)])
    definition = f'local {self.varname} = {CONST_TYPE}({args})\n'
    return definition + code


def get_implementation(obj):
    code = '\n'.join([f'{obj.varname}.{i}={v}' for i, v in obj.__dict__.items() if validate_code(i, v)])
    if hasattr(obj, 'temp_event'):
        code += f'\n{obj.temp_event}'
        delattr(obj, 'temp_event')
    return code


def get_event_implementation(self, obj, event_type):
    return f"""\nfunction {self.varname}:{event_type}( event )
    {obj.temp_event}
    return true
    end
    {self.varname}:addEventListener("{event_type}", {self.varname})"""


class Button:
    def __init__(self, varname='', text='', textColor=(), bgColor=(), width='', height='', x='', y=''):
        self.text = text
        self.textColor = textColor
        self.bgColor =
        self.width = str(width)
        self.height = str(height)
        self.x = str(x)
        self.y = str(y)
        self.varname = varname

    def __str__(self):


class Text:
    def __init__(self, varname='', text='', x=CENTER_X, y=CENTER_Y, width='', height='', font=DEFAULT_FONT):
        self.text = f'"{text}"'
        self.x = str(x)
        self.y = str(y)
        self.width_height = f'({width}, {height})' if width != '' and height != '' else ''
        self.font = str(font)
        self.varname = varname

    def __str__(self):
        return class_to_code(self, TEXT)

    def onTap(self, event_func):
        def argsfunction(*args, **kwargs):
            obj = event_func(*args, **kwargs)
            str_event = get_event_implementation(self, obj, 'tap')
            return str_event
        return argsfunction


class ImageRect:
    def __init__(self, varname, image, width='', height='', x=CENTER_X, y=CENTER_Y):
        shutil.copy(image.filename, os.path.dirname(display.path))
        filename = image.filename.split('\\')[-1]
        self.filename = f'"{filename}"'
        self.width = str(width) if str(width) != '' else str(image.width)
        self.height = str(height) if str(height) != '' else str(image.height)
        self.varname = varname
        self.x = str(x)
        self.y = str(y)

    def __str__(self):
        return class_to_code(self, IMAGE_RECT)


class Display:
    def __init__(self):
        self.elements = []
        self.path = ''
        self.events = []

    def add(self, element):
        self.elements.append(element)

    def add_event(self, event):
        self.events.append(event)

    def compile(self):
        with open(self.path, 'wb') as fp:
            content = '\n'.join([e.__str__() for e in self.elements])
            code_events = '\n'.join([e() for e in self.events])
            fp.write(content.encode() + code_events.encode())


if not hasattr(globals(), 'display'):
    display = Display()
