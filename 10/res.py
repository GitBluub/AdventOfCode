with open('input') as f:
    read_data = f.read().splitlines()

sStack = []
mistakes = []
for l in read_data:
	m = False
	for j in l:
		if m:
			continue
		if j in "[(<{":
			sStack += [j]
		else:
			shouldBe = "])>}"["[(<{".index(sStack[-1])]
			if j != shouldBe:
				mistakes += [j]
				m = True
			else:
				sStack.pop()
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
print(sum([points[i] for i in mistakes]))