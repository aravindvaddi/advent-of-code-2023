
s = 0

digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def check_if_valid_digit_exists(line, i):
	if i + 3 < len(line):
		if line[i:i+3] in digit_map:
			return True, digit_map[line[i:i+3]]
	if i + 4 < len(line):
		if line[i:i+4] in digit_map:
			return True, digit_map[line[i:i+4]]
	if i + 5 < len(line):
		if line[i:i+5] in digit_map:
			return True, digit_map[line[i:i+5]]
	return False, None

def get_first_last_digit_num(line):
	i = 0
	j = len(line) - 1

	s = None
	e = None

	while i < len(line) and j >= 0:
		has_valid_digit_s, digit_s = check_if_valid_digit_exists(line, i)
		has_valid_digit_e, digit_e = check_if_valid_digit_exists(line, j)

		if not s and (line[i].isdigit() or has_valid_digit_s):
			s = line[i] if line[i].isdigit() else digit_s
		if not e and (line[j].isdigit() or has_valid_digit_e):
			e = line[j] if line[j].isdigit() else digit_e

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
		
