import math
def imprimir_saludo (nombre: str)  -> str:
	print ("Hola "+nombre)

def raiz_cuadrada_de(n: float) -> float:
	return math.sqrt(n)

def farenheit_a_celcius (t: float) -> float:
	return ((t-32)*5)/9

def imprimir_dos_veces(estribillo: str) -> str:
	return estribillo * 2

def es_multiplo_de(n: int, m: int) -> bool:
	return (n % m == 0)

def es_par(n: int) -> bool:
	return es_multiplo_de(n,2)

def cantidad_de_pizzas(comenzales: int, porciones: int) -> int:
	return (comenzales*porciones + 8 - (comenzales * porciones) % 8) // 8
