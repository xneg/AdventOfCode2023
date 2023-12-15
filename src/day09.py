def get_next_seq(seq):
    result = [y - x for x, y in zip(seq, seq[1:])]
    return len(set(seq)) == 1, result

def find_prediction(seq):
    last_number = seq[-1]
    is_zero, seq = get_next_seq(seq)
    while not is_zero:
        last_number += seq[-1]
        is_zero, seq = get_next_seq(seq)
    return last_number

def find_predictions(seq):
    first_number = seq[0]
    last_number = seq[-1]
    print(seq)
    i = 0
    is_zero, seq = get_next_seq(seq)
    while not is_zero:
        print(seq)
        i += 1
        last_number += seq[-1]
        first_number += seq[0] if i % 2 == 0 else -seq[0]
        is_zero, seq = get_next_seq(seq)
    print(first_number, last_number)
    return first_number, last_number

input = (open('../inputs/day09.txt', 'r')
         .read()
         .splitlines())

result_1 = 0
result_2 = 0
for line in input:
    current_result = find_predictions([int(x) for x in line.split(sep = ' ')])
    result_1 += current_result[1]
    result_2 += current_result[0]

print(result_1, result_2)