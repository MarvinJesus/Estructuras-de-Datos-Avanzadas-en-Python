# Clase 2 — Pilas y Analizador Aritmético

## Analizador Aritmético

Este ejercicio **no fue dejado por el profesor**; es un ejercicio complementario de práctica para afianzar el uso de la **pila** (`pila.py`), de **diccionarios** y de una validación muy sencilla de **sintaxis aritmética**.

### ¿De dónde viene la idea?

El problema de **validar expresiones con delimitadores balanceados** (paréntesis, corchetes, llaves) es un clásico de algoritmos y compiladores. Aparece en:

- Libros de estructuras de datos (por ejemplo, *Introduction to Algorithms* o textos de lenguajes formales).
- Cursos de compiladores e intérpretes: los analizadores sintácticos usan pilas para verificar que los símbolos de apertura y cierre coincidan.
- Entrevistas técnicas y ejercicios de programación (por ejemplo, “valid parentheses” en LeetCode).

La idea es: **recorrer la expresión carácter a carácter** y, usando una **pila**, ir apilando cada delimitador de apertura y desapilando cuando aparece su cierre correspondiente. Si al final la pila queda vacía y nunca hubo un cierre sin su apertura (ni un par que no coincida), la expresión es válida.

---

### El algoritmo (resumen)

1. **Entrada**: una cadena (expresión) que puede contener `( ) [ ] { }` y otros caracteres.
2. **Estructuras**:
   - Una **pila**: guarda solo los delimitadores de **apertura** `(`, `[`, `{`.
   - Un **diccionario**: relaciona cada delimitador de **cierre** con su apertura (`')' → '('`, `']' → '['`, `'}' → '{'`). Así, al ver un cierre, sabemos qué apertura debe estar en el tope de la pila.
3. **Reglas**:
   - Si el carácter es de **apertura** → se hace **push** en la pila.
   - Si es de **cierre** → se hace **pop** y se comprueba que el elemento sacado coincida con el esperado según el diccionario. Si la pila está vacía (pop falla) o no coincide → expresión **no válida**.
   - El resto de caracteres (números, operadores, letras) se ignoran para la parte de delimitadores.
4. **Resultado (versión actual)**:
   - Si al terminar de recorrer la expresión la pila está **vacía** y además la sintaxis básica de operadores es correcta → expresión **válida**.
   - Si hay error en delimitadores o en operadores, la pila **no queda vacía**. En caso de que exista alguna apertura, se conserva (al menos) la **primera llave/paréntesis de apertura**; si no hubo aperturas, se deja una llave `{` simbólica para indicar el fallo.

La propiedad importante es el **orden LIFO** de la pila: el último delimitador de apertura que entró debe ser el primero en cerrarse, que es exactamente lo que exige la sintaxis correcta de paréntesis/corchetes/llaves anidados.

---

### Cómo se valida que la expresión sea “sintácticamente correcta”

Este analizador comprueba dos cosas:

1. **Delimitadores** `( ) [ ] { }` balanceados y bien anidados.
2. **Sintaxis muy simple de operadores** aritméticos/comparación (`+ - * / < = >`), por ejemplo que no haya `2++2`, `num+-2`, `*9+1`, `2+3*`, etc.

Para los delimitadores:

1. **Cada apertura tiene su cierre**  
   Si aparece `(`, `[` o `{`, más adelante debe aparecer el `)`, `]` o `}` que le corresponde. Si al terminar de leer la expresión la pila sigue teniendo elementos, hay aperturas sin cerrar → **no válido**.

2. **Cada cierre corresponde al último abierto**  
   Cuando vemos un `)`, `]` o `}`, debe “cerrar” justo al último `(`, `[` o `{` que se abrió y aún no se cerró. Eso se controla con la pila: al ver un cierre hacemos **pop** y comprobamos que el carácter sacado sea el del par correcto (usando el diccionario). Si no coincide o la pila está vacía → **no válido**. Así se evitan cosas como `([)]`, donde el `)` cierra antes que el `]` y el orden de anidamiento es incorrecto.

3. **No puede haber cierre sin apertura**  
   Si en algún momento hay un `)`, `]` o `}` y la pila está vacía, significa que ese cierre no tiene una apertura previa → **no válido**.

En resumen: la expresión se considera **válida en (esta) sintaxis** cuando los delimitadores están **balanceados** y **correctamente anidados**, y los operadores no tienen errores sencillos (no empiezan/terminan en operador, ni hay dos operadores seguidos).

#### Ejemplo paso a paso: `"( 2 + 3 )"`

| Carácter | Acción en la pila | Estado |
|----------|-------------------|--------|
| `(`      | push `(`          | Pila: `['(']` |
| ` `, `2`, `+`, `3`, ` ` | (se ignoran) | Pila: `['(']` |
| `)`      | pop → sale `(`, coincide con `)` | Pila: `[]` |

Al terminar, la pila está vacía → expresión **válida** (en delimitadores). Después se puede dejar el valor **1** en la pila como señal de éxito.

#### Ejemplo que falla: `"([)]"`

| Carácter | Acción | Problema |
|----------|--------|----------|
| `(`      | push `(`  | Pila: `['(']` |
| `[`      | push `[`  | Pila: `['(', '[']` |
| `)`      | pop → sale `[`; se esperaba `(` para `)` | **No coincide** → **no válido** |

Así se ve que el orden de cierre es incorrecto: el `)` intenta cerrar el `(`, pero en el tope de la pila está `[`, por tanto la expresión no es sintácticamente correcta en delimitadores.

**Qué no se valida:** Que la expresión sea matemáticamente correcta en sentido amplio (por ejemplo, precedencias completas de operadores, tipos de datos, etc.). Solo se comprueban los delimitadores y unas pocas reglas muy simples sobre operadores (`+ - * / < = >`).

---

### Uso

```python
from analizador_aritmetico import AnalizadorAritmetico

a = AnalizadorAritmetico()
expr = "(2 + 3) * 4"
es_valida = a.validar(expr)
print(expr, "->", "VÁLIDA" if es_valida else "NO VÁLIDA", "; pila vacía?", a.esta_vacia())
```

Ejecutar el módulo directamente para ver varias expresiones de ejemplo:

```bash
python analizador_aritmetico.py
```

---

### Archivos de la clase

- `pila.py` — Implementación de la pila usada por el analizador.
- `analizador_aritmetico.py` — Clase que valida expresiones usando la pila y diccionarios.
- `cola.py` — Implementación de cola (si aplica).
