from producto import Producto
from nodobst import NodoBST


class ArbolProductos:
    def __init__(self):
        self._raiz = None

    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        self._raiz = raiz

    def insertar(self, nombre: str, descripcion: str, precio: float, cantidad: int):
        """Inserta un producto en el arbol usando el nombre como llave.
        Si el producto ya existe, aumenta su cantidad en inventario.
        """
        # Normalizamos el nombre a minusculas para que el arbol no duplique por mayusculas/minusculas
        nombre_normalizado = nombre.lower()
        producto = Producto(nombre_normalizado, descripcion, precio)
        self.raiz = self._insertar(self.raiz, producto, cantidad)

    def _insertar(self, nodo, producto: Producto, cantidad: int):
        if nodo is None:
            return NodoBST(producto, cantidad)
        cmp = self._comparar_nombres(producto.nombre, nodo.producto.nombre)
        if cmp < 0:
            nodo.izquierda = self._insertar(nodo.izquierda, producto, cantidad)
        elif cmp > 0:
            nodo.derecha = self._insertar(nodo.derecha, producto, cantidad)
        else:
            # Si ya existe, actualizamos la información del producto
            nodo.producto.descripcion = producto.descripcion
            nodo.producto.precio = producto.precio
            # y aumentamos la cantidad en inventario
            nodo.incrementar_stock(cantidad)
        return nodo

    def buscar(self, nombre: str):
        """Busca un nodo de producto por nombre."""
        nombre_normalizado = nombre.lower()
        return self._buscar(self.raiz, nombre_normalizado)

    def _comparar_nombres(self, a: str, b: str) -> int:
        """Retorna -1 si a<b, 0 si a==b, 1 si a>b."""
        return -1 if a < b else (1 if a > b else 0)

    def _buscar(self, nodo, nombre: str):
        if nodo is None:
            return None
        cmp = self._comparar_nombres(nombre, nodo.producto.nombre)
        if cmp == 0:
            return nodo
        elif cmp < 0:
            return self._buscar(nodo.izquierda, nombre)
        else:
            return self._buscar(nodo.derecha, nombre)

    def obtener_producto_para_venta(self, nombre: str, cantidad: int):
        """
        Intenta reservar 'cantidad' unidades del producto.
        Si hay stock suficiente, descuenta del nodo y devuelve el Producto.
        Si no hay suficiente, devuelve None.
        """
        nodo = self.buscar(nombre)
        if nodo is None:
            return None
        if nodo.decrementar_stock(cantidad):
            return nodo.producto
        return None

    def recorrido_inorden(self):
        """Recorre el arbol en orden ascendente (izquierda -> raiz -> derecha)."""
        self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(f"{nodo.producto} | Stock: {nodo.cantidad}")
            self._inorden(nodo.derecha)

    def recorrido_preorden(self):
        """Recorre el arbol en preorden (raiz -> izquierda -> derecha)."""
        self._preorden(self.raiz)

    def _preorden(self, nodo):
        if nodo is not None:
            print(nodo.producto)
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

    def recorrido_postorden(self):
        """Recorre el arbol en postorden (izquierda -> derecha -> raiz)."""
        self._postorden(self.raiz)

    def _postorden(self, nodo):
        if nodo is not None:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.producto)
