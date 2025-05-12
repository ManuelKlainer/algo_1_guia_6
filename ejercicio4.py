import math
def peso_pino (altura : float):
	altura_en_cm = altura * 100
	base = min (altura_en_cm, 300) * 3
	extra = max(altura_en_cm - 300, 0) * 2
	return base + extra

def es_peso_util (peso: float):
	return min(peso,400) == 400 and max(peso,1000) == 1000

def sirve_pino (altura: float):
	return es_peso_util (peso_pino (altura))
