with open("input.txt", "r") as f:
    a = f.read().splitlines()

m = [[0 for _ in range(len(a))] for _ in range(len(a[0]))]
flashed = {}

def main():
    for i in range(len(a)):
        for j in range(len(a[i])):
            m[i][j] = int(a[i][j])
            flashed[(i, j)] = False

    for s in range(10000000):
        found = True
        for i in range(len(a)):
            for j in range(len(a[i])):
                flashed[(i, j)] = False
        for i in range(len(a)):
            for j in range(len(a[i])):
                if m[i][j] >= 9:
                    flash(i, j)
                else: m[i][j] += 1
        for i in range(len(a)):
            for j in range(len(a[i])):
                if m[i][j] == 9 and flashed[(i, j)]: 
                    m[i][j] = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if m[i][j] != 0: found = False
        if found:
            print(s + 1)
            exit()

def flash(i, j):
    if flashed[(i, j)]: return
    flashed[(i, j)] = True
    if i > 0:
        if m[i - 1][j] <= 9: m[i - 1][j] += 1
        if m[i - 1][j] >= 10: 
            m[i - 1][j] = 9
            flash(i - 1, j)
    if j > 0:
        if m[i][j - 1] <= 9: m[i][j - 1] += 1
        if m[i][j - 1] >= 10: 
            m[i][j - 1] = 9
            flash(i, j - 1)
    if i < len(a) - 1:
        if m[i + 1][j] <= 9: m[i + 1][j] += 1
        if m[i + 1][j] >= 10: 
            m[i + 1][j] = 9
            flash(i + 1, j)
    if j < len(a[0]) - 1:
        if m[i][j + 1] <= 9: m[i][j + 1] += 1
        if m[i][j + 1] >= 10: 
            m[i][j + 1] = 9
            flash(i, j + 1)
    if i > 0 and j > 0:
        if m[i - 1][j - 1] <= 9: m[i - 1][j - 1] += 1
        if m[i - 1][j - 1] >= 10: 
            m[i - 1][j - 1] = 9
            flash(i - 1, j - 1)
    if i > 0 and j < len(a[0]) - 1:
        if m[i - 1][j + 1] <= 9: m[i - 1][j + 1] += 1
        if m[i - 1][j + 1] >= 10: 
            m[i - 1][j + 1] = 9
            flash(i - 1, j + 1)
    if i < len(a) - 1 and j > 0:
        if m[i + 1][j - 1]  <= 9: m[i + 1][j - 1] += 1
        if m[i + 1][j - 1] >= 10: 
            m[i + 1][j - 1] = 9
            flash(i + 1, j - 1)
    if i < len(a) - 1 and j < len(a[0]) - 1:
        if m[i + 1][j + 1] <= 9: m[i + 1][j + 1] += 1
        if m[i + 1][j + 1] >= 10: 
            m[i + 1][j + 1] = 9
            flash(i + 1, j + 1)

main()