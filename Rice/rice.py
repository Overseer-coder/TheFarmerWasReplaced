def plantar_arroz():
	while True:
		for _ in range(get_world_size()):	
			while get_ground_type() != Grounds.Clay and get_entity_type() != Entities.Rice:
				dig()
				
			if get_water() < 0.5:
				use_item(Items.Water, 2) 
				
			plant(Entities.Rice)	
			move(North)
				
		for _ in range(get_world_size()):	
			if (can_harvest()):
				harvest()
			move(North)
		
clear()	
for _ in range(get_world_size() - 1):
	spawn_drone(plantar_arroz)
	move(East)
plantar_arroz()