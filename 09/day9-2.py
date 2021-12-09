with open("input.txt", "r") as f:
    a = f.read().splitlines()

basins = {}
traversed = set()

def main():

    for i in range(len(a)):
        for j in range(len(a[i])):
            comp = []
            if j < len(a[i]) - 1: comp.append(a[i][j + 1])
            if j > 0: comp.append(a[i][j - 1])
            if i < len(a) - 1: comp.append(a[i + 1][j])
            if i > 0: comp.append(a[i - 1][j])
            comp = [int(k) for k in comp]
            if int(a[i][j]) < min(comp):
                basins[(i, j)] = 0

    for (i, j) in basins:
        traverse(i, j, i , j)
    final = sorted(list(basins.values()))
    print(final[-1] * final[-2] * final[-3])

def traverse(oi, oj, i, j):
    if a[i][j] == '9': return
    if (i, j) not in traversed:
        traversed.add((i, j))
        basins[(oi, oj)] += 1

        if j > 0:
            traverse(oi, oj, i, j - 1)
        
        if j < len(a[i]) - 1:
            traverse(oi, oj, i, j + 1)
        
        if i > 0:
            traverse(oi, oj, i - 1, j)
        
        if i < len(a) - 1:
            traverse(oi, oj, i + 1, j)

main()