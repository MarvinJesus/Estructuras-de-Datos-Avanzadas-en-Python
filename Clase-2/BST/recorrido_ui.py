"""
Interfaz gráfica para visualizar los recorridos de un BST paso a paso.
Muestra el árbol con nodos y aristas, resaltando el nodo actual y los ya recorridos.
"""
import tkinter as tk
from tkinter import ttk

from persona import Persona
from nodobst import NodoBST
from bst import BST


# Colores
COLOR_NODO_NORMAL = "#3498db"      # Azul - no visitado
COLOR_NODO_ACTUAL = "#f1c40f"      # Amarillo - nodo actual en el recorrido
COLOR_NODO_VISITADO = "#2ecc71"    # Verde - ya recorrido
COLOR_ARISTA_NORMAL = "#34495e"
COLOR_ARISTA_ACTIVA = "#e74c3c"    # Rojo - arista hacia el nodo actual
COLOR_TEXTO = "#2c3e50"
COLOR_FONDO = "#ecf0f1"


def obtener_secuencia_inorden(raiz):
    """Retorna lista de nodos en orden inorden."""
    secuencia = []
    def _inorden(nodo):
        if nodo is not None:
            _inorden(nodo.izquierda)
            secuencia.append(nodo)
            _inorden(nodo.derecha)
    _inorden(raiz)
    return secuencia


def obtener_secuencia_preorden(raiz):
    """Retorna lista de nodos en orden preorden."""
    secuencia = []
    def _preorden(nodo):
        if nodo is not None:
            secuencia.append(nodo)
            _preorden(nodo.izquierda)
            _preorden(nodo.derecha)
    _preorden(raiz)
    return secuencia


def obtener_secuencia_postorden(raiz):
    """Retorna lista de nodos en orden postorden."""
    secuencia = []
    def _postorden(nodo):
        if nodo is not None:
            _postorden(nodo.izquierda)
            _postorden(nodo.derecha)
            secuencia.append(nodo)
    _postorden(raiz)
    return secuencia


def obtener_aristas(raiz):
    """Retorna lista de (nodo_padre, nodo_hijo) para dibujar aristas."""
    aristas = []
    def _rec(nodo, padre=None):
        if nodo is not None:
            if padre is not None:
                aristas.append((padre, nodo))
            _rec(nodo.izquierda, nodo)
            _rec(nodo.derecha, nodo)
    _rec(raiz)
    return aristas


def calcular_posiciones(raiz, ancho_canvas, alto_canvas):
    """
    Calcula (x, y) para cada nodo. Usa inorden para x, nivel para y.
    Retorna dict: {id(nodo): (x, y)}
    """
    inorden = obtener_secuencia_inorden(raiz)
    n = len(inorden)
    if n == 0:
        return {}

    # Asignar x en orden inorden (espaciado uniforme)
    margen_x = 60
    espacio_x = (ancho_canvas - 2 * margen_x) / (n + 1) if n > 0 else ancho_canvas // 2
    pos_x = {id(nodo): margen_x + (i + 1) * espacio_x for i, nodo in enumerate(inorden)}

    # Asignar y por nivel (BFS)
    pos_y = {}
    nivel = 0
    cola = [(raiz, 0)]
    max_nivel = 0
    while cola:
        nodo, nivel = cola.pop(0)
        max_nivel = max(max_nivel, nivel)
        pos_y[id(nodo)] = nivel
        if nodo.izquierda is not None:
            cola.append((nodo.izquierda, nivel + 1))
        if nodo.derecha is not None:
            cola.append((nodo.derecha, nivel + 1))

    # Escalar y
    margen_y = 50
    espacio_y = (alto_canvas - 2 * margen_y) / (max_nivel + 2) if max_nivel > 0 else 80
    resultado = {}
    for nid in pos_x:
        nivel = pos_y.get(nid, 0)
        resultado[nid] = (pos_x[nid], margen_y + nivel * espacio_y)
    return resultado


