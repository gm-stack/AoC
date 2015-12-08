import re
i = [a.strip() for a in open("input-8.txt").readlines()]

codechars = sum([len(a) for a in i])

decchars = sum([(len(a) + 2 + a.count("\\") + a.count("\"")) for a in i])

for line in i:
	print line

print codechars, decchars, (decchars-codechars)
