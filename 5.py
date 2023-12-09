from gettext import find
from pprint import pp, pprint
import re 

maps = []
seeds = []
result = 100000000000000000000000000000000000000

def find_location(seed, maps, i = 0):
    if i == len(maps):
        return seed
    else:
        start = seed
        for s, (e, r) in maps[i].items():
            print(f"checking {s}, {e}, {r}")
            if start >= s and start < s + r:
                print(f"processing {e + (start - s)}")
                return find_location(e + (start - s), maps, i + 1)
        print(f"processing value {seed}")
        return find_location(seed, maps, i + 1)

with open('input5.txt', 'r') as file:
    line = file.readline()
    seeds = [int(seed.strip()) for seed in line.strip().split(":")[1].strip().split(" ") if seed.strip()]
    while True:
        line = file.readline()
        if not line:
            break
        if line.strip().endswith("map:"):
            map = {}
            while True:
                line = file.readline()
                if line == '\n' or not line:
                    break
                else:
                    
                    vals = [int(val.strip()) for val in line.strip().split(" ") if val.strip()]
                    map[vals[1]] = (vals[0], vals[2])
            maps.append(map)

    pprint(maps)
    pprint(seeds)

    for seed in seeds:
        print(f"processing value {seed}")
        loc = find_location(seed, maps)

        print()
        result = min(result, loc)

    print(result)
    # 806029445