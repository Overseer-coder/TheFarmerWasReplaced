import colher_dependencia

def plant_cactus(cost):
	clear()
	
	while num_items(Items.Cactus) < cost:	
		primeira_plantacao()
		ordenar_cactus()
		
def primeira_plantacao():
	movimentos = [North, South]
	for i in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type() == Grounds.Grassland:
				till()
			if not plant(Entities.Cactus):
				colher_dependencia.colher(Entities.Cactus, Unlocks.Cactus, 100)
			move(movimentos[i % 2])
		move(East)
			
def ordenar_cactus():
	movimentos = [North, South]
	while True:
		ordenados = True
		for i in range(get_world_size() - 1):
			for _ in range(get_world_size() - 1):
				if get_entity_type() == Entities.Cactus:
					if get_pos_x() != 0 and measure() < measure(West):
						swap(West)
						ordenados = False
					if get_pos_y() != 0 and measure() < measure(South):
						swap(South)
						ordenados = False
					if get_pos_y() != (get_world_size() - 1) and measure() > measure(North):
						swap(North)
						ordenados = False
					if get_pos_x() != (get_world_size() - 1) and measure() > measure(East):
						swap(East)
						ordenados = False
				move(movimentos[i % 2])
			move(East)
		if ordenados:
			harvest()
			clear()
			break
	