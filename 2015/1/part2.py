
with open("input.txt", "r") as f:
	number = 0
	index = 0
	text = str(f.read())
	for char in text:
		if char == ')':
			number -= 1
		elif char == '(':
			number += 1
		else:
			print("ERROR!")
		index+= 1

		if number <= -1:
			print(index)
			break
		