with open('input') as f:
    read_data = f.read().splitlines()

depths = map(int, read_data)
a = None
prev = 0
for i in depths:
	if a is None:
		a = i
		continue
	prev += i > a
	a = i
print(prev)