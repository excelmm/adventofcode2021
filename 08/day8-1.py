with open("input.txt", "r") as f:
    a = f.read().splitlines()

count = 0
for i in a:
    s = i.split("|")[1].strip().split(" ")
    for j in s:
        if len(j) in [2, 4, 7, 3]:
            count += 1

print(count)