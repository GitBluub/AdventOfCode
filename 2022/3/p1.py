with open('input') as f:
    read_data = f.read().splitlines()

abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = 0
for i in read_data:
    l = len(i) // 2
    a, b = i[:l], i[l:]
    d = { x for x in a if x in b }
    r += sum([abc.index(x) + 1 for x in d])
print(r)
