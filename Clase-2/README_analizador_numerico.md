# Clase `AnalizadorAritmeticoNumerico`

Clase que valida expresiones aritméticas **solo con valores numéricos**: comprueba que los delimitadores `( ) [ ] { }` estén balanceados (usando la **Pila** de `pila.py`) y que cada operador tenga un número a la izquierda y a la derecha. **No admite variables** (letras como `a`, `x`, `num`).

Archivo: `analizador_aritmetico_numerico.py`

---

## Propósito

- **Aceptar** expresiones como: `2 + 3`, `(2 + 3) * 4`, `-5 + 3`, `1 < 2`, `3 >= 2`, `{[(2 + 3) * 4] + 1}`.
- **Rechazar**: variables (`a + 2`), operandos faltantes (`2 + `, `+ 3`), delimitadores mal emparejados (`(2 + 3`), dos operadores seguidos (`2 ++ 3`).

---

## Constructor y propiedades privadas

`__init__(self)` no recibe argumentos e inicializa las **propiedades privadas** que usa la tokenización y la validación:

| Propiedad      | Tipo        | Descripción |
|----------------|-------------|-------------|
| `self._N`, `self._O`, `self._A`, `self._C` | `str` | Tipos de token: número, operador, apertura, cierre (`"N"`, `"O"`, `"A"`, `"C"`) |
| `self._PARES`  | `dict`      | Relación cierre → apertura: `')' → '('`, `']' → '['`, `'}' → '{'` |
| `self._APERTURAS` | `frozenset` | Caracteres de apertura: `(`, `[`, `{` |
| `self._CIERRES`   | `frozenset` | Caracteres de cierre: `)`, `]`, `}` |
| `self._OP_DOBLES` | `frozenset` | Operadores de 2 caracteres: `==`, `>=`, `<=`, `!=` |
| `self._OP_UNO`    | `frozenset` | Operadores de 1 carácter: `+`, `-`, `*`, `/`, `<`, `>`, `=` |

La **Pila** (`pila.py`) no se crea en el constructor; se instancia dentro de `_tokenizar` al inicio de cada validación.

---

## Método público

### `validar(self, expresion: str) -> bool`

**Único método pensado para usarse desde fuera.**

- **Entrada**: cadena con la expresión (p. ej. `"2 + 3"`).
- **Salida**: `True` si la expresión es válida; `False` en caso contrario.

Reglas:

1. Si la expresión está vacía o solo tiene espacios → `False`.
2. Se hace `strip()` y se llama a `_tokenizar`. Si hay variable o delimitadores desbalanceados → `False`.
3. Se llama a `_estructura_ok(tokens)`. Si la secuencia de tokens no es correcta → `False`.
4. Si todo pasa → `True`.

**Ejemplo de uso:**

```python
from analizador_aritmetico_numerico import AnalizadorAritmeticoNumerico

analizador = AnalizadorAritmeticoNumerico()
analizador.validar("2 + 3")       # True
analizador.validar("a + 2")       # False (variable)
analizador.validar("(2 + 3")      # False (falta cierre)
```

---

## Métodos internos (privados)

### `_es_numero(self, s: str) -> bool`

Indica si `s` es un número válido (entero o decimal).

- Rechaza cadenas vacías o inválidas como `"."`, `"-"`, `"-."`.
- Usa `float(s)` para comprobar; si no lanza `ValueError`, se considera número.

---

### `_leer_numero(self, expr: str, pos: int) -> tuple`

Lee un número desde la posición `pos` en `expr`.

- Avanza mientras haya dígitos o punto (`.`) y construye la subcadena.
- **Devuelve**: `(texto_numero, pos_siguiente)` si el texto es un número válido (según `_es_numero`), o `(None, pos)` si no.

Usado para números positivos y para el signo negativo (p. ej. `-5`).  
*(Detalle del bucle en `README_leer_numero.md`.)*

---

### `_tokenizar(self, expr: str)`

Recorre la expresión **una sola vez** y hace:

1. **Tokenizar**: dividir en unidades (números, operadores, aperturas, cierres).
2. **Validar delimitadores**: usa la clase **Pila** (`pila.py`): se apilan las aperturas y al ver un cierre se hace `pop` y se comprueba con `self._PARES`.

Cada token es una tupla `(tipo, valor)` donde `tipo` es `self._N`, `self._O`, `self._A` o `self._C`.

- Si encuentra **cualquier letra** → devuelve `None`.
- Si los delimitadores no están balanceados → devuelve `None`.
- Si un número no es válido o un operador no está permitido → devuelve `None`.
- Si todo es correcto → devuelve la **lista de tokens**.

Casos especiales:

- **Signo negativo**: si aparece `-` tras una apertura, un operador o al inicio, se interpreta como número (p. ej. `-5`). Se usa `_leer_numero` y se emite un token de tipo número con valor `"-" + txt`.
- **Operadores de 2 caracteres**: si hay `==`, `>=`, `<=` o `!=`, se emite un solo token y se avanza 2 posiciones.

*(Detalle paso a paso en `README_tokenizar.md`.)*

---

### `_estructura_ok(self, tokens: list) -> bool`

Comprueba que la lista de tokens tenga una **estructura válida** de expresión aritmética:

- Secuencia: **operando** ( **operador** **operando** ) repetido las veces que haga falta.
- **Operando** puede ser:
  - un token de tipo número (`self._N`), o
  - una **subexpresión entre paréntesis**: apertura (`self._A`), expresión válida, cierre (`self._C`).

Implementación con un **bucle iterativo**: una lista hace de pila para los paréntesis anidados y un flag `need_op` indica si se espera operando o operador. Se recorre la lista de tokens y se valida la alternancia y el balance de aperturas/cierres. Al final, la expresión es válida si la pila queda vacía y no se está esperando un operando.

---

## Flujo completo de `validar(expresion)`

```
expresion
    │
    ├─ vacía o solo espacios? → False
    │
    ▼
expresion.strip()
    │
    ▼
_tokenizar(expr)
    │  • Recorre carácter a carácter
    │  • Usa Pila para balance ( ) [ ] { }
    │  • Emite tokens (N, O, A, C)
    │  • Si hay letra o error → None
    │
    ├─ None? → False
    │
    ▼
lista_tokens
    │
    ▼
_estructura_ok(tokens)
    │  • operando (operador operando)*
    │  • operando = número o ( subexpresión )
    │
    ├─ False? → False
    │
    ▼
True
```

---

## Ejemplo de uso (main del script)

Al ejecutar el archivo se usa el bloque `if __name__ == "__main__":`:

```python
analizador = AnalizadorAritmeticoNumerico()
pruebas = [
    "2 + 3", "10.5 * 4", "{[(2 + 3) * 4] + 1}", "((1 + 2) * 3) - 4", "-5 + 3",
    "1 < 2", "3 >= 2", "2 + 3 * 4", "", "a + 2", "2 + b", "2 + ", "+ 3",
    "2 ++ 3", "(2 + 3", "2 + 3)", ...
]
for expr in pruebas:
    ok = analizador.validar(expr)
    print(f"  '{expr}'  ->  {'VÁLIDA' if ok else 'NO VÁLIDA'}")
```

---

## Documentación relacionada

- **`README_tokenizar.md`**: explicación detallada del método `_tokenizar`.
- **`README_leer_numero.md`**: explicación del bucle `while` en `_leer_numero`.
