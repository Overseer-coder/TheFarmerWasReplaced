import hay_farm
import wood_farm
import carrot_farm
import sunflower_farm
import pumpkin_farm
import cactus_farm
import dinossauro
import labirinto

def desbloquear(desbloqueio):
	
	if num_unlocked(Unlocks.Sunflowers) > 0:
		sunflower_farm.plant_sunflower(num_unlocked(Unlocks.Sunflowers) * 100)
	
	unlock_cost = get_cost(desbloqueio)
	unlock_comprado = False
	while not unlock_comprado:
		for item in unlock_cost:
			if item == Items.Hay:
				hay_farm.plant_hay(unlock_cost[item])

			elif item == Items.Wood:
				if num_unlocked(Unlocks.Trees) > 0:
					wood_farm.plant_tree(unlock_cost[item])
				else:
					wood_farm.plant_bush(unlock_cost[item])

			elif item == Items.Carrot:
				carrot_farm.plant_carrot(unlock_cost[item])

			elif item == Items.Pumpkin:
				pumpkin_farm.plant_pumpkin(unlock_cost[item])

			elif item == Items.Weird_Substance:
				pumpkin_farm.plant_pumpkin(unlock_cost[item])

			elif item == Items.Cactus:
				cactus_farm.plant_cactus(unlock_cost[item])

			elif item == Items.Bone:
				dinossauro.iniciar(unlock_cost[item])
				
			elif item == Items.Gold:
				labirinto.left_hand_rule(unlock_cost[item])
				
		unlock_comprado = unlock(desbloqueio)
	