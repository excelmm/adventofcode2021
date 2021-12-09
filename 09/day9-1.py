with open("input.txt", "r") as f:
    a = f.read().splitlines()

sum = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        comp = []
        if j < len(a[i]) - 1: comp.append(a[i][j + 1])
        if j > 0: comp.append(a[i][j - 1])
        if i < len(a) - 1: comp.append(a[i + 1][j])
        if i > 0: comp.append(a[i - 1][j])
        comp = [int(k) for k in comp]
        if int(a[i][j]) < min(comp):
            sum += int(a[i][j]) + 1

print(sum)