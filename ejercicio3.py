def alguno_es_0(a : float, b : float) -> bool:
	if (a==0 or b == 0):
		return True
	return False

def ambos_son_0(a : float, b : float) -> bool:
	if (a==0 and b == 0):
		return True
	return False

def es_nombre_largo(nombre : str) -> bool:
	return (3<=len(nombre) and 8>=len(nombre))

def es_bisiesto (año : int) -> bool:
	if (año % 400 == 0 or (año % 4 == 0 and año % 100 != 0)):
		return True
	return False
