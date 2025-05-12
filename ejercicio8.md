
# Ejercicio 8 – Ejecución simbólica

Realizar la ejecución simbólica de los siguientes códigos:

---

## 1.  
```python
x = 5
y = 7
x = x + y
```

**Ejecución simbólica:**

- x ← 5  
- y ← 7  
- x ← x + y = 5 + 7 = 12  
**Resultado final:** `x = 12`, `y = 7`

---

## 2.  
```python
x = 5
y = 7
z = x + y
y = z * 2
```

**Ejecución simbólica:**

- x ← 5  
- y ← 7  
- z ← x + y = 5 + 7 = 12  
- y ← z * 2 = 12 * 2 = 24  
**Resultado final:** `x = 5`, `y = 24`, `z = 12`

---

## 3.  
```python
x = 5
y = 7
x = "hora"
y = x * 2
```

**Ejecución simbólica:**

- x ← 5  
- y ← 7  
- x ← "hora"  
- y ← x * 2 = "hora" * 2 = "horahora"  
**Resultado final:** `x = "hora"`, `y = "horahora"`

---

## 4.  
```python
x = False
res = not(x)
```

**Ejecución simbólica:**

- x ← False  
- res ← not(x) = not(False) = True  
**Resultado final:** `x = False`, `res = True`

---

## 5.  
```python
x = False
x = not(x)
```

**Ejecución simbólica:**

- x ← False  
- x ← not(x) = not(False) = True  
**Resultado final:** `x = True`

---

## 6.  
```python
x = True
y = False
res = x and y
x = res and x
```

**Ejecución simbólica:**

- x ← True  
- y ← False  
- res ← x and y = True and False = False  
- x ← res and x = False and True = False  
**Resultado final:** `x = False`, `y = False`, `res = False`
