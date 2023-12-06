import math
import re


def get_points(line):
    # card_number_match = re.search(r'(\d+):', line)
    # card_number = card_number_match.group(1)

    numbers_match = re.search(r': (.+?) \| (.+)$', line)
    numbers_before_dash = map(int, numbers_match.group(1).split())
    numbers_after_dash = map(int, numbers_match.group(2).split())

    winning = set(list(numbers_before_dash))
    card_numbers = set(list(numbers_after_dash))

    return len(winning.intersection(card_numbers))

def get_scores(points):
    if points == 0:
        return 0
    return int(math.pow(2, points - 1))

input = open('../inputs/day04.txt', 'r')
lines = input.readlines()

result = sum([get_scores(get_points(line)) for line in lines])
print(result)

# Part ||
result_dict = {}
for i, line in enumerate(lines):
    if i not in result_dict:
        result_dict[i] = 1
    else:
        result_dict[i] += 1
    points = get_points(line)
    for k in range(i + 1, i + points + 1):
        if k not in result_dict:
            result_dict[k] = result_dict[i]
        else:
            result_dict[k] += result_dict[i]

print(sum(list(result_dict.values())))