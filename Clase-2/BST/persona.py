class Persona:
    def __init__(self, nombre_completo: str, cedula: str, nacionalidad: str, edad: int):
        self._nombre_completo = nombre_completo
        self._cedula = cedula
        self._nacionalidad = nacionalidad
        self._edad = edad

    @property
    def nombre_completo(self):
        return self._nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, nombre_completo):
        self._nombre_completo = nombre_completo

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        self._nacionalidad = nacionalidad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def _cedula_numero(self, c):
        """Convierte cédula a número si es posible, para orden correcto (99 < 101)."""
        try:
            return int(c)
        except (ValueError, TypeError):
            return c

    def __lt__(self, other):
        a, b = self._cedula_numero(self._cedula), self._cedula_numero(other._cedula)
        if type(a) == type(b) == int:
            return a < b
        return self._cedula < other._cedula

    def __gt__(self, other):
        a, b = self._cedula_numero(self._cedula), self._cedula_numero(other._cedula)
        if type(a) == type(b) == int:
            return a > b
        return self._cedula > other._cedula

    def __eq__(self, other):
        return self._cedula == other._cedula
