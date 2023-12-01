input = open('../inputs/day01.txt', 'r')
lines = input.readlines()

digits_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def get_number(iterable, line, can_be_word=False):
    result = None
    for i in iterable:
        if line[i].isdigit():
            return int(line[i])
        elif can_be_word:
            for key, value in digits_map.items():
                if key == line[i: i + len(key)]:
                    return value

    return result

def solution(line, can_be_word):
    first_number = get_number(range(len(line)), line, can_be_word)
    second_number = get_number(range(len(line) - 1, -1, -1), line, can_be_word)
    return first_number * 10 + second_number


result = sum([solution(line, False) for line in lines])
print("Part I:", result)

result_2 = sum([solution(line, True) for line in lines])
print("Part II:", result_2)