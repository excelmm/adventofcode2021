with open("input.txt", "r") as f:
    a = f.read().splitlines()

die = 0
count = 0
s1 = 0
s2 = 0
p1 = int(a[0].split(": ")[1])
p2 = int(a[1].split(": ")[1])

while True:
    roll = 0
    for _ in range(3):
        die += 1
        while die > 100: 
            die -= 100
        roll += die
    count += 3
    p1 += roll
    while p1 > 10: 
        p1 -= 10
    s1 += p1
    if s1 >= 1000:
        print(s2 * count)
        break
    roll = 0
    for _ in range(3):
        die += 1
        if die > 100: die -= 100
        roll += die
    count += 3
    p2 += roll
    while p2 > 10: 
        p2 -= 10
    s2 += p2
    if s2 >= 1000:
        print(s1 * count)
        break