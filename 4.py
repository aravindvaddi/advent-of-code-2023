total = 0

match_points_map = {i: 2**(i-1) if i > 0 else 0 for i in range(11)}

print(match_points_map)

def extract_nums(nums):
	return { int(num.strip()) for num in nums.split(' ') if num.strip() }

def process_card(card):
	count = 0
	numbers = card.split(':')[1]
	hold = numbers.strip().split('|')
	win = extract_nums(hold[0])
	own = extract_nums(hold[1])
	for val in win:
		if val in own:
			count += 1

	return match_points_map.get(count)

with open("input4.txt") as file:
	for line in file:
		print('processing', line.strip())
		points = process_card(line.strip())
		print(points)
		total += points


print(total)
# 28538