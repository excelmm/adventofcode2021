import copy
with open("input.txt", "r") as f:
    a = f.read().splitlines()

timer = [int(j) for j in a[0].split(",")]

digit = [0] * 9
for i in timer:
    digit[i] += 1

for _ in range(80):
    j = digit[0]
    for i in range(8):
        digit[i] = digit[i + 1]
    digit[6] += j
    digit[8] = j

print(sum(digit))