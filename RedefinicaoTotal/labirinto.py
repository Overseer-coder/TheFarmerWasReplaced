import colher_dependencia

turn_left = {North:West, West:South, South:East, East:North}
turn_right = {North:East, East:South, South:West, West:North}

def left_hand_rule(cost):
	while num_items(Items.Gold) < cost:
		dir = West
		
		while get_entity_type() == Entities.Hedge:
			if can_move(dir):
				move(dir)
				dir = turn_left[dir]
			else:
				dir = turn_right[dir]
		harvest()
		criar_labirinto()

def criar_labirinto():
	plant(Entities.Bush)
	substancia = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	
	while num_items(Items.Weird_Substance) < substancia:
		colher_dependencia.colher(Entities.Treasure, Unlocks.Mazes, 250)
	
	use_item(Items.Weird_Substance, substancia)