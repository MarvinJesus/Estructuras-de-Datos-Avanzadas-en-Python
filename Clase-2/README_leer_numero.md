# El `while` en `_leer_numero` (línea 35)

En el método `_leer_numero` del archivo `analizador_aritmetico_numerico.py` aparece este bucle:

```python
while i < len(expr) and (expr[i].isdigit() or expr[i] == "."):
    i += 1
```

## ¿Qué hace?

Ese `while` **avanza el índice `i`** mientras el carácter actual de la expresión sea:

- un **dígito** (`0`–`9`), o  
- un **punto** (`.`).

Es decir: recorre la cadena desde la posición `pos` y se detiene cuando encuentra algo que **no** es dígito ni punto (o cuando se acaba la cadena).

## ¿Para qué sirve?

El método `_leer_numero` debe leer **un solo número** dentro de la expresión (entero o decimal), por ejemplo:

- `"2"` → un carácter
- `"10.5"` → dígitos, punto, dígitos
- `"123"` → solo dígitos

El bucle va carácter a carácter y **acumula** todo lo que forma parte del número:

1. **`i < len(expr)`**  
   Evita salirse de la cadena. Si `i` llega al final, se deja de mirar caracteres.

2. **`expr[i].isdigit()`**  
   Comprueba si el carácter en la posición `i` es un dígito (`0`–`9`). Así se aceptan números como `42` o `7`.

3. **`expr[i] == "."`**  
   Permite el punto decimal. Así se pueden leer números como `3.14` o `0.5`.

4. **`i += 1`**  
   En cada iteración se avanza una posición para seguir leyendo el siguiente carácter.

Cuando el `while` termina, `i` queda en la **primera posición después del número**.  
Con `texto = expr[pos:i]` se obtiene la subcadena que corresponde al número (por ejemplo `"10.5"`), y luego `_es_numero(texto)` comprueba que sea un número válido (que no sea solo `"."`, etc.).

## Ejemplo

Para `expr = "2 + 3"` y `pos = 0`:

- `i = 0`: `expr[0]` es `'2'` → es dígito → `i` pasa a 1.
- `i = 1`: `expr[1]` es `' '` → no es dígito ni punto → el `while` termina.
- `texto = expr[0:1]` → `"2"`.
- Se devuelve `("2", 1)` (número leído y posición siguiente).

Para `expr = "10.5 * 4"` y `pos = 0`:

- El bucle avanza mientras vea `'1'`, `'0'`, `'.'`, `'5'`.
- Al llegar al espacio, sale del `while`.
- `texto = "10.5"` y se devuelve `("10.5", 4)`.

En resumen: ese `while` es el que **delimita** en la expresión la secuencia de caracteres que forman un único número (dígitos y un punto decimal).
