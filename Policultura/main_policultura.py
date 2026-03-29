import policultura

def criar_policultura():
	clear()
	movimentos = [North, South]
	while True:
		for _ in range(get_world_size() - 1):
			plant(Entities.Tree)
			spawn_drone(policultura.plantar_policultura)
			move(East)
			
		for _ in range(get_world_size() - 1):
			spawn_drone(colher_terreno)
			move(East)
			
def colher_terreno():
	for _ in range(get_world_size() - 1):
		if can_harvest():
			harvest()
		move(North)
		
criar_policultura()