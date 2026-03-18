from persona import Persona
from nodobst import NodoBST


class BST:
    def __init__(self):
        self._raiz = None

    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        self._raiz = raiz

    def insertar(self, nombre_completo: str, cedula: str, nacionalidad: str, edad: int):
        persona = Persona(nombre_completo, cedula, nacionalidad, edad)
        self.raiz = self._insertar(self.raiz, persona)

    def _insertar(self, nodo, persona):
        if nodo is None:
            return NodoBST(persona)
        cmp = self._comparar_cedulas(persona.cedula, nodo.persona.cedula)
        if cmp < 0:
            nodo.izquierda = self._insertar(nodo.izquierda, persona)
        elif cmp > 0:
            nodo.derecha = self._insertar(nodo.derecha, persona)
        else:
            print("Ya existe una persona con esa cédula.\n")
        return nodo

    def buscar(self, cedula: str):
        return self._buscar(self.raiz, cedula)

    def _comparar_cedulas(self, a: str, b: str) -> int:
        """Retorna -1 si a<b, 0 si a==b, 1 si a>b. Usa comparación numérica cuando aplica."""
        try:
            na, nb = int(a), int(b)
            return -1 if na < nb else (1 if na > nb else 0)
        except (ValueError, TypeError):
            return -1 if a < b else (1 if a > b else 0)

    def _buscar(self, nodo, cedula):
        if nodo is None:
            return None
        cmp = self._comparar_cedulas(cedula, nodo.persona.cedula)
        if cmp == 0:
            return nodo.persona
        elif cmp < 0:
            return self._buscar(nodo.izquierda, cedula)
        else:
            return self._buscar(nodo.derecha, cedula)

    def recorrido_inorden(self):
        """Recorre el árbol en orden ascendente (izquierda -> raíz -> derecha)."""
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(nodo.persona.cedula)
            self._inorden(nodo.derecha)

    def recorrido_preorden(self):
        """Recorre el árbol en preorden (raíz -> izquierda -> derecha)."""
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is not None:
            print(nodo.persona.cedula)
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

    def recorrido_postorden(self):
        """Recorre el árbol en postorden (izquierda -> derecha -> raíz)."""
        self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo is not None:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.persona.cedula)
