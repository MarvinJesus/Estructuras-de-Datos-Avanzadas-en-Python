from persona import Persona


class NodoBST:
    def __init__(self, persona: Persona):
        self._persona = persona
        self._izquierda = None
        self._derecha = None

    @property
    def persona(self):
        return self._persona

    @persona.setter
    def persona(self, persona):
        self._persona = persona

    @property
    def izquierda(self):
        return self._izquierda

    @izquierda.setter
    def izquierda(self, izquierda):
        self._izquierda = izquierda

    @property
    def derecha(self):
        return self._derecha

    @derecha.setter
    def derecha(self, derecha):
        self._derecha = derecha
