with open('input') as f:
    read_data = f.read().splitlines()

i = 0
a = []
for l in read_data:
    if l == "":
        i += 1
    else:
        if len(a) < i + 1: a += [0]
        a[i] += int(l)
a.sort()
a = a[::-1]
print(sum(a[:3]))
