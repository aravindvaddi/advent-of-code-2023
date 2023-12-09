from collections import Counter, defaultdict
from itertools import count
from pprint import pprint

hand_bounty = {}
hand_type = defaultdict(list)
rank = 1
total = 0
l2h = ['hc', '1p', '2p', '3k', 'fh', '4k', '5k']



def get_hand_type(hand):
    counts = Counter(hand)
    # print(counts)
    if (5 in counts.values()) or (4 in counts.values() and counts['J'] == 1) or (3 in counts.values() and counts['J'] == 2) or (2 in counts.values() and counts['J'] == 3) or (1 in counts.values() and counts['J'] == 4):
        return '5k'
    if (4 in counts.values() and counts['J'] == 0) or (counts['J'] == 1 and 3 in counts.values()) or (counts['J'] == 2 and list(counts.values()).count(2) == 2) or (counts['J'] == 3 and 1 in counts.values()):
        return '4k'
    if (3 in counts.values() and 2 in counts.values() and counts['J'] == 0) or (list(counts.values()).count(2) == 2 and counts['J'] == 1):
        return 'fh'
    if (list(counts.values()).count(1) == 3 and counts['J'] == 2) or (3 in counts.values() and counts['J'] == 0) or (2 in counts.values() and counts['J'] == 1 and list(counts.values()).count(1) == 3):
        return '3k'
    if list(counts.values()).count(2) == 2 and counts['J'] == 0:
        return '2p'
    if (2 in counts.values() and counts['J'] == 0 and list(counts.values()).count(1) == 3) or (counts['J'] == 1 and list(counts.values()).count(1) == 5):
        return '1p'
    return 'hc'

def convert(hand):
    result = []
    for card in hand:
        if card.isdigit():
            result.append(int(card))
        elif card == 'T':
            result.append(10)
        elif card == 'J': 
            result.append(1)
        elif card == 'Q':
            result.append(12)
        elif card == 'K':
            result.append(13)
        elif card == 'A':
            result.append(14)
    return result

with open('input7.txt', 'r') as f:
    lines = 0
    for line in f:
        line = line.strip()
        hand, bounty = line.split(' ')
        type = get_hand_type(hand)
        hand_type[type].append(hand)
        hand_bounty[hand] = int(bounty)
        lines += 1
    # print(lines)
    lens = 0

    for t in hand_type.keys():
        print(t, hand_type[t])
        print()
    # print("hand_type", hand_type)#, "hand_bounty", hand_bounty)
    for type in l2h:
        sorted_hands = sorted(hand_type[type], key=convert, reverse=False)
        # print(lens, sorted_hands)
        lens += len(sorted_hands)  
        for hand in sorted_hands:
            total += hand_bounty[hand] * rank
            rank += 1

# print(lens)
print(total)
# 249240039 too high

# 249197028

# 249278839 

# 248726833 X

# 248740565 too low

# 248740565

# 249138943 ✅