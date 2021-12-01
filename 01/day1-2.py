with open("input.txt", "r") as f:
    a = f.read().splitlines()

count = 0
for i in range(3, len(a)):
    if int(a[i]) + int(a[i - 1]) + int(a[i - 2]) > int(a[i - 1]) + int(a[i - 2]) + int(a[i - 3]):
        count += 1
print(count)