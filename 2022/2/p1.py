with open('input') as f:
    read_data = f.read().splitlines()


y = ["A", "B", "C"]
x = ["X", "Y", "Z"]
r = 0
for l in read_data:
    a, b = l.split()
    r += x.index(b) + 1
    if (y.index(a) - x.index(b)) % 3 == 2:
        r += 6
    if (y.index(a) == x.index(b)):
        r += 3

print(r)
