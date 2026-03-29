horizontal = [West, East]
vertical = [South, North]

def ordenar_horizontal():
	fator = 0
	while True:
		ordenados = True
		for _ in range(get_world_size() - 1):
			if get_pos_x() != 0 and measure() < measure(West):
				swap(West)
				
				if measure() > measure(East):
					swap(East)
				
				if measure() < measure(West):
					swap(West)
				
				ordenados = False
			move(horizontal[fator % 2])
		fator += 1
		if ordenados:
			break	
		
def ordenar_vertical():
	fator = 0
	while True:
		ordenados = True
		for _ in range(get_world_size() - 1):
			if get_pos_y() != 0 and measure() < measure(South):
				swap(South)
				
				if measure() > measure(North):
					swap(North)
					
				if measure() < measure(South):
					swap(South)
					
				ordenados = False
			move(vertical[fator % 2])
		fator += 1
		if ordenados:
			break
		