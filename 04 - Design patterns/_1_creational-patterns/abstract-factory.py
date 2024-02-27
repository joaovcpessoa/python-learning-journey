# Abstract Factory
class MazeFactory:
    def make_maze(self):
        pass
    
    def make_wall(self):
        pass
    
    def make_room(self, room_number):
        pass
    
    def make_door(self, room1, room2):
        pass

# Concrete Factory 1
class EnchantedMazeFactory(MazeFactory):
    def make_maze(self):
        return EnchantedMaze()
    
    def make_wall(self):
        return Wall()
    
    def make_room(self, room_number):
        return EnchantedRoom(room_number)
    
    def make_door(self, room1, room2):
        return EnchantedDoor(room1, room2)

# Concrete Factory 2
class OrdinaryMazeFactory(MazeFactory):
    def make_maze(self):
        return OrdinaryMaze()
    
    def make_wall(self):
        return Wall()
    
    def make_room(self, room_number):
        return OrdinaryRoom(room_number)
    
    def make_door(self, room1, room2):
        return OrdinaryDoor(room1, room2)

# Abstract Product
class Maze:
    pass

class Wall:
    pass

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.sides = {}

    def set_side(self, direction, wall):
        self.sides[direction] = wall

class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2
        self.is_open = False

# Concrete Products
class EnchantedMaze(Maze):
    pass

class OrdinaryMaze(Maze):
    pass

class EnchantedRoom(Room):
    pass

class OrdinaryRoom(Room):
    pass

class EnchantedDoor(Door):
    pass

class OrdinaryDoor(Door):
    pass

# Client Code
def create_maze(factory):
    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    door = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side("North", factory.make_wall())
    room1.set_side("East", door)
    room1.set_side("South", factory.make_wall())
    room1.set_side("West", factory.make_wall())

    room2.set_side("North", factory.make_wall())
    room2.set_side("East", factory.make_wall())
    room2.set_side("South", factory.make_wall())
    room2.set_side("West", door)

    return maze

# Exemplo de uso com a Concrete Factory EnchantedMazeFactory
enchanted_factory = EnchantedMazeFactory()
enchanted_maze = create_maze(enchanted_factory)

# Exemplo de uso com a Concrete Factory OrdinaryMazeFactory
ordinary_factory = OrdinaryMazeFactory()
ordinary_maze = create_maze(ordinary_factory)
