#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 3 - Clase 3
from collections import deque


class ColaClientes:
    def __init__(self):
        self._elementos = deque()
    def enqueue(self, elemento):
        """
        Inserta en la cola segun prioridad.
        Se asume que 'elemento' es una tupla (prioridad, cliente)
        y que un numero de prioridad MAYOR significa mas prioridad.
        El cliente con mayor prioridad quedara al frente de la cola.
        """
        if not self._elementos:
            self._elementos.append(elemento)
            return
        nueva_prioridad = elemento[0]
        insertado = False
        for idx, existente in enumerate(self._elementos):
            prioridad_existente = existente[0]
            # Si la nueva prioridad es mayor, va antes
            if nueva_prioridad > prioridad_existente:
                self._elementos.insert(idx, elemento)
                insertado = True
                break
        if not insertado:
            # Si tiene la prioridad mas baja, va al final
            self._elementos.append(elemento)
    def dequeue(self):
        if self.__esta_vacia():
            raise IndexError("La cola esta vacia.\n")
        return self._elementos.popleft()
    def front(self):
        if self.__esta_vacia():
            raise IndexError("La cola esta vacia.\n")
        return self._elementos[0]
    def __esta_vacia(self):
        return len(self._elementos) == 0
    def size(self):
        return len(self._elementos)
