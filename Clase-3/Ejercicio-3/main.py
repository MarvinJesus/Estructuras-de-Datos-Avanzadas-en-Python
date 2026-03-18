#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 3 - Clase 3
from gestor_tickets import SistemaTickets
# -------------------- CAPA DE UI / MENuS -------------------- #
def menu_usuario(gestor: SistemaTickets) -> None:
    while True:
        print("\n--- MENu USUARIO ---")
        print("1. Crear ticket")
        print("2. Buscar ticket resuelto por ID")
        print("3. Volver al menu principal")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            print("\nCreacion de ticket")
            nombre = input("Nombre completo: ").strip()
            descripcion = input("Descripcion del problema: ").strip()
            # Seleccion de prioridad por tipo de persona
            while True:
                print("\nSeleccione la prioridad segun el tipo de persona:")
                print("1. Adulto mayor")
                print("2. Mujer embarazada")
                print("3. Discapacitado")
                print("4. Normal")
                prioridad_str = input("Ingrese una opcion (1-4): ").strip()
                if prioridad_str in {"1", "2", "3", "4"}:
                    prioridad = int(prioridad_str)
                    break
                else:
                    print("Opcion de prioridad no valida. Intente de nuevo.")
            ticket = gestor.crear_ticket(nombre, descripcion, prioridad)
            print(f"\nTicket creado con éxito. ID asignado: {ticket.id}")
        elif opcion == "2":
            print("\nBusqueda de ticket resuelto")
            try:
                ticket_id_str = input("Ingrese el ID del ticket: ").strip()
                ticket_id = int(ticket_id_str)
            except ValueError:
                print("El ID debe ser un numero entero.\n")
                continue
            ticket = gestor.buscar_ticket_resuelto(ticket_id)
            if ticket is not None:
                print("\nTicket encontrado (RESUELTO):")
                print(ticket)
            else:
                print(
                    "\nEl ticket con ese ID no se encuentra en la lista de resueltos."
                )
                print("El ticket esta PENDIENTE de resolucion (o no existe).\n")
        elif opcion == "3":
            break
        else:
            print("Opcion no valida.\n")
def menu_administrador(gestor: SistemaTickets) -> None:
    while True:
        print("\n--- MENu ADMINISTRADOR ---")
        print("1. Ver ticket al frente de la cola")
        print("2. Resolver ticket al frente de la cola")
        print("3. Volver al menu principal")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            resultado = gestor.obtener_ticket_frente()
            if resultado is None:
                print("La cola esta vacia.\n")
            else:
                prioridad, ticket = resultado
                print("\nTicket al frente de la cola de prioridad:")
                print(f"(Prioridad: {prioridad})")
                print(ticket)
        elif opcion == "2":
            resultado = gestor.resolver_ticket_frente()
            if resultado is None:
                print("La cola esta vacia.\n")
            else:
                prioridad, ticket = resultado
                print("\nTicket resuelto y movido a la lista de resueltos:")
                print(f"(Prioridad: {prioridad})")
                print(ticket)
        elif opcion == "3":
            break
        else:
            print("Opcion no valida.\n")
def main() -> None:
    gestor = SistemaTickets()
    while True:
        print("\n=== SISTEMA DE TICKETS ===")
        print("1. Menu de usuario")
        print("2. Menu de administrador")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            menu_usuario(gestor)
        elif opcion == "2":
            menu_administrador(gestor)
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.\n")
if __name__ == "__main__":
    main()