class RecorridoBSTApp:
    def __init__(self, raiz: NodoBST):
        self.raiz = raiz
        self.secuencia_actual = []
        self.indice_actual = -1
        self.visitados = set()
        self.vertices = {}
        self.lineas_aristas = []
        self.ovals_nodos = []

        self.root = tk.Tk()
        self.root.title("Recorrido de BST - Paso a paso")
        self.root.configure(bg=COLOR_FONDO)
        self.root.minsize(800, 650)

        self._crear_ui()
        self._dibujar_arbol()

    def _crear_ui(self):
        # Frame de botones de recorrido
        frame_botones = ttk.Frame(self.root, padding=10)
        frame_botones.pack(fill=tk.X)

        ttk.Label(frame_botones, text="Tipo de recorrido:", font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Inorden", command=self._iniciar_inorden).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Preorden", command=self._iniciar_preorden).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_botones, text="Postorden", command=self._iniciar_postorden).pack(side=tk.LEFT, padx=5)

        # Frame de control de pasos
        frame_pasos = ttk.Frame(self.root, padding=10)
        frame_pasos.pack(fill=tk.X)

        ttk.Button(frame_pasos, text="◀ Anterior", command=self._anterior).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_pasos, text="Siguiente ▶", command=self._siguiente).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_pasos, text="Reiniciar", command=self._reiniciar).pack(side=tk.LEFT, padx=5)

        self.label_estado = ttk.Label(frame_pasos, text="Seleccione un recorrido para comenzar.", font=("Segoe UI", 10))
        self.label_estado.pack(side=tk.LEFT, padx=20)

        # Leyenda
        frame_leyenda = ttk.Frame(self.root, padding=5)
        frame_leyenda.pack(fill=tk.X)
        ttk.Label(frame_leyenda, text="■ No visitado  ■ Actual  ■ Visitado",
                  font=("Segoe UI", 9)).pack(side=tk.LEFT)
        canvas_leyenda = tk.Canvas(frame_leyenda, width=200, height=20)
        canvas_leyenda.pack(side=tk.LEFT, padx=10)
        canvas_leyenda.create_oval(5, 2, 22, 19, fill=COLOR_NODO_NORMAL, outline="#2c3e50")
        canvas_leyenda.create_oval(45, 2, 62, 19, fill=COLOR_NODO_ACTUAL, outline="#2c3e50")
        canvas_leyenda.create_oval(85, 2, 102, 19, fill=COLOR_NODO_VISITADO, outline="#2c3e50")

        # Canvas para el árbol
        self.canvas = tk.Canvas(self.root, width=780, height=450, bg="white",
                                highlightthickness=1, highlightbackground="#bdc3c7")
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.canvas.update()

    def _dibujar_arbol(self):
        self.canvas.delete("all")
        self.lineas_aristas = []
        self.ovals_nodos = []
        self.vertices = {}

        if self.raiz is None:
            self.canvas.create_text(390, 200, text="Árbol vacío", font=("Segoe UI", 16), fill="#7f8c8d")
            self.oval_a_nodo = {}
            return

        ancho = self.canvas.winfo_width() or 780
        alto = self.canvas.winfo_height() or 450
        pos = calcular_posiciones(self.raiz, ancho, alto)
        self.vertices = pos

        radio = 22

        # Dibujar aristas primero
        aristas = obtener_aristas(self.raiz)
        for padre, hijo in aristas:
            pid, hid = id(padre), id(hijo)
            if pid in pos and hid in pos:
                x1, y1 = pos[pid]
                x2, y2 = pos[hid]
                # Acortar líneas para que no sobresalgan del círculo
                from math import sqrt
                dx, dy = x2 - x1, y2 - y1
                dist = sqrt(dx*dx + dy*dy) or 1
                x1e = x1 + (dx / dist) * radio
                y1e = y1 + (dy / dist) * radio
                x2e = x2 - (dx / dist) * radio
                y2e = y2 - (dy / dist) * radio
                ln = self.canvas.create_line(x1e, y1e, x2e, y2e, fill=COLOR_ARISTA_NORMAL, width=2, tags="arista")
                self.lineas_aristas.append((padre, hijo, ln))

        # Dibujar nodos y texto
        inorden = obtener_secuencia_inorden(self.raiz)
        nodo_por_id = {id(n): n for n in inorden}
        self.oval_a_nodo = {}
        for nid, (x, y) in pos.items():
            oval = self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio,
                                          fill=COLOR_NODO_NORMAL, outline="#2c3e50", width=2, tags="nodo")
            self.ovals_nodos.append(oval)
            if nid in nodo_por_id:
                self.oval_a_nodo[oval] = nodo_por_id[nid]
            self.canvas.create_text(x, y, text=nodo_por_id[nid].persona.cedula if nid in nodo_por_id else "",
                                   font=("Segoe UI", 10, "bold"), fill=COLOR_TEXTO, tags="texto")
        self._actualizar_colores()

    def _actualizar_colores(self):
        """Actualiza colores de nodos según estado del recorrido."""
        if self.raiz is None:
            return

        nodo_actual = self.secuencia_actual[self.indice_actual] if 0 <= self.indice_actual < len(self.secuencia_actual) else None

        for item, nodo in self.oval_a_nodo.items():
            nid = id(nodo)
            if nodo == nodo_actual:
                color = COLOR_NODO_ACTUAL
            elif nid in self.visitados:
                color = COLOR_NODO_VISITADO
            else:
                color = COLOR_NODO_NORMAL
            self.canvas.itemconfig(item, fill=color)

        # Resaltar arista hacia el nodo actual
        for padre, hijo, ln_id in self.lineas_aristas:
            if nodo_actual is not None and (hijo == nodo_actual or (padre == nodo_actual and hijo not in self.visitados)):
                self.canvas.itemconfig(ln_id, fill=COLOR_ARISTA_ACTIVA, width=3)
            else:
                self.canvas.itemconfig(ln_id, fill=COLOR_ARISTA_NORMAL, width=2)

    def _iniciar_inorden(self):
        self.secuencia_actual = obtener_secuencia_inorden(self.raiz)
        self.indice_actual = -1
        self.visitados = set()
        self._actualizar_estado()
        self._actualizar_colores()

    def _iniciar_preorden(self):
        self.secuencia_actual = obtener_secuencia_preorden(self.raiz)
        self.indice_actual = -1
        self.visitados = set()
        self._actualizar_estado()
        self._actualizar_colores()

    def _iniciar_postorden(self):
        self.secuencia_actual = obtener_secuencia_postorden(self.raiz)
        self.indice_actual = -1
        self.visitados = set()
        self._actualizar_estado()
        self._actualizar_colores()

    def _siguiente(self):
        if not self.secuencia_actual:
            return
        if self.indice_actual < len(self.secuencia_actual) - 1:
            if self.indice_actual >= 0:
                self.visitados.add(id(self.secuencia_actual[self.indice_actual]))
            self.indice_actual += 1
            self.visitados.add(id(self.secuencia_actual[self.indice_actual]))
            self._actualizar_estado()
            self._actualizar_colores()

    def _anterior(self):
        if not self.secuencia_actual or self.indice_actual < 0:
            return
        self.visitados.discard(id(self.secuencia_actual[self.indice_actual]))
        self.indice_actual -= 1
        if self.indice_actual >= 0:
            self.visitados.discard(id(self.secuencia_actual[self.indice_actual]))
        self._actualizar_estado()
        self._actualizar_colores()

    def _reiniciar(self):
        self.indice_actual = -1
        self.visitados = set()
        self._actualizar_estado()
        self._actualizar_colores()

    def _actualizar_estado(self):
        if not self.secuencia_actual:
            self.label_estado.config(text="Árbol vacío.")
            return
        paso = self.indice_actual + 1
        total = len(self.secuencia_actual)
        if self.indice_actual < 0:
            self.label_estado.config(text=f"Paso 0/{total} - Presione Siguiente para iniciar.")
        elif self.indice_actual < total:
            cedula = self.secuencia_actual[self.indice_actual].persona.cedula
            self.label_estado.config(text=f"Paso {paso}/{total} - Nodo actual: {cedula}")
        else:
            self.label_estado.config(text=f"Recorrido completado. Total: {total} nodos.")

    def run(self):
        self.root.mainloop()


def main():
    """Ejemplo: crea un BST de prueba y abre la UI."""
    bst = BST()
    bst.insertar("Ana García", "105", "Colombia", 28)
    bst.insertar("Luis Pérez", "101", "Argentina", 35)
    bst.insertar("María López", "108", "México", 22)
    bst.insertar("Carlos Ruiz", "99", "España", 41)
    bst.insertar("Sofia Martínez", "103", "Chile", 30)
    bst.insertar("Pedro Sánchez", "107", "Perú", 26)
    bst.insertar("Laura Díaz", "110", "Uruguay", 33)

    app = RecorridoBSTApp(bst.raiz)
    app.run()


if __name__ == "__main__":
    main()
