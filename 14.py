map = []

with open('input14.txt', 'r') as file:
    for line in file:
        line = line.strip()
        map.append(list(line))

current = [len(map) for _ in range(len(map[0]))]

total = 0

print(current)
for x, line in enumerate(map):
    for y, char in enumerate(line):
        if char == 'O':
            total += current[y]
            print('inner',current[y], total)
            current[y] -= 1
        elif char == '#':
            current[y] = len(map) - 1 - x
    print(current)

print(total)