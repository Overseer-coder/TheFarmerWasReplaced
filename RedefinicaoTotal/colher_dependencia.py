import hay_farm
import wood_farm
import carrot_farm
import pumpkin_farm
import cactus_farm

def colher(entity, desbloqueio, extra):
	change_hat(Hats.Brown_Hat)
	cost = get_cost(entity)
	for item in cost:
		if item == Items.Hay and num_items(Items.Hay) < cost[item]:
			hay_farm.plant_hay(num_unlocked(desbloqueio) * 100 * extra)
			
		elif item == Items.Wood and num_items(Items.Wood) < cost[item]:
			if num_unlocked(Unlocks.Trees) > 0:
				wood_farm.plant_tree(num_unlocked(desbloqueio) * 100 * extra)
			else:
				wood_farm.plant_bush(num_unlocked(desbloqueio) * 100 * extra)
				
		elif item == Items.Carrot and num_items(Items.Carrot) < cost[item]:
			carrot_farm.plant_carrot(num_unlocked(desbloqueio) * 100 * extra)
			
		elif item == Items.Pumpkin and num_items(Items.Pumpkin) < cost[item]:
			pumpkin_farm.plant_pumpkin(num_unlocked(desbloqueio) * 100 * extra)
			
		elif item == Items.Cactus and num_items(Items.Cactus) < cost[item]:
			cactus_farm.plant_cactus(num_unlocked(desbloqueio) * 100 * extra)
			
		elif item == Items.Bone and num_items(Items.Bone) < cost[item]:
			cactus_farm.plant_cactus(num_unlocked(desbloqueio) * 100 * extra)
			
		elif item == Items.Weird_Substance:
			pumpkin_farm.plant_pumpkin(num_unlocked(desbloqueio) * 100 * extra)
