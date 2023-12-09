
import re


graph = []

def look_to_count(graph, x, number):
	y1, y2 = number
	if y1 - 1 >= 0 and (graph[x][y1 - 1] != '.' and not graph[x][y1 - 1].isdigit()):
		return True
	
	if y2 < len(graph[x]) and (graph[x][y2] != '.' and not graph[x][y2].isdigit()):
		return True

	if x - 1 >= 0:
		for c in graph[x - 1][y1 - 1 if y1 - 1 >= 0 else 0: y2 + 1 if y2 + 1 < len(graph[x - 1]) else len(graph[x - 1])]:
			if c != '.' and not c.isdigit():
				return True
	
	if x + 1 < len(graph):
		print(f"checking {x + 1}, {y1 - 1}, {y2 + 1}")
		for c in graph[x + 1][y1 - 1 if y1 - 1 >= 0 else 0: y2 + 1 if y2 + 1 < len(graph[x + 1]) else len(graph[x + 1])]:
			if c != '.' and not c.isdigit():
				return True

def find_numbers(edge):
	numbers = []
	i = 0
	while i < len(edge):
		if edge[i].isdigit():
			j = i + 1
			while j < len(edge) and edge[j].isdigit():
				j += 1
			numbers.append((i, j))
			i = j
		i += 1
	
	print(numbers)
	return numbers

def process(graph, x, edge):
	total = 0
	numbers = find_numbers(edge)
	for number in numbers:
		print(f"looking to count {number}, {x}")
		if look_to_count(graph, x, number):
			value = int(edge[number[0]:number[1]])
			print(f"found {value}")
			total += value

	return total

with open("input3.txt", "r") as f:
	sum = 0
	for edge in f:
		graph.append(edge.strip())

	for x, edge in enumerate(graph): 
		sum += process(graph, x, edge)
		
	print(sum)
