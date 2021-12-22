with open("input.txt", "r") as f:
    a = f.read().splitlines()

SIZE = 102

m = [[[0 for _ in range(SIZE)] for _ in range(SIZE)] for _ in range(SIZE)]

for i in a:
    inst = i.split(" ")[0]
    coords = i.split(" ")[1].split(",")
    x1, x2 = (int(j) for j in coords[0].split("=")[1].split(".."))
    y1, y2 = (int(j) for j in coords[1].split("=")[1].split(".."))
    z1, z2 = (int(j) for j in coords[2].split("=")[1].split(".."))

    if x1 > 100 or abs(y1) > 100 or abs(z1) > 100: continue
    x1 += 50
    x2 += 50
    y1 += 50
    y2 += 50
    z1 += 50
    z2 += 50
    if inst == 'on':
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                for k in range(z1, z2 + 1):
                    m[i][j][k] = 1
    else:
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                for k in range(z1, z2 + 1):
                    m[i][j][k] = 0

count = 0
for i in m:
    for j in i:
        count += j.count(1)
print(count)