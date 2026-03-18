from producto import Producto


class NodoBST:
    def __init__(self, producto: Producto, cantidad: int = 0):
        self._producto = producto
        self._cantidad = cantidad
        self._izquierda = None
        self._derecha = None

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def producto(self, producto):
        self._producto = producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad: int):
        self._cantidad = cantidad

    def incrementar_stock(self, cantidad: int):
        self._cantidad += cantidad

    def decrementar_stock(self, cantidad: int) -> bool:
        if cantidad <= self._cantidad:
            self._cantidad -= cantidad
            return True
        return False

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
