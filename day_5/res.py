with open('input') as f:
    read_data = f.read().splitlines()

row_range = range(2**7)
col_range = range(2**3)

L=[]
for i in read_data:
    row_deciding = range(2**7)
    for j in i[:7]:
        if j == 'F':
            row_deciding = row_deciding[:len(row_deciding) // 2]
        elif j == 'B':
            row_deciding = row_deciding[len(row_deciding) // 2:]
        else:
            print("problem")
    col_deciding = range(2**3)
    for j in i[7:]:
        if j == 'L':
            col_deciding = col_deciding[:len(col_deciding) // 2]
        elif j == 'R':
            col_deciding = col_deciding[len(col_deciding) // 2:]
        else:
            print("problem")
    seat_id = (row_deciding[0] * 8) + col_deciding[0]
    L += [seat_id]

L.sort()
for i in range(len(L) - 1):
    if L[i+1] - L[i] != 1:
        print(L[i] + 1) 