
coord1 = (0,0)
coord2 = (0,0)
coords = [(0,0)]

def checkExisting(coord):
	if coord not in coords:
		coords.append(coord)
		return True
	
	return False

with open("input.txt", "r") as f:
	text = f.read()
	number = 1
	index = 1
	for char in text:
		if index%2 == 1:
			if char == '^':
				x = coord1[0] + 1
				y = coord1[1]
				coord1 = (x,y)
				if checkExisting(coord1):
					number+=1
			elif char == 'v':
				x = coord1[0] - 1
				y = coord1[1]
				coord1 = (x,y)
				if checkExisting(coord1):
					number+=1
			elif char == '>':
				x = coord1[0]
				y = coord1[1] + 1
				coord1 = (x,y)
				if checkExisting(coord1):
					number+=1
			elif char == '<':
				x = coord1[0]
				y = coord1[1] - 1
				coord1 = (x,y)
				if checkExisting(coord1):
					number+=1
			else: print("ERROR")
		elif index%2 == 0:
			if char == '^':
				x = coord2[0] + 1
				y = coord2[1]
				coord2 = (x,y)
				if checkExisting(coord2):
					number+=1
			elif char == 'v':
				x = coord2[0] - 1
				y = coord2[1]
				coord2 = (x,y)
				if checkExisting(coord2):
					number+=1
			elif char == '>':
				x = coord2[0]
				y = coord2[1] + 1
				coord2 = (x,y)
				if checkExisting(coord2):
					number+=1
			elif char == '<':
				x = coord2[0]
				y = coord2[1] - 1
				coord2 = (x,y)
				if checkExisting(coord2):
					number+=1
			else: print("ERROR")
		else: print("INDEX ERROR")
		index +=1
	print(number)