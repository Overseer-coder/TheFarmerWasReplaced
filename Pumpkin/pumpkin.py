import movimentacao

def plantar_abobora():
	plantar_primeira_vez()

	estragadas = recuperar_aboboras_estragadas()

	for x, y in estragadas:
		movimentacao.goto(x, y)
		while not can_harvest():
			plant(Entities.Pumpkin)
				
def plantar_primeira_vez():
	for _ in range(get_world_size()):
		till()
		plant(Entities.Pumpkin)
		use_item(Items.Water, 2)
		move(North)			

def recuperar_aboboras_estragadas():
	estragadas = []
	for _ in range(get_world_size()):
		if not can_harvest():
			plant(Entities.Pumpkin)
			estragadas.append((get_pos_x(), get_pos_y()))
		move(North)
		
	return estragadas