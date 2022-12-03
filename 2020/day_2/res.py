with open('input') as f:
    read_data = f.read().splitlines()

def is_valid_password_range(password_line):
    password_chr_range, password_policy, password = password_line.split()
    password_policy = password_policy[:-1]
    password_range_min, password_range_max = list(map(lambda x: int(x), password_chr_range.split('-')))
    res = password.count(password_policy)
    if res in range(password_range_min, password_range_max + 1):
        return True
    else:
        return False

def is_valid_password_pos(password_line):
    password_chr_range, password_policy, password = password_line.split()
    password_policy = password_policy[:-1]
    password_range_min, password_range_max = list(map(lambda x: int(x), password_chr_range.split('-')))
    res = 0
    if password[password_range_min -1] == password_policy:
        res += 1
    if password[password_range_max - 1] == password_policy:
        res += 1
    if res == 1:
        return True
    else:
        return False

def get_nb_valid_password(read_data, password_policy_func):
    res = 0
    for i in read_data:
        res += password_policy_func(i)
    print(res)

get_nb_valid_password(read_data, is_valid_password_pos)
