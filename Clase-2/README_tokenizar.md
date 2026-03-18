# El método `_tokenizar` (línea 40)

El método `_tokenizar(self, expr: str)` en `analizador_aritmetico_numerico.py` recorre la expresión **una sola vez** y hace dos cosas:

1. **Tokeniza**: divide la expresión en unidades con sentido (números, operadores, paréntesis, etc.).
2. **Valida delimitadores**: usa la **Pila** (`pila.py`) para comprobar que los `( ) [ ] { }` estén bien balanceados.

Si encuentra una variable (letra) o delimitadores mal emparejados, devuelve `None`. Si todo es correcto, devuelve una **lista de tokens**: cada token es una tupla `(tipo, valor)`.

---

## ¿Qué es un token?

Un **token** es un elemento mínimo de la expresión. Por ejemplo, en `"2 + 3"` hay tres tokens:

| Token    | Tipo (self._N, self._O, …) | Valor |
|----------|----------------------------|--------|
| número   | `"N"`                      | `"2"`  |
| operador | `"O"`                      | `"+"`  |
| número   | `"N"`                      | `"3"`  |

Los tipos son las propiedades privadas de la clase: `self._N` (número), `self._O` (operador), `self._A` (apertura), `self._C` (cierre).

---

## Inicio del método (líneas 42–44)

```python
self._pila = Pila()
tokens = []
pos, n = 0, len(expr)
```

- **`self._pila = Pila()`**: se crea una pila nueva para esta validación. En ella se apilan solo los delimitadores de **apertura** `(`, `[`, `{`. Al ver un cierre `)`, `]`, `}`, se hace `pop` y se comprueba que coincida con el par esperado (`self._PARES`).
- **`tokens`**: lista donde se irán guardando los tokens `(tipo, valor)`.
- **`pos`, `n`**: índice de recorrido y longitud de la expresión.

---

## Bucle principal: `while pos < n`

En cada iteración:

### 1. Saltar espacios (líneas 47–50)

```python
while pos < n and expr[pos].isspace():
    pos += 1
if pos >= n:
    break
c = expr[pos]
```

Se avanza `pos` mientras haya espacios. Si se llega al final, se sale del bucle. Si no, `c` es el siguiente carácter a procesar.

### 2. Delimitador de apertura `( [ {` (líneas 53–56)

Si `c in self._APERTURAS`:

- **`self._pila.push(c)`**: se apila el carácter (para comprobar luego que su cierre coincida).
- Se añade el token `(self._A, c)`.
- `pos += 1`.

### 3. Delimitador de cierre `) ] }` (líneas 57–63)

Si `c in self._CIERRES`:

- Se hace **`self._pila.pop()`**. Si la pila está vacía, `pop` lanza `IndexError` → se devuelve `None`.
- Si el valor desapilado **no** es el esperado según `self._PARES[c]` (por ejemplo `]` cerrando un `(`), se devuelve `None`.
- Se añade el token `(self._C, c)` y se avanza `pos`.

### 4. Operadores y signo negativo (líneas 64–80)

Si `c` es un carácter de operador (`self._OP_UNO` o `"!"`):

- **Signo negativo como número**: si aún no hay tokens o el último token es operador o apertura (`self._O`, `self._A`), el `-` se interpreta como signo de un número. Se avanza `pos`, se llama a `self._leer_numero(expr, pos)` y se añade un token de tipo número con valor `"-" + txt`. Si no se puede leer un número válido, se devuelve `None`.
- **Operador de dos caracteres**: si los dos caracteres forman `==`, `>=`, `<=` o `!=` (`self._OP_DOBLES`), se añade ese operador y `pos += 2`.
- **Operador de un carácter**: si `c in self._OP_UNO`, se añade `(self._O, c)` y `pos += 1`.
- En cualquier otro caso (por ejemplo `!` solo) se devuelve `None`.

### 5. Número (líneas 81–85)

Si `c` es dígito o punto:

- Se llama a `self._leer_numero(expr, pos)` para leer el número completo.
- Si el resultado no es válido, se devuelve `None`.
- Se añade el token `(self._N, txt)` y `pos` queda actualizado por `_leer_numero`.

### 6. Letra (variable) (líneas 86–87)

Si `c.isalpha()`: se considera variable. El analizador **solo admite números**, así que se devuelve `None`.

### 7. Otro carácter (líneas 88–89)

Cualquier otro carácter se ignora y se hace `pos += 1`.

---

## Final del método (línea 91)

```python
return None if len(self._pila) else tokens
```

Si al terminar el recorrido la **pila no está vacía**, faltan cierres (por ejemplo `(2 + 3` sin `)`). En ese caso se devuelve `None`. Si la pila está vacía, se devuelve la lista `tokens`.

---

## Resumen del flujo (ejemplo)

Expresión: `" ( 2 + 3 ) * 4 "`

1. Saltar espacios → `'('` → push en la pila, token `(A, '(')`.
2. Saltar espacios → `'2'` → `_leer_numero` → token `(N, "2")`.
3. Saltar espacios → `'+'` → token `(O, "+")`.
4. Saltar espacios → `'3'` → token `(N, "3")`.
5. Saltar espacios → `')'` → pop, coincide con `'('` → token `(C, ')')`.
6. Saltar espacios → `'*'` → token `(O, "*")`.
7. Saltar espacios → `'4'` → token `(N, "4")`.
8. Fin de la expresión. Pila vacía → se devuelve la lista de tokens.

Esa lista la usa después `_estructura_ok` para comprobar que la secuencia sea correcta (operando, operador, operando, …).

---

## Valor de retorno

- **Lista de tokens** `[(tipo, valor), ...]` si la expresión es válida (solo números, delimitadores balanceados, sin variables).
- **`None`** si hay variable, delimitadores mal emparejados, número inválido u operador mal formado.
