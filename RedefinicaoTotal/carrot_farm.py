def plant_carrot(cost):
	movimentos = [North, South]
	fator = 0
	while num_items(Items.Wood) < cost:
		for i in range(get_world_size()):
			for _ in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest():
					if get_entity_type() == Entities.Carrot:
						harvest()
					plant(Entities.Carrot)
				move(movimentos[i % 2])
			move(East)