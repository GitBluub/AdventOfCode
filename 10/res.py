with open('input') as f:
    read_data = f.read().splitlines()

sStack = []
mistakes = []
completions = []
for l in read_data:
	m = False
	sStack = []
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
	if not m:
		r = []
		for j in sStack[::-1]:
			r += "])>}"["[(<{".index(j)]
		completions += ["".join(r)]
# points = {")": 3, "]": 57, "}": 1197, ">": 25137}
# print(sum([points[i] for i in mistakes]))
def completionScore(completion):
	res = 0
	for i in completion:
		res *= 5
		res += ")]}>".index(i) + 1
	return res
c = list(map(completionScore, completions))
c.sort()
print(c[len(completions) // 2])