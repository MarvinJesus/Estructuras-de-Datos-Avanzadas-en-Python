#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Clase 1
import string
def main():
    nombre_archivo = "clase-1/parrafo.txt"
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return
    texto_limpio = texto.lower()
    palabras = texto_limpio.split()
    frecuencias = {}
    for palabra in palabras:
        palabra_limpia = palabra.strip(string.punctuation)
        if palabra_limpia:
            frecuencias[palabra_limpia] = frecuencias.get(palabra_limpia, 0) + 1
    print(f"\n--- Reporte de frecuencia de palabras en '{nombre_archivo}' ---\n")
    for palabra, cantidad in frecuencias.items():
        print(f"  '{palabra}': {cantidad} vez" if cantidad == 1 else f"  '{palabra}': {cantidad} veces")
    print("\n" + "-" * 45)
if __name__ == "__main__":
    main()
