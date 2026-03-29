def plantar_alternado(entities, fator):
	def inner_function():
		inner_fator = fator
		inner_entities = entities
		while True:
			if get_ground_type() != Grounds.Soil:
				till()
				plant(inner_entities[inner_fator % 2])
				inner_fator += 1
				
			if get_water() < 0.5:
				use_item(Items.Water)
				use_item(Items.Water)
				
			if can_harvest():
				harvest()
				plant(inner_entities[inner_fator % 2])
				inner_fator += 1
			
			move(North)
	return inner_function

#Método criado para evitar bug com último drone
#por conta do fator passado por parâmetro
def plantar_alternado_sem_parametro_fator(entities):
	fator = 1
	while True:
		if get_ground_type() != Grounds.Soil:
			till()
			plant(entities[fator % 2])
			fator += 1
			
		if get_water() < 0.5:
			use_item(Items.Water)
			use_item(Items.Water)
			
		if can_harvest():
			harvest()
			plant(entities[fator % 2])
			fator += 1
		move(North)