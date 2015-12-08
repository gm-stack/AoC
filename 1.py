i = open("input-1.txt").read()

floor = 0
btime = None
for i,c in enumerate(i):
	if c == "(":
		floor += 1
	elif c == ")":
		floor -= 1
		if floor < 0 and not btime:
			btime = i

print btime+1
print floor