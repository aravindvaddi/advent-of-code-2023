from math import lcm
import re
from pprint import pprint

paths = {}
aas = []
zzs = []

def parse_and_add(line):
    key, v1, v2 = re.findall(r'[A-Z0-9]{3}', line)
    paths[key] = (v1, v2)
    if key[-1] == 'A':
        aas.append(key)
    if key[-1] == 'Z':
        zzs.append(key)
    
with open('input8.txt') as f:
    pattern = f.readline().strip()
    f.readline()
    for line in f:
        line = line.strip()
        parse_and_add(line)

    pprint(paths)
    pprint(len(paths.keys()))
        
    answer = 1
    t = len(pattern)
    for aa in aas:
        i = 0
        c = aa
        while c[-1] != 'Z':
            n = pattern[i % t]
            c = paths[c][0] if n == 'L' else paths[c][1]
            i += 1
        # print('before',c, n, paths)       
        # print('after ',c, n, paths)       

        answer = lcm(answer, i)
    # 19908 too low
    # 23147

print(answer)