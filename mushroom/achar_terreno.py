def encontrar_limpar_terreno_cogumelo():
	while get_ground_type() != Grounds.Mushroom:
		dig()
	
	for _ in range(get_world_size()):
		while get_ground_type() != Grounds.Mushroom:
			dig()
		move(North)