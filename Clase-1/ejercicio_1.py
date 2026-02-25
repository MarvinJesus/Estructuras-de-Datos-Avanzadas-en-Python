#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Clase 1
def main():
    transacciones=[-1,2,-3,4,5,-6,-7,8,-9,10,-11,12]
    print(f"\nLista de transacciones: {transacciones}")
    salidas = [t for t in transacciones if t < 0]
    print(f"\nLista de transacciones de salida: {salidas}")
    entradas = [t for t in transacciones if t > 0]
    print(f"\nLista de transacciones de entrada: {entradas}")
    salidas.sort()
    entradas.sort()
    salidas_mayores = salidas[-3:] if len(salidas) >= 3 else salidas
    print(f"\nLista de transacciones de mayores salidas: {salidas_mayores}")
    entradas_mayores = entradas[-3:] if len(entradas) >= 3 else entradas
    print(f"\nLista de transacciones de mayores entradas: {entradas_mayores}")
    transacciones_seleccionadas = salidas_mayores + entradas_mayores
    transacciones_seleccionadas.sort()
    indice_central = len(transacciones_seleccionadas) // 2
    transacciones_seleccionadas.insert(indice_central, 0)
    print(f"\nLista final con cero en medio: {transacciones_seleccionadas}\n")
if __name__ == "__main__":
    main()

