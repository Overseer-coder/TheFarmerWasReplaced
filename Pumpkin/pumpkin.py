def plantar_abobora():
	direcao = [North, South]
	indice_dir = 0
	while True:
		todas_crescidas = True
		
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Pumpkin)
				
			if get_water() < 0.5:
				use_item(Items.Water)
				use_item(Items.Water)
				
			if not can_harvest():
				plant(Entities.Pumpkin)
				todas_crescidas = False
				
			move(direcao[indice_dir % 2])
		
		indice_dir += 1
		
		if todas_crescidas:
			break
				
			
					
