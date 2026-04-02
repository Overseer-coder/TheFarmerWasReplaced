import colher_dependencia

def plant_sunflower(power):
	clear()
	movimentos = [North, South]
	while num_items(Items.Power) < power:
		
		colher_dependencia.colher(Entities.Sunflower, Unlocks.Sunflowers, 1)
		
		for i in range(get_world_size()):
			for _ in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
				move(movimentos[i % 2])
			move(East)