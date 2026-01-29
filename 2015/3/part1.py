
coord = (0,0)
coords = [(0,0)]

def checkExisting():
	if coord not in coords:
		coords.append(coord)
		return True
	
	return False

with open("input.txt", "r") as f:
	text = f.read()
	number = 1
	for char in text:
		if char == '^':
			x = coord[0] + 1
			y = coord[1]
			coord = (x,y)
			if checkExisting():
				number+=1
		elif char == 'v':
			x = coord[0] - 1
			y = coord[1]
			coord = (x,y)
			if checkExisting():
				number+=1
		elif char == '>':
			x = coord[0]
			y = coord[1] + 1
			coord = (x,y)
			if checkExisting():
				number+=1
		elif char == '<':
			x = coord[0]
			y = coord[1] - 1
			coord = (x,y)
			if checkExisting():
				number+=1
		else: print("ERROR")
	print(number)