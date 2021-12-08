with open('input') as f:
    read_data = f.read().splitlines()
data = [x.split('|') for x in read_data]
digits = [
	[1, 1, 1, 0, 1, 1, 1], # 0
	[0, 0, 1, 0, 0, 1, 0], # 1
	[1, 0, 1, 1, 1, 0, 1], # 2
	[1, 0, 1, 1, 0, 1, 1], # 3
	[0, 1, 1, 1, 0, 1, 0], # 4
	[1, 1, 0, 1, 0, 1, 1], # 5
	[1, 1, 0, 1, 1, 1, 1], # 6
	[1, 0, 1, 0, 0, 1, 0], # 7
	[1, 1, 1, 1, 1, 1, 1], # 8
	[1, 1, 1, 1, 0, 1, 1], # 9
]

s = []
for x in data:
	inputArr = x[0].split()
	output = x[1].split()
	order = [[] for i in range(10)]
	finalOrder = [0 for i in range(7)]
	letterCount = [sum([i.count(k) for i in inputArr]) for k in "abcdefg"]
	l = "abcdefg"
	# Guess the sixtth -- highest count
	finalOrder[5] = l[letterCount.index(max(letterCount))]
	minIndex = letterCount.index(min(letterCount))
	# Guess the fifth -- lowest count
	finalOrder[4] = l[letterCount.index(min(letterCount))]
	letterCount[minIndex] = 10
	# guess the second -- second lowest count
	finalOrder[1] = l[letterCount.index(min(letterCount))]
	for i in inputArr:
		if len(i) == 2:
			order[2] = i
			# guess the third -- two choice one already taken
			finalOrder[2] = i[0] if i[0] != finalOrder[5] else i[1]
		if len(i) == 3:
			order[7] = i
		if len(i) == 4:
			order[4] = i
	# Guess the first -- 3 elements and two of them are the number 3 so the last one is the top bar
	finalOrder[0] = [i for i in order[7] if i not in order[2]][0]
	for i in order[4]:
		if i not in finalOrder:
			# guess middle
			finalOrder[3] = i
			break
	for i in "abcdefg":
		if i not in finalOrder:
			# guess the last
			finalOrder[6] = i
			break
	currDigits = ["".join([str(finalOrder[a]) for a in range(len(d)) if d[a] != 0]) for d in digits]
	nb = []
	for i in output:
		for index, j in enumerate(currDigits):
			if len(i) != len(j):
				continue
			if all([k in i for k in j]):
				nb += [str(index)]
	t = int("".join(nb))
	s += [t]

print(sum(s))