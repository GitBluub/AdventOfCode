with open('input') as f:
    read_data = f.read().splitlines()

cycle = 0
x = 1
r = []
crt = [["." for i in range(40)] for i in range(6)]
cycle = 0
for i in read_data:
    cmd = i.split()[0]
    if cmd == "noop":
        x_p = cycle % 40
        y = cycle // 40
        if abs(x - x_p) <= 1:
            crt[y][x_p] = "#"
        r += [x]
        cycle += 1
    else:
        n = int(i.split()[1])
        x_p = cycle % 40
        y = cycle // 40
        if abs(x - x_p) <= 1:
            crt[y][x_p] = "#"

        r += [x]
        cycle += 1
        x_p = cycle % 40
        y = cycle // 40
        if abs(x - x_p) <= 1:
            crt[y][x_p] = "#"

        r += [x]
        cycle += 1
        x += n
for i in crt:
    print("".join(i))
