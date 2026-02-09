#  ->         \3
# AND = &     \5
# OR = |      \5
# LSHIFT = << \5
# RSHIFT = >> \5
# NOT = ~     \4

instructions = {}
cache = {}

def evaluate(wire):
	if wire.isdigit():
		return int(wire)

	if wire in cache:
		return cache[wire]
	
	expr = instructions[wire]
	print(wire , expr)

	if type(expr) != list:
		value = evaluate(expr)
	elif len(expr) == 2:
		value = ~evaluate(expr[1])
	elif len(expr) == 3 and expr[1] == "AND":
		value = evaluate(expr[0]) & evaluate(expr[2])
	elif len(expr) == 3 and expr[1] == "OR":
		value = evaluate(expr[0]) | evaluate(expr[2])
	elif len(expr) == 3 and expr[1] == "LSHIFT":
		value = evaluate(expr[0]) << evaluate(expr[2])
	elif len(expr) == 3 and expr[1] == "RSHIFT":
		value = evaluate(expr[0]) >> evaluate(expr[2])

	value = value & 0xFFFF
	cache[wire] = value

	return value

def main():
	with open("input.txt", 'r') as f:
		for line in f:
			split = line.split()
			if len(split) == 3:
				instructions[split[2]] = split[0]
			elif len(split) == 4:
				instructions[split[3]] = split[0:2]
			elif len(split) == 5:
				if split[1] == "AND":
					instructions[split[4]] = split[0:3]
				elif split[1] == "OR":
					instructions[split[4]] = split[0:3]
				elif split[1] == "LSHIFT":
					instructions[split[4]] = split[0:3]
				elif split[1] == "RSHIFT":
					instructions[split[4]] = split[0:3]
	print(evaluate("a"))

if __name__ == "__main__":
	main()