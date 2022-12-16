import sys
s = "input"
if len(sys.argv) > 1:
    s = sys.argv[1]
with open(s) as f:
    read_data = f.read().splitlines()
parsed = []
m = [["." for _ in range(maxX)] for _ in range(maxY)]
for i in read_data:
    i = i.replace("Sensor at x=", "").replace(", y=", " ").replace(" closest beacon is at x=", "")
    a, b = i.split(":")
    sx, sy = map(int, a.split())
    bx, by = map(int, b.split())
    parsed += [(sx, sy, bx, by)]
