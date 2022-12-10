with open('input') as f:
    read_data = f.read().splitlines()

cycle = 0
x = 1
r = []
for i in read_data:
    cmd = i.split()[0]
    if cmd == "noop":
        r += [x]
    else:
        n = int(i.split()[1])
        r += [x]
        r += [x]
        x += n
print(sum([r[19] * 20, r[59] * 60, r[99] * 100, r[139] * 140, r[179] * 180, r[219] * 220]))
