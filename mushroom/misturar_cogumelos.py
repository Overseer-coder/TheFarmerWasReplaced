#tentar mover mistura nas posicoes cardeais e colaterais de forma horária
	#se conseguir, vá para a posição que moveu, marca local de onde veio, para não voltar, e reinicia
	#se não conseguir, ir para o bloco que travou e tenta mover nas posicoes cardeais
		#se conseguir, move mistura para a mesma direção que tentou ir e reinicia
		#se não conseguir, retorna e continua posicoes

#para posicoes colaterais, caso consiga mover, é necessário mover o bloco da
#posição anterior para esse mesmo bloco, caso haja um outro bloco naquele mesmo Z anteriormente, 
#exemplo: consegui mover nordeste e Z = 1, então bloco do norte toma este lugar se houver um bloco Z = 1
import movimentacao

anteriores_colaterais_sentido_horario = {
	"NorthEast":North,
	"SouthEast":East,
	"SouthWest":South,
	"NorthWest":West
}

direcoes_coord = [
	(0, 1),   #North
	(1, 1),   #NorthEast
	(1, 0),   #East
	(1, -1),  #SouthEast
	(0, -1),  #South
	(-1, -1), #SouthWest
	(-1, 0),  #West
	(-1, 1)   #NorthWest
]

direcoes_cardeais = [
	North,
	East,
	South,
	West
]

visitados = set()

def achar_caminho_ate_alvo(x_mistura, y_mistura, x_alvo, y_alvo):
	movimentacao.goto(x_mistura, y_mistura)
	camada_corrente = get_pos_z()
	
	while True:
		if (get_pos_x(), get_pos_y() + 1) not in visitados:
			
			conseguiu_empurrar_north = push(North)
				
			if conseguiu_empurrar_north:
				move(North)
				x_mistura, y_mistura = get_pos_x(), get_pos_y()
				visitados.add((get_pos_x(), get_pos_y()))
				continue
			else:
				move(North)
				conseguiu = False
				for dir in direcoes_cardeais:
					if push(dir):
						conseguiu = True
						break
				if not conseguiu:
					movimentacao.goto(x_mistura, y_mistura)
				else:
					move(South)
					push(North)
					move(North)
					x_mistura, y_mistura = get_pos_x(), get_pos_y()
					visitados.add((get_pos_x(), get_pos_y()))
					continue
		########################################################################		
		move(North)
		necessario_reposicao_anterior = get_pos_z() == camada_corrente
		move(East)
		conseguiu = False
			
		for dir in direcoes_cardeais:
			if push(dir):
				conseguiu = True
				break
		if conseguiu and necessario_reposicao_anterior:
			move(West)
			push(East)
		movimentacao.goto(x_mistura, y_mistura)
		########################################################################
		
		if (get_pos_x() + 1, get_pos_y()) not in visitados:
			
			conseguiu_empurrar_east = push(East)
				
			if conseguiu_empurrar_east:
				move(East)
				x_mistura, y_mistura = get_pos_x(), get_pos_y()
				visitados.add((get_pos_x(), get_pos_y()))
				continue
			else:
				move(East)
				conseguiu = False
				for dir in direcoes_cardeais:
					if push(dir):
						conseguiu = True
						break
				if not conseguiu:
					movimentacao.goto(x_mistura, y_mistura)
				else:
					move(West)
					push(East)
					move(East)
					x_mistura, y_mistura = get_pos_x(), get_pos_y()
					visitados.add((get_pos_x(), get_pos_y()))
					continue
		########################################################################			
		move(East)
		necessario_reposicao_anterior = get_pos_z() == camada_corrente
		move(South)
		conseguiu = False
			
		for dir in direcoes_cardeais:
			if push(dir):
				conseguiu = True
				break
		if conseguiu and necessario_reposicao_anterior:
			move(North)
			push(South)
		movimentacao.goto(x_mistura, y_mistura)
		########################################################################
		if (get_pos_x(), get_pos_y() - 1) not in visitados:
			
			conseguiu_empurrar_south = push(South)
				
			if conseguiu_empurrar_south:
				move(South)
				x_mistura, y_mistura = get_pos_x(), get_pos_y()
				visitados.add((get_pos_x(), get_pos_y()))
				continue
			else:
				move(South)
				conseguiu = False
				for dir in direcoes_cardeais:
					if push(dir):
						conseguiu = True
						break
				if not conseguiu:
					movimentacao.goto(x_mistura, y_mistura)
				else:
					move(North)
					push(South)
					move(South)
					x_mistura, y_mistura = get_pos_x(), get_pos_y()
					visitados.add((get_pos_x(), get_pos_y()))
					continue
		########################################################################			
		move(South)
		necessario_reposicao_anterior = get_pos_z() == camada_corrente
		move(West)
		conseguiu = False
			
		for dir in direcoes_cardeais:
			if push(dir):
				conseguiu = True
				break
		if conseguiu and necessario_reposicao_anterior:
			move(East)
			push(West)
		movimentacao.goto(x_mistura, y_mistura)
		########################################################################
		if (get_pos_x() - 1, get_pos_y()) not in visitados:
			
			conseguiu_empurrar_west = push(West)
				
			if conseguiu_empurrar_west:
				move(West)
				x_mistura, y_mistura = get_pos_x(), get_pos_y()
				visitados.add((get_pos_x(), get_pos_y()))
				continue
			else:
				move(West)
				conseguiu = False
				for dir in direcoes_cardeais:
					if push(dir):
						conseguiu = True
						break
				if not conseguiu:
					movimentacao.goto(x_mistura, y_mistura)
				else:
					move(East)
					push(West)
					move(West)
					x_mistura, y_mistura = get_pos_x(), get_pos_y()
					visitados.add((get_pos_x(), get_pos_y()))
					continue
		########################################################################			
		move(West)
		necessario_reposicao_anterior = get_pos_z() == camada_corrente
		move(North)
		conseguiu = False
			
		for dir in direcoes_cardeais:
			if push(dir):
				conseguiu = True
				break
		if conseguiu and necessario_reposicao_anterior:
			move(South)
			push(North)
		movimentacao.goto(x_mistura, y_mistura)
			
achar_caminho_ate_alvo(15, 16, 16, 16)			