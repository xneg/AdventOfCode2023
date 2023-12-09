import math
from functools import reduce
from operator import mul

input = [(41, 214), (96, 1789), (88, 1127), (94, 1055)]


def roots(time, distance):
    d = time * time - 4 * distance
    if d > 0:
        return (
            math.floor((time - math.sqrt(d)) / 2) + 1,
            math.ceil((time + math.sqrt(d)) / 2) - 1,
        )
    return None


def solution(races):
    return reduce(
        mul,
        [
            end - start + 1
            for start, end in [roots(time, distance) for time, distance in races]
        ],
    )


print(solution(input))
print(solution([tuple([int("".join(map(str, tup))) for tup in zip(*input)])]))
