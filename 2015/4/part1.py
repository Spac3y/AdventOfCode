import time
import hashlib

INPUT = 'bgvyzdsv'

append = 0

def check(input):
	res = hashlib.md5(bytes(input, 'utf-8'))
	hex = res.hexdigest()
	for i in range(0,5):
		if hex[i].isdigit():
			if int(hex[i]) != 0:
				return False
		else: return False
	return True

while True:
	# stop = 610000
	append += 1
	
	temp = INPUT + str(append)

	print(f"{temp}")

	if check(temp):
		print(append)
		break
	# time.sleep(0.2)
