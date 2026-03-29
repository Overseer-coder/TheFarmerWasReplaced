def retornar_pos_inicial():
	direita = get_world_size() - get_pos_x()
	baixo = get_pos_y()
	for _ in range(direita):
		move(East)
	for _ in range(baixo):
		move(South)

def goto(x, y):
	x_atual = get_pos_x()
	y_atual = get_pos_y()
	 
	if x_atual > x:
		for _ in range(x_atual - x):
			move(West)
	else:
		for _ in range(abs(x_atual - x)):
			move(East)
			
	if y_atual > y:
		for _ in range(y_atual - y):
			move(South)
	else:
		for _ in range(abs(y_atual - y)):
			move(North)