import os
import shutil

from Py2Corona.Consts import *

r_words = ['varname', 'width', 'height']
r_code = ['filename', 'varname', 'temp_event']


def get_button_color(color):
    default_color = ','.join([str(i / 255)[:3] for i in color[:-1]]) + f',{str(color[-1])}'
    aux = default_color.split(',')
    aux[-1] = str(float(aux[-1]) - 0.1)[:3]
    over = ','.join(aux)
    return '{default={' + default_color + '}, over={'+over+'}}'


def validate_args(i, v): return (str(v) != '') and not (i in r_words)


def validate_code(i, v): return (str(v) != '') and not (i in r_code)


def class_to_code(self, CONST_TYPE):
    code = '\n'.join([f'{self.varname}.{i}={v}' for i, v in self.__dict__.items() if validate_code(i, v)])
    args = ','.join([str(v) for i, v in self.__dict__.items() if validate_args(i, v)])
    definition = f'local {self.varname} = {CONST_TYPE}({args})\n'
    return definition + code


def get_implementation(obj, add_varname = True):
    if add_varname:
        code = '\n'.join([f'{obj.varname}.{i}={v}' for i, v in obj.__dict__.items() if validate_code(i, v)])
    else:
        code = '\n'.join([f'{i}={v}' for i, v in obj.__dict__.items() if validate_code(i, v)])
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
        self.label = f'"{text}"'
        self.labelColor = get_button_color(textColor) if textColor != () else get_button_color((255, 255, 255, 1))
        self.fillColor = get_button_color(bgColor) if bgColor != () else get_button_color((25, 25, 255, 1))
        self.width = str(width) if width != '' else '200'
        self.height = str(height) if height != '' else '40'
        self.left = str(x)
        self.top = str(y)
        self.varname = varname
        self.emboss = 'false'
        self.shape = '"roundedRect"'

    def __str__(self):
        code = '{' + get_implementation(self, False).replace('\n', ',\n') + '}'
        return f'local widget = require( "widget" )\nlocal {self.varname} = widget.newButton({code})'


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
        image.save(f'{varname}.png', 'PNG')
        shutil.copy(f'{varname}.png', os.path.dirname(display.path))
        filename = f'{varname}.png' # image.filename.split('\\')[-1]
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
