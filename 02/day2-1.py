with open("input.txt", "r") as f:
    a = f.read().splitlines()

p = 0
d = 0
for i in a:
    s = i.split(" ")
    if s[0] == 'forward':
        p += int(s[1])
    elif s[0] == 'down':
        d += int(s[1])
    else:
        d -= int(s[1])

print(p * d)