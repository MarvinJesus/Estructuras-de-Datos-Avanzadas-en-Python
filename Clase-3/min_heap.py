class MinHeap:
    def __init__(self, elementos = None):
        self.heap = []

        if elementos:
            self.heap = elementos[:]
            self._build_heap()

    def _build_heap(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    @staticmethod
    def _padre(i):
        return (i - 1) // 2

    @staticmethod
    def _izquierdo(i):
        return 2 * i + 1

    @staticmethod
    def _derecho(i):
        return 2 * i + 2

    def _heapify_down(self, i):
        menor = i
        izquierdo = self._izquierdo(i)
        derecho = self._derecho(i)

        if izquierdo < len(self.heap) and self.heap[izquierdo] < self.heap[menor]:
            menor = izquierdo

        if derecho < len(self.heap) and self.heap[derecho] < self.heap[menor]:
            menor = derecho

        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._heapify_down(menor)

    def _heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self._padre(i)]:
            self.heap[i], self.heap[self._padre(i)] = (
                self.heap[self._padre(i)],
                self.heap[i],
            )
            i = self._padre(i)

    def insertar(self, valor):
        self.heap.append(valor)
        self._heapify_up(len(self.heap) - 1)

    def extraer_min(self):
        if self._esta_vacio():
            raise IndexError("El montículo está vacío.")

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return raiz

    def minimo(self):
        if self._esta_vacio():
            raise IndexError("El montículo está vacío.")
        return self.heap[0]

    def _esta_vacio(self):
        return len(self.heap) == 0