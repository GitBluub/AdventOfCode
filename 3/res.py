with open('input') as f:
    read_data = f.read().splitlines()

a = [sum( [int(read_data[j][i]) for j in range(len(read_data))] ) for i in range(12)]
r = len(read_data)
s = ["1" if a[i] >= r / 2 else "0" for i in range(12)]
s2 = ["0" if a[i] >= r / 2 else "1" for i in range(12)]
 
gamma = int("".join(s), 2)
epsilon = int("".join(s2), 2)

arr = [i for i in read_data]
arr2 = [i for i in read_data]

i = 0
r1=""
r2=""
while len(arr) > 0 and i < 12:
	if len(arr) == 1:
		r1 = arr[0]
		break
	n = sum( [int(arr[j][i]) for j in range(len(arr))] )
	if n >= len(arr) / 2:
		r1 += "1"
		arr = [arr for arr in arr if arr[i] == "1"]
	else:
		r1 += "0"
		arr = [arr for arr in arr if arr[i] == "0"]
	i += 1 

i = 0
while len(arr2) > 0 and i <  12:
	if len(arr2) == 1:
		r2 = arr2[0]
		break
	nbOne = sum( [int(arr2[j][i]) for j in range(len(arr2))] )
	nbZero = len(arr2) - nbOne
	if nbZero <= nbOne:
		r2 += "0"
		arr2 = [n for n in arr2 if n[i] == '0']
	else:
		r2 += "1"
		arr2 = [n for n in arr2 if n[i] == '1']
	print(arr2)
	i += 1
print("r2")
print(r2)
oxygen = int(r1, 2)
co2 = int(r2, 2)
print(oxygen)
print(co2)
print(oxygen * co2)