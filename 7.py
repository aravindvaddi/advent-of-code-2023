from collections import Counter, defaultdict
from pprint import pprint

hand_bounty = {}
hand_type = defaultdict(list)
rank = 1
total = 0
l2h = ['hc', '1p', '2p', '3k', 'fh', '4k', '5k']



def get_hand_type(hand):
    counts = Counter(hand)
    if 5 in counts.values():
        return '5k'
    if 4 in counts.values():
        return '4k'
    if 3 in counts.values() and 2 in counts.values():
        return 'fh'
    if 3 in counts.values():
        return '3k'
    if list(counts.values()).count(2) == 2:
        return '2p'
    if 2 in counts.values():
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
            result.append(11)
        elif card == 'Q':
            result.append(12)
        elif card == 'K':
            result.append(13)
        elif card == 'A':
            result.append(14)
    return result

with open('input7.txt', 'r') as f:
    for line in f:
        line = line.strip()
        hand, bounty = line.split(' ')
        type = get_hand_type(hand)
        hand_type[type].append(hand)
        hand_bounty[hand] = int(bounty)

    # print(hand_type, hand_bounty)
    for type in l2h:
        sorted_hands = sorted(hand_type[type], key=convert, reverse=False)
        # print(sorted_hands)
        for hand in sorted_hands:
            total += hand_bounty[hand] * rank
            rank += 1

print(total)

