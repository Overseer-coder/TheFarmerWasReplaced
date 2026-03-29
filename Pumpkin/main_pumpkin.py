import pumpkin

while True:
	clear()
	
	for _ in range(get_world_size() - 1):
		spawn_drone(pumpkin.plantar_abobora)
		move(East)
	
	pumpkin.plantar_abobora()
	
	while num_drones() > 1:
		pass
		
	harvest()