from Py2Corona.singletons import display
from random import randrange
import string

all_chars = string.ascii_lowercase + string.digits
all_objects = []
var_words = []
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


def rgbToCoronaColor(color):
    if not type(color) is tuple:
        raise AttributeError(f'The Color Attribute expect a tuple with (r, g, b, alpha), but {type(color)} was received.')

    default_color = ','.join([str(i / 255)[:5] for i in color[:-1]]) + f',{str(color[-1])}'
    aux = default_color.split(',')
    aux[-1] = str(float(aux[-1]) - 0.1)[:3]
    over = ','.join(aux)
    return default_color, '{default={' + default_color + '}, over={'+over+'}}'


def generate_varname(name: "Este é o nome da classe"):
    rword = name.lower() + '_'
    for i in range(7):
        n = randrange(len(all_chars))
        rword += all_chars[n]
    if rword not in var_words:
        var_words.append(rword)
    else:
        generate_varname(name)
    return rword


def py2Compile(path=None):
    # need to add code_events in the compilation
    if not path:
        path = display.path
    with open(path, 'wb') as fp:
        fp.write('widget = require("widget")\n'.encode())
        for o in all_objects:
            fp.write(str(o).encode())
