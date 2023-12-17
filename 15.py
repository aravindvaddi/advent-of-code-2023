from matplotlib import lines

total = 0

def hasher(string):
    val = 0
    for char in string:
        # print(char, val)
        if val == '\n':
            continue
        val += ord(char)
        val *= 17
        val %= 256
    return val


with open('input15.txt', 'r') as file:
    lines = file.readlines()
    # print(len(lines))

    for line in lines:
        seqs = line.strip().split(',')
        for seq in seqs:
            val = hasher(seq)
            # print(val)
            total += val

print(total)

# print(hasher('HASH'))