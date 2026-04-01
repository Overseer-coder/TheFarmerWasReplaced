def plant_bush(cost):
	movimentos = [North, South]
	fator = 0
	while num_items(Items.Wood) < cost:
		for i in range(get_world_size()):
			for _ in range(get_world_size()):
				if can_harvest():
					if get_entity_type() == Entities.Bush:
						harvest()
					plant(Entities.Bush)
				move(movimentos[i % 2])
			move(East)