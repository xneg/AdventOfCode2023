import re


class Map:
    def binary_search_closest_minimum(list, target):
        left, right = 0, len(list) - 1
        closest_min = 0

        while left <= right:
            mid = (left + right) // 2

            if list[mid] <= target:
                closest_min = max(closest_min, list[mid])
                left = mid + 1
            else:
                right = mid - 1

        return closest_min

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.map = {}

    def add(self, source_value, destination_value, range):
        self.map[source_value] = (destination_value, range)


    def transform(self, source_list):
        result = []
        keys_sorted = sorted(self.map.keys())
        for item in source_list:
            closest_key = Map.binary_search_closest_minimum(keys_sorted, item)
            if closest_key in self.map:
                destination, range = self.map[closest_key]
                if closest_key + range >= item:
                    result.append(item - closest_key + destination)
                else:
                    result.append(item)
            else:
                result.append(item)
        return (self.destination, result)

input = open('../inputs/day05.txt', 'r')
lines = input.readlines()

numbers = re.findall(r'\b\d+\b', lines[0])
seeds = [int(num) for num in numbers]
print(seeds)

maps = {}
current_source = ''
for line in lines[1:]:
    if line == '\n':
        continue
    pattern = re.compile(r'\b(\w+)-to-(\w+) map\b')
    match = pattern.match(line)
    if match:
        current_source = match.group(1)
        destination = match.group(2)
        maps[current_source] = Map(current_source, destination)
    else:
        numbers = line.split(' ')
        maps[current_source].add(int(numbers[1]), int(numbers[0]), int(numbers[2]))

source = 'seed'
source_list = seeds

# print(maps[source].map)
# print(maps[source].transform(source_list))

while(source in maps):
    source, source_list = maps[source].transform(source_list)

print(source_list)
print(min(source_list))
