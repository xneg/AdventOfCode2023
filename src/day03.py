def fill_heatmap(x, y, heatmap, value):
    if value == 0:
        if (x, y) not in heatmap:
            heatmap[(x, y)] = value
        return

    for i in range(-1, 2):
        for j in range(-1, 2):
            heatmap[(x + i, y + j)] = value


input = open('../inputs/day03.txt', 'r')
lines = input.readlines()

def get_heatmap(input, get_value_func):
    heatmap = {}
    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            value = get_value_func(ch)
            fill_heatmap(x, y, heatmap, value)
    return heatmap

heatmap01 = get_heatmap(lines, lambda ch: 0 if ch.isdigit() or ch in ('.', '\n') else 1)

numbers = []
for y, line in enumerate(lines):
    current_digit_list = []
    need_add = False
    for x, ch in enumerate(line):
        if ch.isdigit():
            current_digit_list.append(ch)
            if heatmap01[(x, y)] == 1:
                need_add = True
        else:
            if need_add:
                numbers.append(int(''.join(current_digit_list)))
            current_digit_list = []
            need_add = False

print(sum(numbers))
print(numbers)

# Part II
current_gear = 1
def star_symbols_func(ch):
    global current_gear
    result = current_gear if ch == '*' else 0
    if result > 0:
        current_gear += 1
    return result

heatmap02 = get_heatmap(lines, star_symbols_func)

adjacent_digits = {}
for y, line in enumerate(lines):
    current_digit_list = []
    need_add_to = set()
    for x, ch in enumerate(line):
        if ch.isdigit():
            current_digit_list.append(ch)
            if heatmap02[(x, y)] > 0:
                need_add_to.add(heatmap02[(x, y)])
        else:
            if need_add_to:
                current_number = int(''.join(current_digit_list))
                for x in need_add_to:
                    if not x in adjacent_digits:
                        adjacent_digits[x] = [current_number]
                    else:
                        adjacent_digits[x].append(current_number)
                # numbers.append(int(''.join(current_digit_list)))
            current_digit_list = []
            need_add_to = set()

print(adjacent_digits)
print(sum([v[0] * v[1] for v in adjacent_digits.values() if len(v) == 2]))
# print(heatmap)
# print(len(lines[0]))
# print(len(lines))
#
# for j in range(len(lines)):
#     for i in range(len(lines[0])):
#         value = heatmap02[(i, j)] if (i, j) in heatmap02 else 0
#         print(f"{value} ", end='')
#     print('')