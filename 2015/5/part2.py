
def is_nice(s: str) -> bool:
	pair_twice = False
	for i in range(len(s) - 1):
		pair = s[i:i+2]
		if pair in s[i+2:]:
			pair_twice = True
			break

	repeat_with_gap = False
	for i in range(len(s) - 2):
		if s[i] == s[i+2]:
			repeat_with_gap = True
			break

	return pair_twice and repeat_with_gap


with open("input.txt", "r") as f:
	aux = 0
	for line in f:
		if is_nice(line):
			aux += 1
	print(aux)
	