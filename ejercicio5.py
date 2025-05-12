""" 
problema devolver_el_doble_si_es_par(numero : Z) {
	asegura: {si numero es par devuelve el doble de numero}
	asegura: {si numero es impar devuelve numero}
}

problema devolver_valor_si_es_par_sino_el_que_sigue(numero: Z) {
	asegura: {si numero es par devuelve numero}
	asegura: {si numero es impar devuelve numero+1}
}

problema devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: Z) {
	asegura: {si numero es multiplo de 3 devuelve 2*numero}
	asegura: {si numero es multiplo de 9 devuelve 3*numero}
	asegura: {caso contrario devuelve el mismo numero}
}

problema lindo_nombre (nombre : String) {
	asegura: {res="Tu nombre tiene muchas letras!" si la longitud es igual o mayor a 5}
	asegura: {res="Tu nombre tiene menos de 5 caracteres" de lo contrario}
}

problema elRango (numero : Z) {
	asegura: {imprime "Menor a 5" si numero es menor a 5}
	asegura: {imprime "Entre 10 y 20" si numero está entre 10 y 20}
	asegura: {imprime "Mayor a 20" si numero es mayor a 20}
}

problema vacaciones (edad : Z, sexo: Char) {
	asegura: {imprime "Andá de vacaciones" si edad<18 o bien edad>=60 y sexo="f" o bien edad>=65 y sexo="m"}
	asegura: {imprime "Te toca trabajar" en otro caso}
}

"""
def devolver_el_doble_si_es_par(numero : int):
	if (numero % 2 == 0):
		return 2*numero
	else:
		return numero
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int):
	if (numero % 2 == 0):
		return numero
	else:
		return numero+1
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int):
	if (numero%9==0):
		return 3*numero
	elif (numero%3==0):
		return 2*numero
	else:
		return numero
def lindo_nombre (nombre : str):
	if (len(nombre) >= 5):
		return "Tu nombre tiene muchas letras!"
	else:
		return "Tu nombre tiene menos de 5 caracteres"
def elRango (numero : int):
	if (numero < 5):
		print("Menor a 5")
	elif (numero >= 10 and numero <= 20):
		print("Entre 10 y 20")
	elif (numero > 20):
		print("Mayor a 20")
def vacaciones (edad : int, sexo: str):
	if (edad < 18 or (edad >= 60 and sexo=="f")  or (edad >= 65 and sexo=="m")):
		print("Andá de vacaciones!")
	else:
		print("Te toca trabajar")

