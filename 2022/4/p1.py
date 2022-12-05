with open('input') as f:
    read_data = f.read().splitlines()

r=0
for i in read_data:
  a,b = i.split(",")
  c,d = map(int, a.split("-"))
  e,f = map(int, b.split("-"))
  mini, maxi = min([c,d,e,f]), max([c,d,e,f])
  if (c == mini and d == maxi) or (e == mini and f == maxi): r += 1
print(r)
