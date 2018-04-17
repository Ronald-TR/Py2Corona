class Physics:
    class Element:
        def __init__(self, element, behavior, especifications=None):
            self.element = element
            self.behavior = behavior
            self.especifications = especifications
            if not especifications:
                self.especifications = {'density': 40, 'friction': 1, 'bounce': 0.5}

        def __str__(self):
            espec = self.especifications.__str__().replace(r"'", '').replace(':', '=')
            return f'{self.element.varname}, "{self.behavior}", {espec}'

    def __init__(self, varname='physics'):
        self.varname = varname
        self.elements = []

    def add(self, element, behavior, especifications=None):
        self.elements.append(self.Element(element, behavior, especifications).__str__())
        return self

    def addLinearImpulse(self, element, x, y, refx, refy):
        # verifico se o programador escolheu o x e/ou y do elemento, entao corrijo a atribuicao
        refx = refx if refx != element.x else f'{element.varname}.x'
        refy = refy if refy != element.y else f'{element.varname}.y'
        temp_event = f'{element.varname}:applyLinearImpulse({x}, {y}, {refx}, {refy})'
        setattr(element, 'temp_event', temp_event)
        return self

    def __str__(self):
        req = f'{self.varname} = require ("physics")\n'
        return f'{req}{self.varname}.start()\n' + '\n'.join([f'{self.varname}.addBody({i})' for i in self.elements])
