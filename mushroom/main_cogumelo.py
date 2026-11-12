import localizar_cogumelo
import movimentacao
import achar_terreno

clear()		
for _ in range(get_world_size() - 1):
	spawn_drone(achar_terreno.encontrar_limpar_terreno_cogumelo)
	move(East)
achar_terreno.encontrar_limpar_terreno_cogumelo()

while num_drones() > 1:
	pass

movimentacao.goto(get_world_size() / 2, get_world_size() / 2)

dig()
tipo_cogumelo_alvo = measure()
x_alvo, y_alvo = get_pos_x(), get_pos_y()
x_proximo, y_proximo = localizar_cogumelo.localizar_mais_proximo_ao_redor_alvo(x_alvo, y_alvo, tipo_cogumelo_alvo)

movimentacao.goto(x_proximo, y_proximo)

