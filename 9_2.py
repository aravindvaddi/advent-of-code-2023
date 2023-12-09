answer = 0

def parse(input):
    nums = [int(val.strip()) for val in input.split(' ') if val.strip()]
    return nums

def process(input):
    i = 0
    while len(set(input[i:])) != 1 and i < len(input):
        for j in range(len(input) - 1, i, -1):
            input[j] = input[j] - input[j - 1]
        print('ouput',input)
        i += 1

    sum = 0
    for k in range(0, i + 1):
        if k % 2 == 0:
            sum += input[k]
        else: 
            sum -= input[k]
        print('sum, k',sum, k)
    return sum


with open('input9.txt', 'r') as f:
    for line in f:
        input = parse(line.strip())
        print('input', input)
        result = process(input)
        print('result', result)
        answer += result

print(answer)