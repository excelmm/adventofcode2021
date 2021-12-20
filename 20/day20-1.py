import math
import copy
with open("input.txt", "r") as f:
    a = f.read().splitlines()

SIZE = 1000

m = [['.' for _ in range(SIZE)] for _ in range(SIZE)]

algo = a[0]
a = a[2:]

r = len(a)
c = len(a[0])

for i in range(r):
    for j in range(c):
        m[SIZE // 2 + i][SIZE // 2 + j] = a[i][j]

for _ in range(2):
    newm = copy.deepcopy(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == 0 or i == len(m) - 1:
                newm[i][j] = '#' if m[i][j] == '.' else '.'
            elif j == 0 or j == len(m[i]) - 1:
                newm[i][j] = '#' if m[i][j] == '.' else '.'
            else:
                current = m[i - 1][j - 1] + m[i - 1][j] + m [i - 1][j + 1] + m[i][j - 1] + m[i][j] + m[i][j + 1] + m[i + 1][j - 1] + m[i + 1][j] + m[i + 1][j + 1]
                current = int(current.replace('.', '0').replace('#', '1'), 2)
                newm[i][j] = algo[current]
    m = copy.deepcopy(newm)

    # for i in m:
    #     for j in i:
    #         print(j, end="")
    #     print()

count = 0
for i in m:
    count += i.count('#')
print(count)