class Cliente:
    """
    Representa un cliente de la Tienda.
    Cada cliente tiene una prioridad de atención (1 = basico, 2 = afiliado, 3 = premium)
    y un carrito de compras con su lista de productos.
    """

    def __init__(self, nombre_completo: str, cedula: str, prioridad: int):
        self._nombre_completo = nombre_completo
        self._cedula = cedula
        self._prioridad = prioridad  # 1 basico, 2 afiliado, 3 premium
        self._carrito: list[tuple[object, int]] = []  # (Producto, cantidad)

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
    def prioridad(self) -> int:
        return self._prioridad

    @prioridad.setter
    def prioridad(self, prioridad: int):
        self._prioridad = prioridad

    @property
    def carrito(self):
        return self._carrito

    def agregar_al_carrito(self, producto, cantidad: int):
        self._carrito.append((producto, cantidad))

    def total_a_pagar(self) -> float:
        total = 0.0
        for producto, cantidad in self._carrito:
            total += producto.precio * cantidad
        return total

    # Nota: no se implementan métodos de comparación (__lt__, __gt__, __eq__)
    # porque el programa actual no los necesita para la cola ni para el árbol.
