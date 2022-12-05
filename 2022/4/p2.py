with open('input') as f:
    read_data = f.read().splitlines()

r=0
for i in read_data:
  a,b = i.split(",")
  c,d = map(int, a.split("-"))
  e,f = map(int, b.split("-"))
  g, h = max(c, e), min(d, f)
  if h >= g: r += 1
print(r)
