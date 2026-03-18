#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 2 - Clase 2
"""
    Analizador aritmético: solo números, sin variables.
    Valida delimitadores ( ) [ ] { } con Pila y que cada operador tenga número a izq/der.
"""

from pila import Pila

class AnalizadorAritmeticoNumerico:
    """
        Valida expresiones aritméticas solo con números; usa Pila para delimitadores.
    """

    def __init__(self):
        # Propiedades privadas: tipos de token y delimitadores
        self._N, self._O, self._A, self._C = "N", "O", "A", "C"
        self._PARES = {")": "(", "]": "[", "}": "{"}
        self._APERTURAS = frozenset(self._PARES.values())
        self._CIERRES = frozenset(self._PARES.keys())
        self._OP_DOBLES = frozenset(("==", ">=", "<=", "!="))
        self._OP_UNO = frozenset("+-*/<>=")

    def _es_numero(self, s: str) -> bool:
        if not s or s in (".", "-", "-."):
            return False
        try:
            float(s)
            return True
        except ValueError:
            return False

    def _leer_numero(self, expr: str, pos: int) -> tuple:
        """
            Devuelve (texto_numero, pos_siguiente) o (None, pos).
        """
        i = pos
        while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
            i += 1
        texto = expr[pos:i]
        return (texto, i) if self._es_numero(texto) else (None, pos)

    def _tokenizar(self, expr: str):
        """
            Tokeniza y valida delimitadores con la Pila. Lista de (tipo, valor) o None.
        """
        self._pila = Pila()
        tokens = []
        pos, n = 0, len(expr)

        while pos < n:
            while pos < n and expr[pos].isspace():
                pos += 1
            if pos >= n:
                break
            c = expr[pos]

            if c in self._APERTURAS:
                self._pila.push(c)
                tokens.append((self._A, c))
                pos += 1
            elif c in self._CIERRES:
                try:
                    if self._pila.pop() != self._PARES[c]:
                        return None
                except IndexError:
                    return None
                tokens.append((self._C, c))
                pos += 1
            elif c in self._OP_UNO or c == "!":
                # Signo negativo como número
                espera_op = not tokens or tokens[-1][0] in (self._O, self._A)
                if c == "-" and espera_op:
                    pos += 1
                    txt, pos = self._leer_numero(expr, pos)
                    if txt is None:
                        return None
                    tokens.append((self._N, "-" + txt))
                elif pos + 1 < n and expr[pos : pos + 2] in self._OP_DOBLES:
                    tokens.append((self._O, expr[pos : pos + 2]))
                    pos += 2
                elif c in self._OP_UNO:
                    tokens.append((self._O, c))
                    pos += 1
                else:
                    return None
            elif c.isdigit() or c == ".":
                txt, pos = self._leer_numero(expr, pos)
                if txt is None:
                    return None
                tokens.append((self._N, txt))
            elif c.isalpha():
                return None
            else:
                pos += 1

        return None if len(self._pila) else tokens

    def _estructura_ok(self, tokens: list) -> bool:
        """
            La regla que usa es: operando (operador operando)*; operando = N o ( subexpresión ).
            tipos de tokens: _A: apertura, _C: cierre, _N: número, _O: operador
        """
        if not tokens:
            return False
        pila = []
        need_op = True
        for tipo, _ in tokens:
            if tipo == self._A:
                pila.append(1)
            elif tipo == self._C:
                if not pila:
                    return False
                pila.pop()
            elif need_op:
                if tipo != self._N:
                    return False
                need_op = False
            else:
                if tipo != self._O:
                    return False
                need_op = True
        return len(pila) == 0 and not need_op

    def validar(self, expresion: str) -> bool:
        """
            True si delimitadores balanceados, solo números y cada operador con número izq/der.
        """
        if not expresion or not expresion.strip():
            return False
        tokens = self._tokenizar(expresion.strip()) ##tokeniza
        return tokens is not None and self._estructura_ok(tokens) ##valida estructura
