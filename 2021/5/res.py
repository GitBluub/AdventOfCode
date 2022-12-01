
with open('input') as f:
    read_data = f.read().splitlines()

vents = []
n=0
for i in read_data:
	a,b = i.split(' -> ')
	x1, y1 = list(map(int, a.split(",")))
	x2, y2 = list(map(int, b.split(",")))
	n=max(n, x1, x2, y1, y2)
	vents += [([x1, y1], [x2, y2])]
board = [[0 for i in range(n+1)] for j in range(n+1)]


for a, b in vents:
	x1, y1 = a
	x2, y2 = b
	if x1 == x2:
		y1, y2 = min(y1, y2), max(y1, y2)
		for i in range(y1, y2+1):
			board[x1][i] += 1
	elif y1 == y2:
		x1, x2 = min(x1, x2), max(x1, x2)
		for i in range(x1, x2+1):
			board[i][y1] += 1
	else:
		yneg = y1 > y2
		xneg = x1 > x2
		for i in range(abs(x2 - x1) + 1):
			y = y1 - i if yneg else y1 + i
			x = x1 - i if xneg else x1 + i
			board[x][y] += 1
r = sum(sum([1 for x in i if x >= 2]) for i in board)
print(r)