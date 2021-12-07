with open('input') as f:
    read_data = f.read().splitlines()

nbs = list(map(int, read_data[0].split(',')))
print(min([sum([abs(j-i) for j in nbs]) for i in nbs]))