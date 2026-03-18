from cola_prioridad import ColaClientes
from cliente import Cliente
from bst import ArbolProductos


class Tienda:
    """
    Representa la Tienda.
    Gestiona el inventario de productos (ArbolProductos) y la cola de clientes (ColaClientes).
    """

    def __init__(self) -> None:
        self._inventario = ArbolProductos()
        self._cola_clientes = ColaClientes()

    # -------------------- INVENTARIO / ARBOL DE PRODUCTOS -------------------- #
    @property
    def inventario(self) -> ArbolProductos:
        return self._inventario

    def agregar_producto(self, nombre: str, descripcion: str, precio: float, cantidad: int):
        self._inventario.insertar(nombre, descripcion, precio, cantidad)

    def buscar_producto(self, nombre: str):
        return self._inventario.buscar(nombre)

    def reservar_producto(self, nombre: str, cantidad: int):
        """
        Intenta reservar 'cantidad' unidades de un producto del inventario.
        Si hay stock suficiente, descuenta del inventario y devuelve el Producto.
        Si no hay suficiente stock o no existe, devuelve None.
        """
        return self._inventario.obtener_producto_para_venta(nombre, cantidad)

    def mostrar_inventario(self):
        self._inventario.recorrido_inorden()

    # -------------------- COLA DE CLIENTES -------------------- #
    def registrar_cliente(self, nombre_completo: str, cedula: str, prioridad: int) -> Cliente:
        """
        Crea un Cliente y lo encola en la ColaClientes segun su prioridad.
        La prioridad es: 1 = basico, 2 = afiliado, 3 = premium.
        """
        cliente = Cliente(nombre_completo, cedula, prioridad)
        # En la cola, un numero de prioridad MAYOR significa mas prioridad
        prioridad_interna = prioridad  # aqui 3 > 2 > 1 ya cumple el requisito
        self._cola_clientes.enqueue((prioridad_interna, cliente))
        return cliente

    def obtener_cliente_frente(self):
        """
        Devuelve el cliente al frente de la cola sin sacarlo.
        Si la cola esta vacia, devuelve None.
        """
        try:
            _, cliente = self._cola_clientes.front()
        except IndexError:
            return None
        return cliente

    def atender_siguiente_cliente(self):
        """
        Saca de la cola al cliente con mayor prioridad (y mas cercano al frente)
        y lo devuelve para procesar su factura.
        Si la cola esta vacia, devuelve None.
        """
        try:
            _, cliente = self._cola_clientes.dequeue()
        except IndexError:
            return None
        return cliente
