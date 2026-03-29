import movimentacao

def plantar_policultura():
	for _ in range(60):
		entity, (x, y) = get_companion()
		dif_x = get_pos_x() - x
		dif_y = get_pos_y() - y
		dir_horizontal = None
		dir_vertical = None
		
		if dif_x < 0:
			dir_horizontal = East
		elif dif_x > 0:
			dir_horizontal = West
			
		if dif_y < 0:
			dir_vertical = North
		elif dif_y > 0:
			dir_vertical = South
			
		for _ in range(abs(dif_x)):
			move(dir_horizontal)
		for _ in range(abs(dif_y)):
			move(dir_vertical)
			
		plantada = get_entity_type() 

		if get_ground_type() != Grounds.Soil:
			till()
			
		if get_water() < 0.5:
			use_item(Items.Water)

		plant(entity)