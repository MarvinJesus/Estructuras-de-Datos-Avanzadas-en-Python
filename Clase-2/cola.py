#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Clase 2
from collections import deque
class Cola:
    def __init__(self):
        self._elementos = deque()

    def enqueue(self, elemento):
        self._elementos.append(elemento)

    def dequeue(self):
        if self.__esta_vacia():
            raise IndexError("La cola está vacía.\n")
        return self._elementos.popleft()

    def front(self):
        if self.__esta_vacia():
            raise IndexError("La cola está vacía.\n")
        return self._elementos[0]

    def __esta_vacia(self):
        return len(self._elementos) == 0

    def size(self):
        return len(self._elementos)
