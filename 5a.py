i = open("input-5.txt").readlines()

nice = 0

def pair(word):
	wbit = [word[i:i+2] for i,c in enumerate(word[:-1])]
	for i,w in enumerate(wbit):
		if w in wbit[i+2:]:
			return True
	return False

def lxl(word):
	wbit = [word[i:i+3] for i,c in enumerate(word[:-2])]
	for w in wbit:
		if w[0] == w[2]:
			return True
	return False

for word in i:
	if pair(word) and lxl(word):
		nice += 1

print nice