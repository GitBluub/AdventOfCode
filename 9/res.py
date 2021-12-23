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
		lowP += [b + 1]
print(sum(lowP))
