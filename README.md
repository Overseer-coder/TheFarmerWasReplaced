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

Exemplo de cactus ordenados por tamanho:           

                1 2 3                                           
                1 2 2                                           
                1 1 1                                           

Exemplo de cactus desordenados:

                3 2 1
                2 1 3
                3 2 2

A implementação deste algoritmo, encontrado na pasta **"Cactus"**, é dividido em 3 partes:

- Cada drone tomará sua coluna de responsabilidade e plantará cactus em toda a sua extensão;
- Após o plantio, os drones serão dispostos em cada linha do grid e ordenarão, horizontalmente, todos os cactus da linha, de forma que  fiquem dispostos em ordem crescente, da direita para a esquerda;
- Por fim, os drones serão dispostos em cada coluna do grid e ordenarão, verticalmente, todos os cactus da coluna, de forma que  fiquem dispostos em ordem crescente, de cima para baixo;

Com isso, as regras para a ordenação dos cactus será satisfeita, e a coleta ordenada será concretizada.

**Labirinto:** O labirinto é um clássico problema de busca. A implementação utilizada foi a "Hand-on-wall rule". O princípio dela é a de sempre estar com uma das mãos "encostada" na parede do labirinto seguir o caminho sem retirá-la. Existem duas variações, a "left-hand rule" e "right-hand rule", onde, respectivamente, a mão esquerda e direita devem estar sempre em contato direto com a parede do labirinto para que ele seja completado.
É uma solução muito simples, não exige armazenamento do caminho ou recursão, basta seguir o caminho inteiro simulando não desgrudar da parede escolhida, assim, todo o labirinto será varrido e o tesouro será encontrado. A implementação do algoritmo encontra-se na pasta **"Labirinto"** e consiste em duas etapas:

- Todos os drones são separados, em pares, por todo o grid, para aumentar a área de atuação de todos eles. Um deles executará o left-hand, e o outro o right-hand;
- Com todos os drones posicionados, o labirinto será criado e a busca dos drone começará. Sempre que qualquer um deles encontrar o tesouro, será coletado e um novo labirinto será criado instantaneamente.

**Dinossauro:** O dinossauro é exatamente igual ao classico Snake. Precisamos coletar uma maça, que irá spawnar aleatoriamente no grid, ao coletá-la a cauda irá aumentar e uma nova maça será spawnada em outro local. A solução deste problema, presente na pasta **"Dinossauro"**, é a criação de um Ciclo Hamiltoniano, onde iremos passar por todas as posições do grid uma única vez e retornar ao início, fechando o ciclo.

Ciclo Hamiltoniano implementado:

                    ↑ → → → → → → 
                    ↑ ← ← ← ← ← ←
                    ↑ → → → → → →
                    ↑ ← ← ← ← ← ←
                    ↑ → → → → → →
              (0,0) ↑ ← ← ← ← ← ←

Como passamos uma única vez por cada posição, é impossível a colisão com a cauda, e a maçã também será sempre coletada eventualmente, pois estrá dentro do caminho do ciclo. Para cada passo, há um verificador de movimento, caso não seja possível mover-se significa que o grid foi inteiramente preenchido, neste caso, a cauda é coletada, gerando ossos, e o processo é reiniciado.

## Redefinição Total

O desafio final de The Farmer Was Replaced são os Leaderboards, listas de jogadores que disputam pelo pódio dos algoritmos mais rápido e eficientes para resolverem determinados desafios propostos pelos desenvolvedores. A "Redefinição Total" é um desafio que consiste na automação total de todos os processos do jogo até a liberação dos Leaderboards novamente, ou seja, o jogo será reiniciado completamente, e o algoritmo deve, de uma única vez, coletar todos os recursos necessários, comprar todas as melhorias pré-requisito, preocupar-se com recursos que dependem de outros, até comprar o **"Unlocks.Leaderboard".**
A solução completa está presente na pasta **"RedefinicaoTotal"** e funciona da seguinte forma:

- **"redefinicao_total.py"** é o arquivo que iniciará o algoritmo, e **"simulacao.py"** simula o mesmo cenário, mas sem colocar seu tempo no leaderboard;
- **"central_desbloqueios.py"** contém todas melhorias, em ordem, necessárias para chegar ao objetivo final. Algumas melhorias extras são adquiridas para diminuir o tempo de execução;
- **"unlocks.py"** faz toda a gestão dos recursos que serão necessários para que o upgrade enviado por parâmetro seja comprado.
- Existem plantas que dependem de outras para serem plantadas, e o **"colher_dependencia.py"** cuida justamente disso. Para cada função, esta será chamada para que os recursos dependentes sejam colhidos antes do desejado.