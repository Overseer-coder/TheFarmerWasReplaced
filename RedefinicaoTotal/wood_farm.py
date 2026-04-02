def plant_bush(cost):
	clear()
	movimentos = [North, South]
	while num_items(Items.Wood) < cost:
		for i in range(get_world_size()):
			for _ in range(get_world_size()):
				if can_harvest():
					if get_entity_type() == Entities.Bush:
						harvest()
					plant(Entities.Bush)
				move(movimentos[i % 2])
			move(East)
			
def plant_tree(cost):
	clear()
	movimentos = [North, South]
	while num_items(Items.Wood) < cost:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if (j + i) % 2 == 0:
					plant(Entities.Tree)
				move(movimentos[i % 2])
			move(East)