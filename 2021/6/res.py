with open('input') as f:
    read_data = f.read().splitlines()

nbs = list(map(int, read_data[0].split(',')))
cache = [[0 for j in range(257)] for i in range(9)]

def nbOfLanternFish(initialValue, nbOfDays):
	if (nbOfDays == 0):
		return len(initialValue)
	if (len(initialValue) != 1):
		return sum([nbOfLanternFish([i], nbOfDays) for i in initialValue])
	if cache[initialValue[0]][nbOfDays] != 0:
		return cache[initialValue[0]][nbOfDays]
	arr = initialValue
	new_arr = [j - 1 for j in arr if j != 0]
	new_arr += [6, 8] * arr.count(0)
	cache[initialValue[0]][nbOfDays] = nbOfLanternFish(new_arr, nbOfDays-1)
	return cache[initialValue[0]][nbOfDays]

a = [nbOfLanternFish([i], 256) for i in range(6)]
print(a)
print(sum([a[i] for i in nbs]))