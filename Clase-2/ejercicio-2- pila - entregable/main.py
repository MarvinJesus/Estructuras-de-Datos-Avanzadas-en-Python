#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ejercicio 2 - Clase 2

"""
    Punto de entrada para probar el AnalizadorAritmeticoNumerico del Ejercicio 2.
    Permite ingresar expresiones por consola y muestra si son válidas o no, tambien se pueden hacer pruebas.
"""

from analizador_aritmetico_numerico import AnalizadorAritmeticoNumerico

def main() -> None:
    print("""
        _                _ _              _
       / \   _ __   __ _| (_)______ _  __| | ___  _ __
      / _ \ | '_ \ / _` | | |_  / _` |/ _` |/ _ \| '__|
     / ___ \| | | | (_| | | |/ / (_| | (_| | (_) | |
    /_/  \__\_| |_|\__,_|_|_/___\__,_|\__,_|\___/|_|       _   _                           _
         / \   _ __(_) |_ _ __ ___   ___| |_(_) ___ ___   | \ | |_   _ _ __ ___   ___ _ __(_) ___ ___
        / _ \ | '__| | __| '_ ` _ \ / _ \ __| |/ __/ _ \  |  \| | | | | '_ ` _ \ / _ \ '__| |/ __/ _ \
       / ___ \| |  | | |_| | | | | |  __/ |_| | (_| (_) | | |\  | |_| | | | | | |  __/ |  | | (_| (_) |
      /_/   \_\_|  |_|\__|_| |_| |_|\___|\__|_|\___\___/  |_| \_|\__,_|_| |_| |_|\___|_|  |_|\___\___/
    """)
    analizador = AnalizadorAritmeticoNumerico()
    print("Analizador Aritmético Numérico (solo números, sin variables)")
    print("Escribe una expresión o Enter vacío para salir o Escribe test para pruebas.\n")

    while True:
        expresion = input("Expresión> ").strip()
        if not expresion:
            print("Saliendo...")
            break
        elif expresion == "test":
            print("Pruebas...")
            pruebas = [
                "2 + 3", "10.5 * 4", "{[(2 + 3) * 4] + 1}", "((1 + 2) * 3) - 4", "-5 + 3",
                "1 < 2", "3 >= 2", "2 + 3 * 4", "", "a + 2", "2 + b", "2 + ", "+ 3",
                "2 ++ 3", "(2 + 3", "2 + 3)", "(2 + + 9)", "(-2 -+ - 9)","(-2 -- -9)","(-4 - -5)","{[(2 + 3) * 4] + 1","{(8 + 1) * 2] + 3}",
            ]
            print("Analizador Aritmético Numérico - Solo números\n")
            for expr in pruebas:
                ok = analizador.validar(expr)
                print(f"  '{expr}'  ->  {'VÁLIDA' if ok else 'NO VÁLIDA'}")
        else:
            es_valida = analizador.validar(expresion)
            estado = "VÁLIDA" if es_valida else "NO VÁLIDA"
            print(f"  '{expresion}' -> {estado}")

if __name__ == "__main__":
    main()
