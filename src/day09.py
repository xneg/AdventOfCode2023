def get_next_seq(seq):
    sum = 0
    result = []
    for x, y in zip(seq, seq[1:]):
        result.append(y - x)
        sum += (y - x)
    return sum == 0, result

def find_prediction(seq):
    last_number = seq[-1]
    is_zero, seq = get_next_seq(seq)
    while not is_zero:
        last_number += seq[-1]
        # print(seq)
        # last_numbers.append(seq[-1])
        is_zero, seq = get_next_seq(seq)
    return last_number

input = (open('../inputs/day09.txt', 'r')
         .read()
         .splitlines())

result = 0
count = 0
results = []
for line in input:
    current_result = find_prediction([int(x) for x in line.split(sep = ' ')])
    result += current_result
    count += 1
    results.append((current_result, line))
for a, b in sorted(results):
    print(a, b)
print(count, result)