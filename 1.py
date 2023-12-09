
s = 0

def get_first_last_digit_num(line):
	i = 0
	j = len(line) - 1

	s = None
	e = None

	while i < len(line) and j >= 0:
		if not s and line[i].isdigit():
			s = line[i]
		if not e and line[j].isdigit():
			e = line[j]

		j -= 1
		i += 1
	return int(f'{s}{e}')

with open("input.txt", "r") as f:
	i = 0
	for l in f:
		print(f"processing line {i}: {l}", end="")
		val = get_first_last_digit_num(l)
		print(f"found code {val}")
		s += val

print(s)	
		
