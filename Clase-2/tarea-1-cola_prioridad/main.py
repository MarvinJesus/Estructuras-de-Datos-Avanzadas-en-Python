#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Clase 2 - Tarea 1: uso de cola de prioridad

from cola_prioridad import Cola


def mostrar_menu() -> None:
    print("""
Cola de prioridad
==================
1) Encolar elemento
2) Desencolar elemento
3) Ver frente de la cola
4) Ver tamaño de la cola
5) Ver toda la cola (Testeo)
6) Salir
""")


def main() -> None:
    cola = Cola()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            try:
                prioridad_str = input("Prioridad (entero, mayor = más prioridad): ").strip()
                prioridad = int(prioridad_str)
            except ValueError:
                print("Prioridad inválida, debe ser un entero.\n")
                continue

            valor = input("Valor del elemento: ")
            cola.enqueue((prioridad, valor)) #tupla de prioridad y valor
            print("Elemento encolado.\n")

        elif opcion == "2":
            try:
                prioridad, valor = cola.dequeue()
                print(f"Desencolado -> prioridad: {prioridad}, valor: {valor}\n")
            except IndexError as e:
                print(str(e))

        elif opcion == "3":
            try:
                prioridad, valor = cola.front()
                print(f"Frente -> prioridad: {prioridad}, valor: {valor}\n")
            except IndexError as e:
                print(str(e))

        elif opcion == "4":
            print(f"Tamaño de la cola: {cola.size()}\n")

        elif opcion == "5":
            if cola.size() == 0:
                print("La cola está vacía.\n")
            else:
                print("Contenido de la cola (frente -> final):")
                for prioridad, valor in cola._elementos:
                    print(f"  prioridad: {prioridad}, valor: {valor}")
                print()

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.\n")


if __name__ == "__main__":
    main()

