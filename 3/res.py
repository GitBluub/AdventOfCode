with open('input') as f:
    read_data = f.read().splitlines()

a = [sum( [int(read_data[j][i]) for j in range(len(read_data))] ) for i in range(12)]
r = len(read_data)
s = ["1" if a[i] >= r / 2 else "0" for i in range(12)]
s2 = ["0" if a[i] >= r / 2 else "1" for i in range(12)]
 
print("".join(s))
gamma = int("".join(s), 2)
epsilon = int("".join(s2), 2)
print(gamma * epsilon)