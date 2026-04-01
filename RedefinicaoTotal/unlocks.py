import hay_farm
import bush_farm
import carrot_farm

def desbloquear(desbloqueio):
	unlock_cost = get_cost(desbloqueio)
	
	for item in unlock_cost:
		if item == Items.Hay:
			hay_farm.plant_hay(unlock_cost[item])
		elif item == Items.Wood:
			bush_farm.plant_bush(unlock_cost[item])
		elif item == Items.Carrot:
			carrot_farm.plant_carrot(unlock_cost[item])
			
	unlock(desbloqueio)
	