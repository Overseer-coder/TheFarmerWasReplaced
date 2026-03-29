import plantar

clear()

fator = 0
entities = [Entities.Sunflower, Entities.Sunflower]
for _ in range(get_world_size() - 1):
	spawn_drone(plantar.plantar_alternado(entities, fator))
	fator +=1
	move(East)

plantar.plantar_alternado_sem_parametro_fator(entities)
