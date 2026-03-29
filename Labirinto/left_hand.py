turn_left = {North:West, West:South, South:East, East:North}
turn_right = {North:East, East:South, South:West, West:North}

def left_hand_rule():
	while get_entity_type() != Entities.Hedge:
		pass
		
	while True:
		dir = West
		
		while get_entity_type() == Entities.Hedge:
			if can_move(dir):
				move(dir)
				dir = turn_left[dir]
			else:
				dir = turn_right[dir]
		harvest()
		recriar_labirinto()

def recriar_labirinto():
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))