import re


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


def find_intersection_with_remainder(a1, b1, a2, b2):
    # Check if segments overlap
    if b1 < a2 or b2 < a1:
        return None, [(a1, b1)]  # No overlap, return the entire first segment

    # Calculate intersection points
    intersection_start = max(a1, a2)
    intersection_end = min(b1, b2)

    # Calculate non-intersecting parts
    non_intersecting_parts = []
    if a1 < intersection_start:
        non_intersecting_parts.append((a1, intersection_start - 1))
    if b1 > intersection_end:
        non_intersecting_parts.append((intersection_end + 1, b1))

    # Check if intersection is a valid segment
    if intersection_start <= intersection_end:
        intersection = (intersection_start, intersection_end)
    else:
        intersection = None  # No valid intersection

    return intersection, non_intersecting_parts

class Map:

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
        self.map = {}

    def add(self, source_value, destination_value, range):
        self.map[source_value] = (source_value + range - 1, destination_value - source_value)


    def transform(self, source_list):
        result = []
        keys_sorted = sorted(self.map.keys())
        for item in source_list:
            closest_key = binary_search_closest_minimum(keys_sorted, item)
            if closest_key in self.map:
                end, modifier = self.map[closest_key]
                if end >= item:
                    result.append(item + modifier)
                else:
                    result.append(item)
            else:
                result.append(item)
        return (self.destination, result)


    def transform_part_2(self, source_list):
        result = []
        keys_sorted = sorted(self.map.keys())

        def get_result(source_start, source_end):
            result = []
            reminders = []
            start, end = source_start, source_end
            for map_start in keys_sorted:
                map_end, modifier = self.map[map_start]
                intersection, reminders = find_intersection_with_remainder(start, end, map_start, map_end)
                if intersection:
                    result.append((intersection[0] + modifier, intersection[1] + modifier))
                if reminders:
                    if len(reminders) > 1:
                        result.append(reminders[0])
                        start, end = reminders[1]
                    else:
                        start, end = reminders[0]
                else:
                    break
            if reminders:
                result.extend(reminders)
            return result

        for source_start, source_end in source_list:
            result.extend(get_result(source_start, source_end))
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

while(source in maps):
    source, source_list = maps[source].transform(source_list)

print(source_list)
print(min(source_list))

seeds2 = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

source = 'seed'
source_list = seeds2

while(source in maps):
    source, source_list = maps[source].transform_part_2(source_list)

print(source_list)
flat_list = [item for pair in source_list for item in pair]
print(min(sorted(flat_list)))