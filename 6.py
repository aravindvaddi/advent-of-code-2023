result = 1

def parse_input(line):
	return [int(val.strip()) for val in line.split(':')[1].split(' ') if val.strip()]

def process(time, distance):
	valid_options = 0
	for i in range(time + 1):
		d = (time * i) - i**2
		if d > distance:
			valid_options += 1
	return valid_options

with open('input6.txt', 'r') as f:
	times = parse_input(f.readline().strip())
	distances = parse_input(f.readline().strip())

for time, distance in zip(times, distances):
	result *= process(time, distance)

print(result if result != 1 else '0')
# 771628