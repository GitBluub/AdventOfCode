with open('input') as f:
    read_data = f.read().splitlines()

data = [x.split('|') for x in read_data]

l = sum([len([y for y in x[1].split() if len(y) in [2,3,4,7]]) for x in data])
print(l)