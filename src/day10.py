from enum import Enum


class Direction(Enum):
    North = 1
    South = 2
    West = 3
    East = 4

    def opposite(self):
        opposite_mapping = {
            Direction.North: Direction.South,
            Direction.South: Direction.North,
            Direction.West: Direction.East,
            Direction.East: Direction.West,
        }
        return opposite_mapping[self]


symbols_map = {
    "|": (Direction.North, Direction.South),
    "-": (Direction.West, Direction.East),
    "L": (Direction.North, Direction.East),
    "J": (Direction.North, Direction.West),
    "7": (Direction.South, Direction.West),
    "F": (Direction.South, Direction.East),
    ".": None,
}


class Cell:
    def __init__(self, x, y, ends, symbol):
        self.symbol = symbol
        self.coordinates = (x, y)
        self.ends = ends

    move_map = {
        Direction.East: (1, 0),
        Direction.West: (-1, 0),
        Direction.North: (0, -1),
        Direction.South: (0, 1),
    }

    def try_move(self, from_direction: Direction):
        opposite_direction = from_direction.opposite()
        if not self.ends or not opposite_direction in self.ends:
            return False, None
        exit = next((end for end in self.ends if end != opposite_direction), None)
        result = (
            exit,
            tuple(x + y for x, y in zip(self.coordinates, self.move_map[exit])),
        )
        return True, result


class StartCell(Cell):
    def try_move(self, from_direction: Direction):
        next_cell_coordinates = tuple(
            x + y for x, y in zip(self.coordinates, self.move_map[from_direction])
        )
        return True, (
            from_direction,
            next_cell_coordinates,
        )


input = open("../inputs/day10.txt", "r").read().splitlines()

cells = {}
start_cell = None
for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c != "S":
            cells[(x, y)] = Cell(x, y, symbols_map[c], c)
        else:
            start_cell = StartCell(x, y, None, c)
            cells[(x, y)] = start_cell

for dir in (Direction.East, Direction.North, Direction.West, Direction.South):
    current_cell = start_cell
    current_direction = dir
    path_length = 0
    loop = [start_cell.coordinates]

    while True:
        success, result = current_cell.try_move(current_direction)
        if not success:
            path_length = 0
            break
        else:
            path_length += 1
            (current_direction, (x, y)) = result
            loop.append((x, y))
            if not (x, y) in cells:
                path_length = 0
                break
            current_cell = cells[(x, y)]
            if current_cell == start_cell:
                print(dir)
                break

    if path_length != 0:
        print(path_length / 2)
        break

# print(loop)
def point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    if (x, y) in polygon:
        return False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside

def find_points_inside_loop(input, loop):
    inside_points = []

    for i in range(len(input)):
        for j in range(len(input[0])):
            if point_in_polygon(j, i, loop):
                inside_points.append((i, j))

    return inside_points

print(len(find_points_inside_loop(input, loop)))
