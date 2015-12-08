from collections import defaultdict
i = open("input-6.txt").readlines()

def coord(a):
	x = a.split(",")
	xc = map(int,x)
	return xc

lights = defaultdict(int)

for line in i:
	cmd = line.strip().split(" ")
	if cmd[0] == "turn":
		x1,y1 = coord(cmd[2])
		x2,y2 = coord(cmd[4])
		if cmd[1] == "on":
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					lights[(x,y)] += 1
		elif cmd[1] == "off":
			for x in range(x1,x2+1):
				for y in range(y1,y2+1):
					if lights[(x,y)] > 0:
						lights[(x,y)] -= 1
	elif cmd[0] == "toggle":
		x1,y1 = coord(cmd[1])
		x2,y2 = coord(cmd[3])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				lights[(x,y)] += 2

#print lights

countOn = 0
for i,state in lights.items():
		countOn += state

print countOn
