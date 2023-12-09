result = 1

def parse_input(line):
	return int(line.split(':')[1].replace(' ', '').strip())

def process(time, distance):
	valid_options = 0
	for i in range(time + 1):
		d = (time * i) - i**2
		if d > distance:
			valid_options += 1
	return valid_options

with open('input6.txt', 'r') as f:
	time = parse_input(f.readline().strip())
	distance = parse_input(f.readline().strip())

	result = process(time, distance)

print(result if result != 1 else '0')
# 27363861