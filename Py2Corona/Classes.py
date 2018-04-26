import os
import shutil

from Py2Corona.Consts import *
from Py2Corona.utils import *


class Py2CAttr:
    def __init__(self, *args, **kwargs):
        self.python = ''
        self.corona = ''
        for arg in kwargs:
            if not arg in self.__dict__.keys():
                msg = f'Attribute "{arg}" does not exists'
                raise AttributeError(msg)
            setattr(self, arg, kwargs[arg])

    def definition(self, attrname):
        return f'{attrname}={self.corona}'

    @staticmethod
    def signature(aobject, rwords=[], hide_attrname=False):
        if not rwords:
            rwords.append('_varname')
        if not hide_attrname:
            attributes = [v.definition(k[1:]) for k, v in aobject.__dict__.items() if v.corona and not k in rwords]
        else:
            attributes = [v.corona for k, v in aobject.__dict__.items() if v.corona and not k in rwords]

        return ','.join(attributes)

    def __str__(self):
        return self.__dict__.__str__()


class Button:
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        all_objects.append(obj)
        return obj

    def __init__(self, *args, **kwargs):
        self._varname = Py2CAttr(corona=generate_varname(self.__class__.__name__))
        self._label = Py2CAttr()
        self._top = Py2CAttr()
        self._left = Py2CAttr()
        self._fillColor = Py2CAttr()
        self._labelColor = Py2CAttr()
        self._width = Py2CAttr(corona='200')
        self._height = Py2CAttr(corona='40')
        self._emboss = Py2CAttr(corona='false')
        self._shape = Py2CAttr(corona='"roundedRect"')
        self._font = Py2CAttr(corona=DEFAULT_FONT)
        self._fontSize = Py2CAttr(corona='16')

        for arg in kwargs:
            parg = '_' + arg
            if parg not in self.__dict__.keys():
                raise AttributeError(f'Attribute {arg} does not exists in {self.__class__.__name__}')
            setattr(self, arg, kwargs[arg])

    @property
    def varname(self):
        return self._varname

    @varname.setter
    def varname(self, value):
        self._varname.corona = generate_varname(self.__class__.__name__ or value)
        self._varname.python = value

    @property
    def fillColor(self):
        return self._fillColor

    @fillColor.setter
    def fillColor(self, value):
        self._fillColor.corona = rgbToCoronaColor(value)
        self._fillColor.python = value

    @property
    def labelColor(self):
        return self._labelColor

    @labelColor.setter
    def labelColor(self, value):
        self._labelColor.corona = rgbToCoronaColor(value)
        self._labelColor.python = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value):
        self._label.corona = f'"{str(value)}"'
        self._label.python = str(value)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top.corona = str(value)
        self._top.python = str(value)

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left.corona = str(value)
        self._left.python = str(value)

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font.corona = str(f'"{value}"')
        self._font.python = str(value)

    @property
    def fontSize(self):
        return self._fontSize

    @fontSize.setter
    def fontSize(self, value):
        self._fontSize.corona = str(f'{value}')
        self._fontSize.python = str(value)

    def __str__(self):
        corona_attrs = Py2CAttr.signature(self).replace(',', ',\n')
        signature = f'local {self.varname.corona} = widget.newButton({{{corona_attrs}}})'
        return signature


class Text:
    def __init__(self, *args, **kwargs):
        self._text = Py2CAttr()
        self._x = Py2CAttr()
        self._y = Py2CAttr()
        self._width_height = Py2CAttr()
        self._font = Py2CAttr()
        self._varname = Py2CAttr(corona=generate_varname(self.__class__.__name__))
        for arg in kwargs:
            parg = '_' + arg
            if parg not in self.__dict__.keys():
                raise AttributeError(f'Attribute {arg} does not exists in {self.__class__.__name__}')
            setattr(self, arg, kwargs[arg])

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text.corona = f'"{str(value)}"'
        self._text.python = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x.corona = str(value)
        self._x.python = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y.corona = str(value)
        self._y.python = value

    @property
    def width_height(self):
        return self._width_height

    @width_height.setter
    def width_height(self, value):
        self._width_height.corona = str(value)
        self._width_height.python = value

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value):
        self._font.corona = str(value)
        self._font.python = value

    @property
    def varname(self):
        return self._varname

    @varname.setter
    def varname(self, value):
        self._varname.corona = str(value)
        self._varname.python = value

    def __str__(self):
        corona_attrs = Py2CAttr.signature(self)
        signature = f'local {self.varname.corona} = display.newText({{{corona_attrs}}})'
        return signature

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
            fp.write('widget = require("widget")\n'.encode())
            fp.write(content.encode() + code_events.encode())


if not hasattr(globals(), 'display'):
    display = Display()
