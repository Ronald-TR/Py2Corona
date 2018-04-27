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
    # singleton definition
    display = Display()
