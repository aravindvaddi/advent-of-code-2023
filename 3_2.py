graph = []
result = 0

def extract_number_reduce_locations(loc, visited, graph):
	x, y = loc
	s = y - 1
	e = y + 1

	while s >= 0:
		if graph[x][s].isdigit():
			visited.add((x, s))
		else:
			break
		s -= 1

	while e < len(graph[x]):
		if graph[x][e].isdigit():
			visited.add((x, e))
		else:
			break
		e += 1

	# print(s + 1, e)

	return int(graph[x][s + 1:e])

def generate_surroundings(x, y):
	return {
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),                   (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    }

def get_numbers(star, graph):
	numbers = []
	visited = set()
	x, y = star
	surroundings = generate_surroundings(x, y)
	# print(surroundings)
	for (x, y) in surroundings:

		if (x, y) not in visited and graph[x][y].isdigit():
			visited.add((x, y))
			# print('checking', x, y)
			number = extract_number_reduce_locations((x, y), visited, graph)
			# print(number)
			numbers.append(number)
	return numbers if len(numbers) == 2 else None

def get_star_locations(graph, edge, x):
	star_locations = []
	for y, _ in enumerate(edge):
		if graph[x][y] == '*':
			star_locations.append((x, y))

	return star_locations

with open('input3.txt', 'r') as f:
	for line in f:
		graph.append(f'.{line.strip()}.')

	graph.insert(0, '.' * (len(line.strip()) + 2))
	graph.append('.' * (len(line.strip()) + 2))


	for x, edge in enumerate(graph):
		stars = get_star_locations(graph, edge, x)
		for star in stars:
			numbers = get_numbers(star, graph)
			if numbers:
				# print(numbers)
				result += numbers[0] * numbers[1]


print(result)
# 72246648