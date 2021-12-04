
with open('input') as f:
    read_data = f.read().splitlines()

numbers = list(map(int, read_data[0].split(',')))
bingos = read_data[1:]

t=[]
curr=[]
for i in bingos:
	if i == "":
		t += [curr]
		curr = []
	else:
		curr += [i]
t = [a for a in t if a != []]
t = [[list(map(int, x.split())) for x in a] for a in t]

bingos = t
lastN = None


def bingosValid(bingos):
	for bingo in bingos:
		for line in bingo:
			#print(" ".join(map(str, line)))
			if all([a == -1 for a in line]):
				return bingo
		rotated = zip(*bingo)
		for cols in rotated:
			#print(" ".join(map(str, cols)))
			if all([a == -1 for a in cols]):
				return bingo
		#if all([bingo[a][a] == -1 for a in range(len(bingo))]):
		#	return bingo
		#if all([bingo[a][len(bingo)-1-a] == -1 for a in range(len(bingo))]):
		#	return bingo
	return []

r=0
numbersvalid = []
validBingo = []
for i in numbers:
	validBingo = bingosValid(bingos)
	if validBingo != []:
		break
	for k in range(len(bingos)):
		bingo = bingos[k]
		for j in range(len(bingo)):
			bingo[j] = [x if x != i else -1 for x in bingo[j]]
	lastN = i
	numbersvalid += [lastN]
	r += 1
numbersvalid = numbersvalid[:-1]
for line in validBingo:
	print(" ".join(map(str, line)))
r = sum([sum([a if a != -1 else 0 for a in l]) for l in validBingo])
print(lastN)
print(r)
print(r * lastN)