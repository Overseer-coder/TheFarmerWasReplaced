import colher_dependencia

def plant_pumpkin(cost):
	clear()
	movimentos = [North, South]
	
	while num_items(Items.Pumpkin) < cost:
		while True:
			colher_dependencia.colher(Entities.Pumpkin, Unlocks.Pumpkins, 10)
			todas_crescidas = True
			
			for i in range(get_world_size() - 1):
				for _ in range(get_world_size() - 1):
					if get_ground_type() == Grounds.Grassland:
						till()
					if get_entity_type() != Entities.Pumpkin:
						harvest()
						plant(Entities.Pumpkin)
						if num_unlocked(Unlocks.Fertilizer) > 0:
							use_item(Items.Fertilizer)
						todas_crescidas = False
					move(movimentos[i % 2])
				move(East)
			if (todas_crescidas):
				break
		harvest()