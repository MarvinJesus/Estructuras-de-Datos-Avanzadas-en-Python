from gestor_tienda import Tienda
from producto import Producto


def menu() -> None:
    tienda = Tienda()

    while True:
        print("\n=== SISTEMA DE VENTAS EN LINEA ===")
        print("1. Insertar producto al inventario")
        print("2. Insertar cliente en la cola y llenar su carrito")
        print("3. Atender siguiente cliente (generar factura)")
        print("4. Mostrar inventario de productos")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print("\n--- Insercion de producto ---")
            nombre = input("Nombre del producto: ").strip()
            descripcion = input("Descripcion: ").strip()
            try:
                precio_str = input("Precio: ").strip()
                precio = float(precio_str)
                cantidad_str = input("Cantidad en inventario: ").strip()
                cantidad = int(cantidad_str)
                if cantidad <= 0:
                    raise ValueError
            except ValueError:
                print("Precio debe ser numero y cantidad entero positivo.\n")
                continue
            tienda.agregar_producto(nombre, descripcion, precio, cantidad)
            print("Producto agregado/actualizado en el inventario.\n")

        elif opcion == "2":
            print("\n--- Registro de cliente y llenado de carrito ---")
            nombre_cliente = input("Nombre completo del cliente: ").strip()
            cedula = input("Cédula del cliente: ").strip()

            while True:
                print("\nSeleccione el tipo de cliente (prioridad):")
                print("1. Básico")
                print("2. Afiliado")
                print("3. Premium")
                prioridad_str = input("Ingrese una opcion (1-3): ").strip()
                if prioridad_str in {"1", "2", "3"}:
                    prioridad = int(prioridad_str)
                    break
                else:
                    print("Opcion de prioridad no válida. Intente de nuevo.")

            cliente = tienda.registrar_cliente(nombre_cliente, cedula, prioridad)
            print("\nAhora llene el carrito del cliente seleccionando productos del inventario.")

            while True:
                print("\n--- Inventario disponible ---")
                tienda.mostrar_inventario()
                nombre_prod = input(
                    "\nIngrese el nombre del producto a añadir al carrito (o ENTER para terminar): "
                ).strip()
                if not nombre_prod:
                    break
                try:
                    cantidad_str = input("Cantidad: ").strip()
                    cantidad = int(cantidad_str)
                    if cantidad <= 0:
                        raise ValueError
                except ValueError:
                    print("La cantidad debe ser un entero positivo.\n")
                    continue

                producto_reservado = tienda.reservar_producto(nombre_prod, cantidad)
                if producto_reservado is None:
                    print("No hay suficiente stock o el producto no existe.\n")
                    continue

                cliente.agregar_al_carrito(producto_reservado, cantidad)
                print("Producto añadido al carrito y stock actualizado.\n")

        elif opcion == "3":
            print("\n--- Atencion del siguiente cliente ---")
            cliente = tienda.atender_siguiente_cliente()
            if cliente is None:
                print("No hay clientes en la cola.\n")
            else:
                print(f"\nCliente atendido: {cliente.nombre_completo} (cédula: {cliente.cedula})")
                print("Carrito de compras:")
                if not cliente.carrito:
                    print("El carrito está vacio.")
                else:
                    total = 0.0
                    for producto, cantidad in cliente.carrito:
                        subtotal = producto.precio * cantidad
                        total += subtotal
                        print(
                            f"- {producto.nombre} x {cantidad} "
                            f"@ ${producto.precio:.2f} = ${subtotal:.2f}"
                        )
                    print(f"\nTOTAL A PAGAR: ${total:.2f}\n")

        elif opcion == "4":
            print("\n--- Inventario de productos ---")
            tienda.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema de ventas...")
            break

        else:
            print("Opcion no válida.\n")


def main() -> None:
    menu()


if __name__ == "__main__":
    main()
