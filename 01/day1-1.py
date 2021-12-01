with open("input.txt", "r") as f:
    a = f.read().splitlines()

count = 0
for i in range(1, len(a)):
    if int(a[i]) > int(a[i - 1]):
        count += 1

print(count)