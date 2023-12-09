import re
from pprint import pprint

paths = {}

def parse_and_add(line):
    key, v1, v2 = re.findall(r'[A-Z]{3}', line)
    paths[key] = (v1, v2)
    return key
    
with open('input8.txt') as f:
    pattern = f.readline().strip()
    f.readline()
    for line in f:
        line = line.strip()
        parse_and_add(line)

    pprint(paths)
        
    i = 0
    t = len(pattern)
    c = 'AAA'
    while c != 'ZZZ':
        print(i, c) if i % 100 == 0 else None
        n = pattern[i % t]
        # print('before',c, n, paths)       

        c = paths[c][0] if n == 'L' else paths[c][1]
        # print('after ',c, n, paths)       
        i += 1

    print(i)
    # 19908 too low
    # 23147