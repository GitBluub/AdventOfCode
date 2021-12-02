with open('input') as f:
    read_data = f.read().splitlines()


depths = list(map(int, read_data))
a = None
prev = 0
measurements = [sum(depths[i:i + 3]) for i in range( len(depths) - 1) ]
for i in measurements:
	if a is None:
		a = i
		continue
	prev += i > a
	a = i
print(prev)	