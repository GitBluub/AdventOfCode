with open('input') as f:
    read_data = f.read().splitlines()
r = read_data[0]
for i in range(len(r) - 3):
    if (len(list(set(r[i:i+14]))) == 14):
        print(i + 14)
        exit(0)
