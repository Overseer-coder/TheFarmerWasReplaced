def plant_hay(cost):
	clear()
	movimentos = [North, South]
	while num_items(Items.Hay) < cost:
		for i in range(get_world_size()):
			for _ in range(get_world_size()):
				if can_harvest():
					harvest()
				move(movimentos[i % 2])
			move(East)