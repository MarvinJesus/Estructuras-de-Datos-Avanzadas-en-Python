#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Clase 2
from pila import Pila
class AnalizadorAritmetico:
    """
    Valida expresiones aritméticas comprobando que los delimitadores
    (paréntesis, corchetes, llaves) estén balanceados usando una pila.
    """

    def __init__(self):
        self._pila = Pila()
        # Diccionario: delimitador de cierre -> delimitador de apertura
        self._cierre_a_apertura = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        # Diccionario: delimitadores de apertura (para saber si un carácter es apertura)
        self._aperturas = set(self._cierre_a_apertura.values())
        # Diccionario: delimitadores de cierre
        self._cierres = set(self._cierre_a_apertura.keys())
        # Operadores aritméticos y de comparación (sintaxis matemática simple)
        self._operadores = set("+-*/<=>")

    def _es_operador(self, caracter: str) -> bool:
        return caracter in self._operadores

    def _sintaxis_operadores_valida(self, expresion: str) -> bool:
        """
        Valida que la expresión no tenga errores simples de sintaxis con operadores:
        - No puede empezar con un operador (salvo '-' para números negativos).
        - No puede terminar con un operador.
        - No puede haber dos operadores seguidos (con o sin espacios): 2++2, num+-2, *9+1.
        """
        if not expresion or not expresion.strip():
            return True  # Sin contenido, no hay operadores que validar
        t = expresion.strip()
        # No puede terminar con operador
        if self._es_operador(t[-1]):
            return False
        # Primer carácter no espacio: no puede ser operador (salvo '-' como signo negativo)
        i = 0
        while i < len(t) and t[i].isspace():
            i += 1
        if i < len(t) and self._es_operador(t[i]) and t[i] != "-":
            return False
        # No dos operadores consecutivos (con espacios entre medio)
        j = 0
        while j < len(t):
            if self._es_operador(t[j]):
                k = j + 1
                while k < len(t) and t[k].isspace():
                    k += 1
                if k < len(t) and self._es_operador(t[k]):
                    return False  # operador seguido de operador
                j = k
            else:
                j += 1
        return True

    def _es_apertura(self, caracter: str) -> bool:
        return caracter in self._aperturas

    def _es_cierre(self, caracter: str) -> bool:
        return caracter in self._cierres

    def _obtener_apertura_esperada(self, cierre: str) -> str:
        return self._cierre_a_apertura.get(cierre)

    def validar(self, expresion: str) -> bool:
        """
        Valida la expresión. Conforme se recorre cada carácter:
        - Si es apertura ( [ { se hace push en la pila.
        - Si es cierre ) ] } se hace pop y se comprueba que coincida.
        Al final, si la pila está vacía (y no hubo errores) y la sintaxis
        básica de operadores es correcta, la expresión es válida.
        REGLA IMPORTANTE: si la expresión NO es válida, la pila NO debe
        quedar vacía.
        """
        # Limpiar la pila por si se reutiliza el analizador
        self._pila = Pila()
        primera_apertura = None

        for caracter in expresion:
            if self._es_apertura(caracter):
                if primera_apertura is None:
                    primera_apertura = caracter
                self._pila.push(caracter)
            elif self._es_cierre(caracter):
                try:
                    tope = self._pila.pop()
                    esperado = self._obtener_apertura_esperada(caracter)
                    if tope != esperado:
                        # No coincide el par: aseguramos que la pila tenga al menos
                        # la primera apertura (o una llave por defecto) antes de fallar.
                        if len(self._pila) == 0:
                            if primera_apertura is not None:
                                self._pila.push(primera_apertura)
                            else:
                                self._pila.push('{')
                        return False
                except IndexError:
                    # Cierre sin apertura: si la pila quedó vacía, guardamos la primera
                    # apertura o una llave por defecto para indicar error.
                    if len(self._pila) == 0:
                        if primera_apertura is not None:
                            self._pila.push(primera_apertura)
                        else:
                            self._pila.push('{')
                    return False

        # Expresión válida: delimitadores balanceados Y sintaxis de operadores correcta
        if len(self._pila) != 0:
            return False
        if not self._sintaxis_operadores_valida(expresion):
            # Operadores mal usados: si la pila está vacía, dejamos al menos
            # la primera apertura o una llave por defecto para marcar el error.
            if len(self._pila) == 0:
                if primera_apertura is not None:
                    self._pila.push(primera_apertura)
                else:
                    self._pila.push('{')
            return False  # Operadores mal usados (ej. 2++2, *9+1, num+-2)
        return True

    def esta_vacia(self) -> bool:
        """Indica si la pila está vacía."""
        return len(self._pila) == 0

# Ejemplo de uso
if __name__ == "__main__":
    analizador = AnalizadorAritmetico()

    pruebas = [
        "{ (2 + 3) + (4 * 4) }",
        "(2 + 3) * 4",
        "[(a + b) * c]",
        "{(1 + 2) * [3 - 4]}",
        "((()))",
        "-5 + 3",           # Menos unario al inicio OK
        "sin delimitadores",
        "(2 + 3",           # Falta cierre
        "2 + 3)",           # Cierre sin apertura
        "([)]",             # Orden incorrecto
        "2+2",             # Dos operadores seguidos
        "num+-2",           # Operador seguido de operador
        "*9+1",             # Empieza con operador
        "2+3*",             # Termina con operador
    ]

    print("Analizador Aritmético - Validación de expresiones\n")
    for expr in pruebas:
        resultado = analizador.validar(expr)
        estado = "VÁLIDA" if resultado else "NO VÁLIDA"
        print(f"  '{expr}'  ->  {estado} ; pila vacía? {analizador.esta_vacia()}")
