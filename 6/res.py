with open('input') as f:
    read_data = f.read().splitlines()

nbs = list(map(int, read_data[0].split(',')))
def nbOfLanternFish(initialValue, nbOfDays):
	arr = [initialValue]
	for i in range(nbOfDays):
		new_arr = []
		for j in arr:
			if j == 0:
				new_arr.append(6)
				new_arr.append(8)
			else:
				new_arr.append(j-1)
		arr = new_arr
	return len(arr)
a = [nbOfLanternFish(i, 80) for i in range(6)]
print(a)
print(sum([a[i] for i in nbs]))