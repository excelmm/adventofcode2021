with open("input.txt", "r") as f:
    a = f.read().splitlines()

die = 0
count = 0
s1 = 0
s2 = 0
p1 = int(a[0].split(": ")[1])
p2 = int(a[1].split(": ")[1])

win_count = {}
def count(p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in win_count:
        return win_count[(p1, p2, s1, s2)]
    wins = (0, 0)
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                next_p1 = p1 + i + j + k
                if next_p1 > 10: next_p1 -= 10
                next_s1 = s1 + next_p1

                w = count(p2, next_p1, s2, next_s1)
                wins = (wins[0] + w[1], wins[1] + w[0])
    win_count[(p1, p2, s1, s2)] = wins
    return wins

print(max(count(p1, p2, s1, s2)))