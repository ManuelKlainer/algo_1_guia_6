
# Ejercicio 9 – Funciones con y sin uso de `global`

## Código base
```python
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g
```

---

## 1. ¿Cuál es el resultado de evaluar tres veces seguidas `ro(1)`?

Evaluación paso a paso:
- `g = 0` inicialmente
- `ro(1)` → g = 1 → retorna 1 + 1 = 2
- `ro(1)` → g = 2 → retorna 1 + 2 = 3
- `ro(1)` → g = 3 → retorna 1 + 3 = 4

**Resultado:** `2, 3, 4`

---

## 2. ¿Cuál es el resultado de evaluar tres veces seguidas `rt(1, 0)`?

Como `rt` no modifica la variable global `g` y siempre recibe `g = 0`:

Evaluación:
- `rt(1, 0)` → g interno = 0 + 1 = 1 → retorna 1 + 1 = 2
- `rt(1, 0)` → idem → 2
- `rt(1, 0)` → idem → 2

**Resultado:** `2, 2, 2`

---

## 3. Ejecución simbólica de cada función

### `rt(x: int, g: int) -> int`
```python
g = g + 1
return x + g
```
Ejemplo: `rt(1, 0)`

- x ← 1
- g ← 0
- g ← g + 1 → g = 1
- return x + g → 1 + 1 = 2

---

### `ro(x: int) -> int`
```python
global g
g = g + 1
return x + g
```
Ejemplo: con g inicial en 0 y llamando a `ro(1)`

- g ← 0
- g ← g + 1 → g = 1
- return x + g → 1 + 1 = 2

---

## 4. Especificaciones de las funciones

### Especificación de `rt`

```text
problema rt(x: int, g: int) : int {
  requiere: { True }
  asegura: { resultado = x + g + 1 }
}
```

### Especificación de `ro`

```text
problema ro(x: int) : int {
  requiere: { existe una variable global g: int }
  asegura: {
    g final = g inicial + 1
    resultado = x + g final
  }
}
```
