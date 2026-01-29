
# 2*l*w + 2*w*h + 2*h*l

with open("input.txt", "r") as f:
	total_paper = 0
	for line in f:
		current_paper = 0
		h = int(line.split('x')[0])
		w = int(line.split('x')[1])
		l = int(line.split('x')[2])

		min1 = min(h, min(w,l))
		min2 = max(h, max(w,l))
		min2 = h+w+l - min1 - min2
		print(min1,min2)

		current_paper = h*w*l + 2*min1 + 2*min2
		total_paper += current_paper

print(total_paper)