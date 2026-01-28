
with open("input.txt", "r") as f:
	number = 0
	text = str(f.read())
	for char in text:
		if char == '(':
			number += 1
		elif char == ')':
			number -= 1
		else:
			print("Error")
	print(number)