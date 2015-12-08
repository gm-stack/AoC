i = open("input-5.txt").readlines()

nice = 0

for word in i:
	vowels = sum([a in "aeiou" for a in word])
	doubles = sum([word[i] == word[i+1] for i,c in enumerate(word[:-2])])
	bad = sum([b in word for b in ["ab","cd","pq","xy"]])

	if vowels >= 3 and doubles >= 1 and bad == 0:
		nice += 1

print nice