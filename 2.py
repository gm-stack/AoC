i = open("input-2.txt").readlines()

totalwrap = 0
totalribbon = 0

for line in i:
	x,y,z = map(int,line.split("x"))
	reqd = (2*x*y) + (2*x*z) + (2*y*z)
	extra = min(x*y, x*z, y*z)
	totalwrap += reqd + extra

	lside = max(x,y,z)
	rreq = x*2 + y*2 + z*2 - lside*2
	bow = x*y*z

	totalribbon += rreq + bow

print totalwrap
print totalribbon