import math
import re
from typing import Dict


class Node:
    def __init__(self, value, left, right, nodes: Dict[str, "Node"]):
        self.value = value
        self.left = left
        self.right = right
        self.nodes = nodes

    def move(self, direction) -> "Node":
        return self.nodes[self.left] if direction == 'L' else self.nodes[self.right]


input = (open('../inputs/day08.txt', 'r')
         .read()
         .splitlines())

instructions = input[0]

nodes = {}
pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')

for line in input[2:]:
    match = pattern.search(line)
    node_name = match.group(1)
    left = match.group(2)
    right = match.group(3)
    nodes[node_name] = Node(node_name, left, right, nodes)

# Part I
current_node = nodes["AAA"]
iterations = 0
while current_node.value != "ZZZ":
    if current_node.value == "MCA":
        print('WTF?!')
    direction = instructions[iterations % len(instructions)]
    current_node = current_node.move(direction)
    iterations += 1

print(iterations)

# Part II
current_nodes = [v for v in nodes.values() if v.value.endswith('A')]

nodes_iterations = []
for current_node in current_nodes:
    node_iterations = 0
    print(current_node.value)
    while not current_node.value.endswith("Z"):
        direction = instructions[node_iterations % len(instructions)]
        current_node = current_node.move(direction)
        node_iterations += 1
    nodes_iterations.append(node_iterations)

def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = abs(result * num) // math.gcd(result, num)

    return result


print(nodes_iterations)
print(lcm_of_list(nodes_iterations))
