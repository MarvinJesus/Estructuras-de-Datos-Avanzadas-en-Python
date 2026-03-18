#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 3 - Clase 3
from datetime import datetime
class Ticket:
    """
    Representa un ticket del sistema.
    """
    cantidad = 0  # contador estatico para generar ids únicos
    def __init__(self, nombre_completo: str, descripcion: str, prioridad: int) -> None:
        Ticket.cantidad += 1
        self.id = Ticket.cantidad
        self.nombre_completo = nombre_completo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_creacion = datetime.now()
        self.fecha_resolucion: datetime | None = None
    def resolver(self) -> None:
        self.fecha_resolucion = datetime.now()
    def __str__(self) -> str:
        fecha_creacion_str = self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")
        fecha_resolucion_str = (
            self.fecha_resolucion.strftime("%Y-%m-%d %H:%M:%S")
            if self.fecha_resolucion
            else "PENDIENTE"
        )
        prioridad_texto = {
            1: "Adulto mayor",
            2: "Mujer embarazada",
            3: "Discapacitado",
            4: "Persona normal",
        }.get(self.prioridad, f"Prioridad {self.prioridad}")
        return (
            f"Ticket ID: {self.id}\n"
            f"Nombre completo: {self.nombre_completo}\n"
            f"Descripción: {self.descripcion}\n"
            f"Prioridad: {self.prioridad} ({prioridad_texto})\n"
            f"Fecha creación: {fecha_creacion_str}\n"
            f"Fecha resolución: {fecha_resolucion_str}"
        )
