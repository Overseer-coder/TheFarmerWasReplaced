def plantar_cactus():
	for _ in range(get_world_size()):
		till()
		plant(Entities.Cactus)	
		move(North)