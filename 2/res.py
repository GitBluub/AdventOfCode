with open('input') as f:
    read_data = f.read().splitlines()

aim = 0
horizontal = 0
depth = 0
for i in read_data:
	s = i.split(' ')
	if s[0] == "forward":
		horizontal += int(s[1])
		depth += int(s[1]) * aim
	if s[0] == "up":
		aim -= int(s[1])
	if s[0] == "down":
		aim += int(s[1])

print(depth * horizontal)