

# INPUT = 'jchzalrnumimnmhp'

def vowel_check(string):
	vowels = {
		'a' : 0,
		'e' : 0,
		'i' : 0,
		'o' : 0,
		'u' : 0,
	}
	for char in string:
		if char in 'aeiou':
			vowels[char] +=1
	
	number = 0
	for char in 'aeiou':
		number += vowels[char]
	
	return number >= 3

def letter_twice(string):
	for i in range(0,len(string)-1):
		if(string[i]==string[i+1]):
			return True
	return False

def naughty_combination(string):
	comb = ['ab', 'cd', 'pq', 'xy']
	for i in range(len(comb)):
		if comb[i] in string:
			# print(comb[i])
			return False
	return True

def nice_string(string):
	return vowel_check(string) and letter_twice(string) and naughty_combination(string)

# print(vowel_check(INPUT))
# print(letter_twice(INPUT))
# print(naughty_combination(INPUT))

with open("input.txt", "r") as f:
	aux = 0
	for line in f:
		if nice_string(line):
			aux += 1
	print(aux)
	