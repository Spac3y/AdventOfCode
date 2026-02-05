
number = 0

matrix = [[0 for _ in range(1000)] for _ in range(1000)]

def turn(start,end, param):
	startX = int(start.split(",")[0])
	startY = int(start.split(",")[1])
	endX = int(end.split(",")[0])
	endY = int(end.split(",")[1])

	for i in range(startX, endX+1):
		for j in range(startY, endY+1):
			if param == 1:
				matrix[i][j] += 1
			else:
				if matrix[i][j] == 0:
					matrix[i][j] = 0
				else:
					matrix[i][j] -= 1

with open("input.txt") as f:
	for line in f:
		command = line.split()[0]

		if command == 'turn':
			param = line.split()[1]
			start = line.split()[2]
			end = line.split()[4]

			if param == 'on':
				turn(start, end, 1)

			elif param == 'off':
				turn(start,end, 0)

			else: print("ERROR TOGGLE")

		elif command == 'toggle':
			start = line.split()[1]
			end = line.split()[3]

			startX = int(start.split(",")[0])
			startY = int(start.split(",")[1])

			endX = int(end.split(",")[0])
			endY = int(end.split(",")[1])

			for i in range(startX, endX+1):
				for j in range(startY, endY+1):
					matrix[i][j] += 2

		else: print("ERROR COMMAND")

	for i in range(1000):
		for j in range(1000):
			number += matrix[i][j]
	print(number)
