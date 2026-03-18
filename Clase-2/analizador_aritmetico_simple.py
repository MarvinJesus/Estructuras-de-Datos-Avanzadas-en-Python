#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analizador aritmético simplificado: solo valida delimitadores balanceados ( ) [ ] { }."""

from pila import Pila


class AnalizadorAritmeticoSimple:
    """Valida que paréntesis, corchetes y llaves estén balanceados usando una pila."""

    PARES = {')': '(', ']': '[', '}': '{'}

    def __init__(self):
        self._pila = Pila()

    def validar(self, expresion: str) -> bool:
        """Devuelve True si los delimitadores ( ) [ ] { } están balanceados."""
        self._pila = Pila()
        aperturas = set(self.PARES.values())

        for c in expresion:
            if c in aperturas:
                self._pila.push(c)
            elif c in self.PARES:
                try:
                    if self._pila.pop() != self.PARES[c]:
                        return False
                except IndexError:
                    return False  # cierre sin apertura

        return len(self._pila) == 0


if __name__ == "__main__":
    analizador = AnalizadorAritmeticoSimple()
    pruebas = [
        "(2 + 3)",
        "[(a + b) * c]",
        "{(1 + 2) * [3 - 4]}",
        "((()))",
        "(2 + 3",      # falta cierre
        "2 + 3)",      # cierre sin apertura
        "([)]",        # orden incorrecto
    ]
    print("Analizador simplificado - Delimitadores balanceados\n")
    for expr in pruebas:
        ok = analizador.validar(expr)
        print(f"  '{expr}'  ->  {'VÁLIDA' if ok else 'NO VÁLIDA'}")
