# TheFarmerWasReplaced
The Farmer Was Replaced é um idle game de programação onde automatizamos drones para gerenciarem uma fazenda. O jogo utiliza, como base, uma versão simplificada do Python e com funções extras necessárias para a progreção.

## Multi Drones
O jogo possui um aspecto super interessante com multi threading. Há um desbloqueio específico **"Unlocks.Megafarm"** em que recebemos drones extras para realizarem funções delegadas aos mesmos. Ao utilizar o comando **"spawn_drone(funcao)"**, um drone será spawnado e realizará a função **"funcao"** até o final antes de desparecer. O principal desafio da utilização dos drone é arquitetar o trabalho conjunto de todos eles, e para fazer isso cada drone será responsável por apenas uma única coluna do grid.

## Implementações
**Plantar:** O algoritmo genérico **"plantar"**, implementado em **Plantar/plantar.py**, centraliza o plantio de itens baseados em parâmetros recebidos: **"entities"** e **"fator"**. Entities é uma lista de produtos que deverão ser plantados, até no máximo 2. Para que um mesmo produto seja plantado, apenas utilize uma lista com entidade iguais. Fator é uma variável de controle para que sejam plantados produtos de forma alternada, que é um fator determinante para as **"Trees"**, que crescem mais devagar caso haja outras trees próximas nas posições cardeais.

**Abóboras:** Ao plantar abóboras, formando um quadrado NxN, elas se juntarão e formarão uma abóbora maior, rendendo muito mais material.Porém, há uma chance de que uma abóbora estrague durante seu período de crescimento, e esta não irá formar a abóbora maior, sendo necessário substituí-la. A implementação deste algoritmo, encontrado na pasta **"Pumpkin"**, é dividido em 3 partes:

- Cada drone tomará sua coluna de responsabilidade e plantará abóboras em toda a sua extensão;
- Após o plantio, o drone irá percorrer toda a coluna verificando a existência de abóboras estragadas. Caso haja, a posição dela será adicionada em uma lista;
- Por fim, o drone irá para cada posição de abóboras estragadas e plantará novas até que elas cresçam em sua totalidade.

**Cactus:** Cactus ordenados, ao serem coletados, gerarão uma reação em cadeia, coletando todos os cactus de uma só vez e gerando uma quantidade exponencial de material. Para que os cactus sejam considerados ordenados, duas regras devem ser seguidas: tomando um cacto como referência, todo os cactus ao norte e leste devem ser maiores ou iguais a ele, em tamanho, e todos os cactus a oeste e sul devem ser menores ou iguais.

Exemplo de cactus ordenados por tamanho:           Exemplo de cactus desordenados:

                1 2 3                                           3 2 1
                1 2 2                                           1 3 2
                1 1 1                                           1 2 3

A implementação deste algoritmo, encontrado na pasta **"Cactus"**, é dividido em 3 partes:

- Cada drone tomará sua coluna de responsabilidade e plantará cactus em toda a sua extensão;
- Após o plantio, os drones serão dispostos em cada linha do grid e ordenarão, horizontalmente, todos os cactus da linha, de forma que  fiquem dispostos em ordem crescente, da direita para a esquerda;
- Por fim, os drones serão dispostos em cada coluna do grid e ordenarão, verticalmente, todos os cactus da coluna, de forma que  fiquem dispostos em ordem crescente, de cima para baixo;

Com isso, as regras para a ordenação dos cactus será satisfeita, e a coleta ordenada será concretizada.
