import re

galaxies = set()
space = []
answer = 0
with open('input11.txt', 'r') as f:
    for i, line in enumerate(f):
        line = line.strip()
        for m in re.finditer('#', line):
            galaxies.add((i, m.start()))
        space.append(line)

empty_rows = {i for i in range(len(space))}
empty_cols = {i for i in range(len(space[0]))}

print(empty_rows, empty_cols, space, galaxies)

for row, col in galaxies:
    empty_cols.remove(col) if col in empty_cols else None
    empty_rows.remove(row) if row in empty_rows else None

print()
print(empty_rows, empty_cols, space, galaxies)

while galaxies:
    galaxy = galaxies.pop()
    for neighbour in galaxies:
        if galaxy == neighbour:
            continue
        row, col = galaxy
        row_n, col_n = neighbour
        distance = abs(row - row_n) + abs(col - col_n)

        lx = min(row, row_n)
        rx = max(row, row_n)
        ly = min(col, col_n)
        ry = max(col, col_n)

        for row in empty_rows:
            if lx < row < rx:
                distance += 999999

        for col in empty_cols:
            if ly < col < ry:
                distance += 999999
        
        print(galaxy, neighbour, distance)
        answer += distance

print(answer)
# 208663533500 - too low