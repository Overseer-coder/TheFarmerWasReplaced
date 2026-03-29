import left_hand
import right_hand
import movimentacao

clear()

movimentos = [
			  (0, get_world_size() / 3),
			  (0, get_world_size() / 2),
			  (0, get_world_size() - 1),
			  (get_world_size() / 3, get_world_size() -1),
			  (get_world_size() / 2, get_world_size() -1),
			  (get_world_size() - 1, get_world_size() - 1),
			  (get_world_size() - 1, get_world_size() / 2),
			  (get_world_size() - 1, get_world_size() / 3),
			  (get_world_size() - 1, 0),
			  (get_world_size() / 3, 0),
			  (get_world_size() / 2, 0),
			  (get_world_size() / 2, get_world_size() / 2),
			  (get_world_size() / 2 - 2, get_world_size() / 2),
			  (get_world_size() / 2, get_world_size() / 2 - 2),
			  (get_world_size() / 2 - 2, get_world_size() / 2 - 2)
			 ]

for x, y in movimentos:
	spawn_drone(left_hand.left_hand_rule)
	spawn_drone(right_hand.right_hand_rule)
	movimentacao.goto(x, y)

plant(Entities.Bush)
use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))
