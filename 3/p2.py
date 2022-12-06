with open('input') as f:
    read_data = f.read().splitlines()

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
gr = [read_data[i:i + 3] for i in range(0, len(read_data), 3,)]
r = 0
for i in gr:
    a, b, c = i
    d = { x for x in a if x in b and x in c }
    r += sum([abc.index(x) + 1 for x in d])
print(r)
