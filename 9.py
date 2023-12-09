answer = 0

def parse(input):
    nums = [int(val.strip()) for val in input.split(' ') if val.strip()]
    return nums

def process(input):
    i = len(input) - 1
    while len(set(input[:i + 1])) != 1 and i > 0:
        for j in range(i):
            input[j] = input[j + 1] - input[j]
        i -= 1

    sum = 0
    for k in range(1, len(input) - i + 1):
        sum += input[-k]
    return sum


with open('input9.txt', 'r') as f:
    for line in f:
        input = parse(line.strip())
        result = process(input)
        answer += result

print(answer)