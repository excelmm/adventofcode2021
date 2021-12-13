with open("input.txt", "r") as f:
    a = f.read().splitlines()

maxr = 0
maxc = 0
for i in a:
    j = i.split(",")
    if j[0] == '': break
    maxr = max(int(j[1]) + 1, maxr)
    maxc = max(int(j[0]) + 1, maxc)

m = [[0 for _ in range(maxc)] for _ in range(maxr)]

for i in a:
    if ',' in i:
        j = [int(p) for p in i.split(",")]
        m[j[1]][j[0]] = 1
    elif 'fold' in i:
        axis = i.split(" ")[2]
        line = int(axis.split("=")[1])
        if axis[0] == 'x':
            newm = [[0 for _ in range(maxc // 2)] for _ in range(maxr)]
            for i in range(maxr):
                for j in range(maxc // 2):
                    newm[i][j] = max(m[i][j], m[i][maxc - 1 - j])
        break

count = 0
for i in newm:
    for j in i:
        if j == 1: count += 1
print(count)
