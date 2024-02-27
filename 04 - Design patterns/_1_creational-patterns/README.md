<h2>Conceitos Principais:</h2><br>

<b>Abstract Factory (MazeFactory):</b> Define uma interface para criar famílias de objetos relacionados, como Maze, Wall, Room, e Door.
No código, MazeFactory possui métodos abstratos (make_maze, make_wall, make_room, make_door) que serão implementados por suas subclasses concretas.

<b>Concrete Factories (EnchantedMazeFactory e OrdinaryMazeFactory):</b> Implementam a interface MazeFactory para criar objetos de uma família específica. EnchantedMazeFactory cria objetos relacionados a um labirinto encantado, enquanto OrdinaryMazeFactory cria objetos para um labirinto comum.

<b>Abstract Products (Maze, Wall, Room, Door):</b> São interfaces para os produtos que serão criados pelas fábricas. Cada fábrica concreta implementa essas interfaces.

<b>Concrete Products (EnchantedMaze, OrdinaryMaze, EnchantedRoom, OrdinaryRoom, EnchantedDoor, OrdinaryDoor):</b> São as implementações reais dos objetos que a fábrica cria.
EnchantedMazeFactory cria objetos encantados (EnchantedMaze, EnchantedRoom, EnchantedDoor), enquanto OrdinaryMazeFactory cria objetos comuns (OrdinaryMaze, OrdinaryRoom, OrdinaryDoor).

<b>Cliente (create_maze):</b> Utiliza a fábrica para criar um conjunto completo de objetos relacionados. No exemplo, create_maze cria um labirinto com dois quartos e uma porta entre eles usando a fábrica fornecida como argumento.

<b>Fluxo de Uso:</b>
O cliente decide qual tipo de labirinto deseja criar (encantado ou comum).
O cliente cria uma instância da fábrica correspondente (EnchantedMazeFactory ou OrdinaryMazeFactory).
O cliente utiliza a fábrica para criar os objetos relacionados chamando create_maze(factory).
A fábrica cria os objetos concretos (labirinto, quartos, paredes, portas) de acordo com a família específica.
O cliente recebe o labirinto criado pela fábrica e pode interagir com ele.
Esse exemplo ilustra como o padrão Abstract Factory permite que você encapsule a criação de famílias de objetos relacionados, fornecendo uma interface comum para diferentes implementações desses objetos. Isso facilita a troca entre diferentes conjuntos de objetos sem modificar o código do cliente.