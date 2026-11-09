import movimentacao

visitados = []
direcoes = [North, East, South, West]

def DFS(x_ant, y_ant, x_novo, y_novo):
	
	if (x_novo, y_novo) not in visitados:
		movimentacao.goto(x_novo, y_novo)
		visitados.append((x_novo, y_novo))
		
		if get_entity_type() == Entities.Treasure:
			harvest()
		else:
			for dir in direcoes:
				if not can_move(dir):
					continue
					
				if dir == North:
					DFS(x_novo, y_novo, x_novo, y_novo + 1)
					
				elif dir == East:
					DFS(x_novo, y_novo, x_novo + 1, y_novo)
					
				elif dir == South:
					DFS(x_novo, y_novo, x_novo, y_novo - 1)
					
				elif dir == West:
					DFS(x_novo, y_novo, x_novo - 1, y_novo)
					
			movimentacao.goto(x_ant, y_ant)


clear()
plant(Entities.Bush)
use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))
DFS(0, 0, 0, 0)