with open('input') as f:
    read_data = f.read().splitlines()

read_data = list(map(lambda x: int(x), read_data))
target_year = 2020

def get_binomial(read_data, target):
    for i in read_data:
        missing = target - i
        if missing in read_data:
            print(missing, i)
            print(missing * i)
            return [missing, i]

    return [0, 0]
def get_trinomial(read_data, target):
    for i in read_data:
        missing = target - i
        j, k = get_binomial(read_data, missing)
        if j and k:
            print(i, j, k)
            print(i * j * k)
            return [i, j, k]


# get_binomial(read_data, target_year)
get_trinomial(read_data, target_year)