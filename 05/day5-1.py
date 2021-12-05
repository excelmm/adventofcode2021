import re
with open("input.txt", "r") as f:
    a = f.read().splitlines()

b = []
for i in range(1000):
    n = []
    for j in range(1000):
        n.append(0)
    b.append(n)

reg = r"(.*),(.*) -> (.*),(.*)"

for i in a:
    r = [int(j) for j in re.findall(reg, i)[0]]
    if r[0] != r[2] and r[1] != r[3]: continue
    for j in range(min(r[1], r[3]), max(r[1], r[3]) + 1):
        for k in range(min(r[0], r[2]), max(r[0], r[2]) + 1):
            b[j][k] += 1

count = 0
for i in b:
    for j in i:
        if j > 1: count += 1
        
print(count)