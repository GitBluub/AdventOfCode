with open('input') as f:
    read_data = f.read().splitlines()

def slope(x, y):
    pos_y = 0
    pos_x = 0
    res = 0
    while pos_y < len(read_data):
        if read_data[pos_y][pos_x] == '#':
            res += 1
        pos_x += x
        pos_y += y
        pos_x = pos_x % len(read_data[0])
        if pos_y >= len(read_data):
            break
    return res

total_res = 1

total_res *= slope(1, 1)
total_res *= slope(3, 1)
total_res *= slope(5, 1)
total_res *= slope(7, 1)
total_res *= slope(1, 2)
print(total_res)