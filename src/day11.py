
def manhattan(a, b):
    return abs(b[1] - a[1]) + abs(b[0] - a[0])

input = open("../inputs/day11.txt", "r").read().splitlines()

rows = set()
columns = set()
planets = []
for y, line in enumerate(input):
    for x, c in enumerate(line):
        if c == '#':
            rows.add(y)
            columns.add(x)
            planets.append((x, y))

empty_rows = set(range(len(input))) - rows
empty_columns = set(range(len(input[0]))) - columns

def update_galaxy(initial_planets, empty_rows, empty_columns, shift):
    planets = initial_planets
    for row in reversed(sorted(list(empty_rows))):
        planets = [planet if planet[1] < row else (planet[0], planet[1] + shift - 1) for planet in planets]

    for column in reversed(sorted(list(empty_columns))):
        planets = [planet if planet[0] < column else (planet[0] + shift - 1, planet[1]) for planet in planets]
    return planets

def get_result(planets):
    result = [manhattan(planets[i], planets[j]) for i in range(len(planets)) for j in range(i + 1, len(planets))]
    return sum(result)

print(get_result(update_galaxy(planets, empty_rows, empty_columns, 2)))
print(get_result(update_galaxy(planets, empty_rows, empty_columns, 1000000)))