import re
from functools import reduce
from operator import mul

bag = {"red": 12, "green": 13, "blue": 14}

def check_conditon(situation, reality):
    for key, value in situation.items():
        if reality[key] < value:
            return False
    return True

input = open('../inputs/day02.txt', 'r')
lines = input.readlines()

results_1 = []
results_2 = []
for line in lines:
    game_number_match = re.search(r'Game (\d+):', line)
    game_number = int(game_number_match.group(1))
    games = re.split(r';\s*', line)
    # games_list = []
    need_add = True
    possible_dict = {}
    for game in games:
        counts_match = re.findall(r'(\d+) (red|green|blue)', game)
        counts_dict = {color: int(count) for count, color in counts_match}
        for key, value in counts_dict.items():
            if key not in possible_dict:
                possible_dict[key] = value
            elif value > possible_dict[key]:
                possible_dict[key] = value
        if not check_conditon(counts_dict, bag):
            need_add = False
    results_2.append(reduce(mul, possible_dict.values()))
    if need_add:
        results_1.append(game_number)


print(sum(results_1))
print(results_2)
print(sum(results_2))

        # games_list.append(counts_dict)
    # print(games_list)