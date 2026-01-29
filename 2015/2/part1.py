
# 2*l*w + 2*w*h + 2*h*l

with open("input.txt", "r") as f:
	total_paper = 0
	for line in f:
		current_paper = 0
		h = int(line.split('x')[0])
		w = int(line.split('x')[1])
		l = int(line.split('x')[2])
		current_paper = 2*h*l + 2*h*w + 2*w*l
		mini = min(h*w, h*l)
		mini = min(mini, w*l)

		total_paper += current_paper+mini
print(total_paper)