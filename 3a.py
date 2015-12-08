from collections import defaultdict

i = open("input-3.txt").read()

x = 0
y = 0

houses = defaultdict(int)
houses[(0,0)] = 1

for c in i[::2]:
	if c == "<": x -= 1
	elif c == ">": x += 1
	elif c == "^": y += 1
	elif c == "v": y -= 1

	houses[(x,y)] += 1

x = 0
y = 0

for c in i[1::2]:
	if c == "<": x -= 1
	elif c == ">": x += 1
	elif c == "^": y += 1
	elif c == "v": y -= 1

	houses[(x,y)] += 1

count = 0
for i in houses.items():
	if i[1] >= 1:
		count += 1

print count