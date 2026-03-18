#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 3 - Clase 3
class Producto:
    """
    Representa un producto del inventario de la Tienda.
    El nombre se utiliza como llave en el árbol binario de búsqueda.
    """

    cantidad = 0  # contador estático para generar ids únicos

    def __init__(self, nombre: str, descripcion: str, precio: float) -> None:
        Producto.cantidad += 1
        self.id = Producto.cantidad
        # Normalizamos el nombre a minúsculas para evitar duplicados por mayúsculas/minúsculas
        self.nombre = nombre.lower()
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.descripcion} - ${self.precio:.2f}"
