import sys
s = "input"
if len(sys.argv) > 1:
    s = sys.argv[1]
with open(s) as f:
    read_data = f.read().splitlines()
parsed = []
r = []
target = 2000000
for i in read_data:
    i = i.replace("Sensor at x=", "").replace(", y=", " ").replace(" closest beacon is at x=", "")
    a, b = i.split(":")
    sx, sy = map(int, a.split())
    bx, by = map(int, b.split())
    parsed += [(sx, sy, bx, by)]
    d = abs(sx - bx) + abs(sy - by)
    if sy - d >= target or  sy + d <= target: continue
    offset2 = abs(target - sy)
    offset = d - offset2
    for x in range(offset + 1):
        w = sx - x
        if w != bx or target != by:
            r += [w]
        w = sx + x
        if (bx != w or by != target):
            r += [w]
print(len(set(r)))
