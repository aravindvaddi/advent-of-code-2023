from collections import defaultdict

total = 0
cards = defaultdict(int)

def extract_nums(nums):
	return { int(num.strip()) for num in nums.split(' ') if num.strip() }

def parse_input(card):
	t = card.split(':')
	card_no = int(t[0].split(' ')[-1].strip())
	lotto_nums = t[1].strip().split('|')
	win = extract_nums(lotto_nums[0])
	own = extract_nums(lotto_nums[1])
	return card_no, win, own 

def update_cards(card_no, count):
	for i in range(0, count):
		cards[card_no + i + 1] += cards[card_no]

def process_card(card):
	count = 0
	card_no, win, own = parse_input(card)	
	cards[card_no] += 1
	for val in win:
		if val in own:
			count += 1

	update_cards(card_no, count)

with open("input4.txt") as file:
	for line in file:
		# print('processing', line.strip())
		process_card(line.strip())
		# print(cards)


total = sum(cards.values())
print(total)
# 9425061