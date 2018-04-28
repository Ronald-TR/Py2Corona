import os
import shutil
from Py2Corona.Consts import *
from Py2Corona.utils import *
from Py2Corona.singletons import display


class WindowsFont:
    def __init__(self, name):
        self.name = name
        try:
            shutil.copy('C:\\Windows\\Fonts\\' + name, os.path.dirname(display.path))
        except PermissionError as p:
            print('Permission denied for font: ' + p.filename + ', ignoring...\n')

    def __str__(self):
        return self.name


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
        attributes = []
        if not rwords:
            rwords.append('_varname')
        values = {}
        [values.__setitem__(k, v) for k, v in aobject.__dict__.items() if k not in rwords]
        for k, v in values.items():
            if v.corona:
                if not hide_attrname:
                    attributes.append(f'\n\t{v.definition(k[1:])}')
                else:
                    attributes.append(f'\n\t{v.corona}')

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
        self._strokeWidth = Py2CAttr()
        self._strokeColor = Py2CAttr(corona=rgbToCoronaColor((0, 0, 0, 1))[1])

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
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, value):
        self._shape.corona = f'"{str(value)}"'
        self._shape.python = value

    @property
    def fillColor(self):
        return self._fillColor

    @fillColor.setter
    def fillColor(self, value):
        pure, coronaColor = rgbToCoronaColor(value)
        self._fillColor.corona = coronaColor
        self._fillColor.python = value

    @property
    def labelColor(self):
        return self._labelColor

    @labelColor.setter
    def labelColor(self, value):
        pure, coronaColor = rgbToCoronaColor(value)
        self._labelColor.corona = coronaColor
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

    @property
    def strokeWidth(self):
        return self._strokeWidth

    @strokeWidth.setter
    def strokeWidth(self, value):
        self._strokeWidth.corona = str(f'{value}')
        self._strokeWidth.python = str(value)

    @property
    def strokeColor(self):
        return self._strokeColor

    @strokeColor.setter
    def strokeColor(self, value):
        pure, coronaColor = rgbToCoronaColor(value)
        self._strokeColor.corona = coronaColor
        self._strokeColor.python = value

    def __str__(self):
        corona_attrs = Py2CAttr.signature(self)
        signature = f'\nlocal {self.varname.corona} = widget.newButton(\n{{{corona_attrs}}}\n)'
        return signature


class Text:
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        all_objects.append(obj)
        return obj

    def __init__(self, *args, **kwargs):
        self._text = Py2CAttr()
        self._x = Py2CAttr()
        self._y = Py2CAttr()
        self._width_height = Py2CAttr()
        self._font = Py2CAttr()
        self._fontSize = Py2CAttr(corona='16')
        self._varname = Py2CAttr(corona=generate_varname(self.__class__.__name__))
        self._color = ()
        for arg in kwargs:
            parg = '_' + arg
            if parg not in self.__dict__.keys():
                raise AttributeError(f'Attribute {arg} does not exists in {self.__class__.__name__}')
            setattr(self, arg, kwargs[arg])

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

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
        self._font.corona = f'"{str(value)}"'
        self._font.python = value

    @property
    def fontSize(self):
        return self._fontSize

    @fontSize.setter
    def fontSize(self, value):
        self._fontSize.corona = str(value)
        self._fontSize.python = value

    @property
    def varname(self):
        return self._varname

    @varname.setter
    def varname(self, value):
        self._varname.corona = str(value)
        self._varname.python = value

    def __str__(self):
        corona_attrs = Py2CAttr.signature(self, ['_varname', '_color'])
        signature = f'\nlocal {self.varname.corona} = display.newText(\n{{{corona_attrs}}}\n)'
        definition = ''
        if self.color:
            colors, defcolors = rgbToCoronaColor(self.color)
            definition = f'\n{self.varname.corona}:setFillColor({colors})'
        return signature + definition

    def onTap(self, event_func):
        def argsfunction(*args, **kwargs):
            obj = event_func(*args, **kwargs)
            str_event = get_event_implementation(self, obj, 'tap')
            return str_event
        return argsfunction


class ImageRect:
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj.__init__(*args, **kwargs)
        all_objects.append(obj)
        return obj

    def __init__(self, *args, **kwargs):
        self.image = None
        self._filename = Py2CAttr()
        self._width = Py2CAttr(corona=CONTENT_WIDTH)
        self._height = Py2CAttr(corona=CONTENT_HEIGHT)
        self._varname = Py2CAttr(corona=generate_varname(self.__class__.__name__))
        self._x = Py2CAttr(corona=CENTER_X)
        self._y = Py2CAttr(corona=CENTER_Y)
        for arg in kwargs:
            parg = '_' + arg
            if parg not in self.__dict__.keys():
                raise AttributeError(f'Attribute {arg} does not exists in {self.__class__.__name__}')
            setattr(self, arg, kwargs[arg])

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename.corona = f'"{str(value)}"'
        self._filename.python = str(value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width.corona = str(value)
        self._width.python = str(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height.corona = str(value)
        self._height.python = str(value)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x.corona = str(value)
        self._x.python = str(value)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y.corona = str(value)
        self._y.python = str(value)

    def __str__(self):
        if self.image:
            try:
                self.filename = f'{self._varname.corona}.png'
                self.image.save(f'{self._varname.corona}.png', 'PNG')
                shutil.copy(f'{self._varname.corona}.png', os.path.dirname(display.path))
            except Exception as E:
                pass

        corona_attrs = Py2CAttr.signature(self, ['image', '_varname', '_x', '_y'], True)
        signature = f'\nlocal {self._varname.corona} = display.newImageRect(\n{corona_attrs}\n)'
        definition = f'\n{self._varname.corona}.x={self.x.corona}\n{self._varname.corona}.y={self.y.corona}\n'
        return signature + definition

