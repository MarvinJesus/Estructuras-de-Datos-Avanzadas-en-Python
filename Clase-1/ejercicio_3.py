#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Clase 1
def main():
    intereses_usuario_a = {"programacion", "musica", "deportes", "lectura", "cine", "viajes"}
    intereses_usuario_b = {"musica", "deportes", "cocina", "fotografia", "lectura", "arte"}
    print(f"\nIntereses del Usuario A: {intereses_usuario_a}")
    print(f"Intereses del Usuario B: {intereses_usuario_b}")
    print(f"Intereses que comparten ambos usuarios: {intereses_usuario_a   &   intereses_usuario_b}")
    print(f"Intereses que tiene A pero B no: {intereses_usuario_a   -   intereses_usuario_b}")
    print(f"Lista total de intereses unicos: {intereses_usuario_a   |   intereses_usuario_b}")
if __name__ == "__main__":
    main()
