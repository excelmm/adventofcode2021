with open("input.txt", "r") as f:
    a = f.read().splitlines()

positions = [int(i) for i in a[0].split(",")]

leastSum = 1000000000000000
maxPos = max(positions)
for i in range(maxPos):
    sum = 0
    for j in positions:
        sum += abs(i - j)
    leastSum = min(sum, leastSum)

print(leastSum)