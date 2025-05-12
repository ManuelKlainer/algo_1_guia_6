def del_1_al_10():
	for i in range(1,11):
		print(i)

def pares_10_al_40():
	for i in range(10,41,2):
			print(i)

def eco_10_veces():
	for i in range (10):
		print ("eco")

def cuenta_regresive(n: int):
	for i in range (n, 0, -1):
		print (i)
	print("Despegue")

def viaje_en_el_tiempo(partida: int, llegada: int):
	for i in range (partida -1 ,llegada -1, -1):
		print(f"Viajó un año al pasado, estamos en el año: {i}")

def viaje_al_pasado(partida: int):
	for i in range (partida -20, -384 -1, -20):
		print(f"Viajó 20 años al pasado, estamos en el año: {i}")

