import hashlib

input = "iwrupvqb"
nonce = 0

while True:
	hash = hashlib.md5(input + str(nonce)).hexdigest()
	if hash.startswith("000000"):
		print nonce
		break
	nonce += 1