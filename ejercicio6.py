def del_1_al_10():
	i:int = 1
	while (i<=10):
		print(i)
		i+=1

def pares_10_al_40():
	i : int = 10
	while (i <= 40):
		print(i)
		i+=2

def eco_10_veces():
	i : int = 10
	while (i > 0):
		print ("eco")
		i -= 1

def cuenta_regresiva(n: int):
	while (n >= 1):
		print(n)
		n -= 1
	print("Despegue")

def viaje_en_el_tiempo(partida: int, llegada: int):
	while (partida > llegada):
		partida-=1
		print(f"Viajó un año al pasado, estamos en el año: {partida}")

def viaje_a_aristoteles(partida: int):
	while (partida > -384):
		partida-=20
		print(f"Viajó 20 años al pasado, estamos en el año: {partida}")

