#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Clase 2
class Pila:
    def __init__(self):
        self._elementos = []

    def push(self, elemento):
        self._elementos.append(elemento)

    def pop(self):
        if self.__esta_vacia():
            raise IndexError("La pila está vacía.\n")
        return self._elementos.pop()

    def peek(self):
        if self.__esta_vacia():
            raise IndexError("La pila está vacía.\n")
        return self._elementos[-1]

    def __esta_vacia(self):
        return len(self._elementos) == 0
        
    def __len__(self):
        return len(self._elementos)

    def __str__(self):
        return str(self._elementos)