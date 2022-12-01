
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


validBingo = []
def bingoValid(bingo):
	for line in bingo:
		#print(" ".join(map(str, line)))
		if all([a == -1 for a in line]):
			validBingo = bingo
			return True
	rotated = zip(*bingo)
	for cols in rotated:
		#print(" ".join(map(str, cols)))
		if all([a == -1 for a in cols]):
			validBingo = bingo
			return True
	return False

finished = []

def bingosValid(bingos):
	r = []
	global finished
	for j,i in enumerate(bingos):
		isValid = bingoValid(i)
		if isValid and j not in finished:
			finished += [j]
		r+=[isValid]
	return all([bingoValid(bingo) for bingo in bingos])

r=0
for i in numbers:
	if bingosValid(bingos):
		break
	for k in range(len(bingos)):
		bingo = bingos[k]
		for j in range(len(bingo)):
			bingo[j] = [x if x != i else -1 for x in bingo[j]]
	lastN = i
	r += 1
for line in bingos[finished[-1]]:
	print(" ".join(map(str, line)))
print(finished)
r = sum([sum([a if a != -1 else 0 for a in l]) for l in bingos[finished[-1]]])
print(lastN)
print(r)
print(r * lastN)