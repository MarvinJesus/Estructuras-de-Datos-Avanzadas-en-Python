#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 3 - Clase 3
from cola_prioridad import Cola
from ticket import Ticket
class SistemaTickets:
    """
    Gestor del sistema de tickets.
    Encapsula el acceso a la cola de prioridad y a los tickets.
    """
    def __init__(self) -> None:
        self.__tickets_pendientes = Cola()
        self.__tickets_resueltos: list[Ticket] = []
    # -------------------- OPERACIONES DEL GESTOR -------------------- #
    def crear_ticket(self, nombre: str, descripcion: str, prioridad: int) -> Ticket:
        """
        Crea un ticket y lo encola en la cola de prioridad.
        La prioridad recibida es:
            1 = adulto mayor
            2 = mujer embarazada
            3 = discapacitado
            4 = normal
        Internamente se transforma para que la cola
        mantenga mayor numero = mayor prioridad.
        Devuelve el ticket creado.
        """
        ticket = Ticket(nombre, descripcion, prioridad)
        prioridad_interna = 5 - prioridad  # 1->4, 2->3, 3->2, 4->1
        self.__tickets_pendientes.enqueue((prioridad_interna, ticket))
        return ticket
    def buscar_ticket_resuelto(self, ticket_id: int) -> Ticket | None:
        """
        Busca un ticket resuelto por ID en la lista interna.
        """
        for t in self.__tickets_resueltos:
            if t.id == ticket_id:
                return t
        return None
    def obtener_ticket_frente(self) -> tuple[int, Ticket] | None:
        """
        Devuelve el ticket al frente de la cola de prioridad sin sacarlo.
        Si la cola esta vacia, devuelve None.
        """
        try:
            _, ticket = self.__tickets_pendientes.front()
        except IndexError:
            return None
        # devolvemos la prioridad "logica" del ticket (1-4)
        return ticket.prioridad, ticket
    def resolver_ticket_frente(self) -> tuple[int, Ticket] | None:
        """
        Saca y resuelve el ticket al frente de la cola.
        Lo mueve a la lista de resueltos.
        Devuelve (prioridad, ticket) o None si la cola esta vacia.
        """
        try:
            _, ticket = self.__tickets_pendientes.dequeue()
        except IndexError:
            return None
        ticket.resolver()
        self.__tickets_resueltos.append(ticket)
        # devolvemos la prioridad "logica" del ticket (1-4)
        return ticket.prioridad, ticket
