with open('input') as f:
    read_data = f.read().splitlines()

m = [list(map(int, r)) for r in read_data]
lowP = []
for i, a in enumerate(m):
	for j, b in enumerate(a):
		if j != 0 and a[j-1] <= b:
			continue
		if j != len(a) - 1 and a[j+1] <= b:
			continue
		if i != 0 and m[i - 1][j] <= b:
			continue
		if i != len(m) - 1 and m[i + 1][j] <= b:
			continue
		lowP += [(i, j)]

basin = []	
def recBasin(i, j, b):
	global basin
	if i * len(m) + j in basin:
		return
	if m[i][j] >= b and m[i][j] != 9:
		basin += [(i * len(m)) + j]
	else:
		return
	if i != 0:
		recBasin(i-1, j, b)	
	if i != len(m) - 1:
		recBasin(i+1, j, b)	
	if j != 0:
		recBasin(i, j-1, b)	
	if j != len(m[0]) - 1:
		recBasin(i, j+1, b)

def getBasinSize(i, j):
	global basin
	basin = []
	recBasin(i, j, m[i][j])
	return len(basin)

basinsSize = [getBasinSize(i, j) for i, j in lowP]
basinsSize.sort()
print(basinsSize[-1] * basinsSize[-2] * basinsSize[-3])