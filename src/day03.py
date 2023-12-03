def fill_heatmap(x, y, heatmap, value):
    if value == 0:
        if (x, y) not in heatmap:
            heatmap[(x, y)] = value
        return

    for i in range(-1, 2):
        for j in range(-1, 2):
            heatmap[(x + i, y + j)] = value

def get_heatmap(input, get_value_func):
    heatmap = {}
    for y, line in enumerate(input):
        for x, ch in enumerate(line):
            value = get_value_func(ch)
            fill_heatmap(x, y, heatmap, value)
    return heatmap

def solution(input, heatmap):
    numbers = {}
    for y, line in enumerate(input):
        current_digit_list = []
        need_add_to = set()
        for x, ch in enumerate(line):
            if ch.isdigit():
                current_digit_list.append(ch)
                if heatmap[(x, y)] > 0:
                    need_add_to.add(heatmap[(x, y)])
            else:
                if need_add_to:
                    current_number = int(''.join(current_digit_list))
                    for x in need_add_to:
                        if not x in numbers:
                            numbers[x] = [current_number]
                        else:
                            numbers[x].append(current_number)
                current_digit_list = []
                need_add_to = set()
    return numbers

input = open('../inputs/day03.txt', 'r')
lines = input.readlines()

heatmap01 = get_heatmap(lines, lambda ch: 0 if ch.isdigit() or ch in ('.', '\n') else 1)
numbers = solution(lines, heatmap01)
print("Part I:", sum(numbers[1]))

# Part II
current_gear = 1
def star_symbols_func(ch):
    global current_gear
    result = current_gear if ch == '*' else 0
    if result > 0:
        current_gear += 1
    return result

heatmap02 = get_heatmap(lines, star_symbols_func)
adjacent_numbers = solution(lines, heatmap02)

print("Part II:", sum([v[0] * v[1] for v in adjacent_numbers.values() if len(v) == 2]))