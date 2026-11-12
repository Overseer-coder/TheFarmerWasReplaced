import movimentacao

candidatos = set()

def mover(dir, passos, tipo_cogumelo):
	for _ in range(passos):
		move(dir)
		if measure() == tipo_cogumelo:
			candidatos.add((get_pos_x(), get_pos_y()))

def calcular_manhattan(x_alvo, y_alvo):
	menor_distancia = 10000
	x_resp = 0
	y_resp = 0
	
	for x, y in candidatos:
		distancia_manhattan = abs(x - x_alvo) + abs(y - y_alvo)
		if distancia_manhattan < menor_distancia:
			menor_distancia = distancia_manhattan
			x_resp, y_resp = x, y
			
	return x_resp, y_resp

def localizar_mais_proximo_ao_redor_alvo(x_alvo, y_alvo, tipo_cogumelo_alvo):
	i = 1

	while True:
		
		mover(West, 1, tipo_cogumelo_alvo)
		mover(North, i, tipo_cogumelo_alvo)
		mover(East, i*2, tipo_cogumelo_alvo)
		mover(South, i*2, tipo_cogumelo_alvo)
		mover(West, i*2, tipo_cogumelo_alvo)
		mover(North, i, tipo_cogumelo_alvo)
		
		if candidatos:
			return calcular_manhattan(x_alvo, y_alvo)
			
		i += 1
	



	