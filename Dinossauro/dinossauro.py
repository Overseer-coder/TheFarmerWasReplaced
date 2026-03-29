horizontal = [West, East]
fator = [2, 1]

def iniciar():
	clear()
	hamiltonian_cycle()

def hamiltonian_cycle():
	change_hat(Hats.Dinosaur_Hat)
	dir = North
	indice_fator = 1
	while True:
		while move(North):
			pass
		
		while get_pos_x() != 0 or get_pos_y() != 0:	
			for _ in range(get_world_size() - fator[indice_fator % 2]):
				move(horizontal[indice_fator % 2])
			move(South)
			indice_fator += 1
	#change_hat(Hats.Brown_Hat)
			
iniciar()