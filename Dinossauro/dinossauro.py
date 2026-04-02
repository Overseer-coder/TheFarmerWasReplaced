horizontal = [West, East]

def iniciar(ossos):
	while num_items(Items.Bone) < ossos:
		clear()
		hamiltonian_cycle()

def hamiltonian_cycle():
	change_hat(Hats.Dinosaur_Hat)
	hat = Hats.Dinosaur_Hat
	dir = North
	while hat == Hats.Dinosaur_Hat:
		indice_fator = 1
		while move(North):
			pass

		if not move(East) or (get_pos_x() != 0 and get_pos_y() != (get_world_size() - 1)):
			change_hat(Hats.Brown_Hat)
			hat = Hats.Brown_Hat
			
		while hat == Hats.Dinosaur_Hat:	
			for _ in range(get_world_size() - 2):
				if not move(horizontal[indice_fator % 2]):
					change_hat(Hats.Brown_Hat)
					hat = Hats.Brown_Hat
			if not move(South):
				if get_pos_x() == 1 and get_pos_y() == 0:
					break
				change_hat(Hats.Brown_Hat)
				hat = Hats.Brown_Hat
			indice_fator += 1
			
		if not move(West):
			change_hat(Hats.Brown_Hat)
			hat = Hats.Brown_Hat
		
iniciar(10000000)