import movimentacao
import ordenar_cactus
import cactus

while True:
	clear()
	
	movimentacao.goto(get_world_size() - 1, 0)
	
	for _ in range(get_world_size() - 1):
		spawn_drone(cactus.plantar_cactus)
		move(West)
	
	cactus.plantar_cactus()
	
	while num_drones() > 1:
		pass
		
	movimentacao.goto(get_world_size() - 1, 0)
	
	for _ in range(get_world_size() - 1):
		spawn_drone(ordenar_cactus.ordenar_horizontal)
		move(North)
		
	ordenar_cactus.ordenar_horizontal()
	
	while num_drones() > 1:
		pass
		
	movimentacao.goto(0, get_world_size() - 1)
	
	for _ in range(get_world_size() - 1):
		spawn_drone(ordenar_cactus.ordenar_vertical)
		move(East)
		
	ordenar_cactus.ordenar_vertical()
	
	while num_drones() > 1:
		pass
	
	harvest()