from itertools import permutations
import copy
with open("input.txt", "r") as f:
    a = f.read().splitlines()

sum = 0
for i in a:
    m = {
        '1110111': 0,
        '0010010': 1,
        '1011101': 2,
        '1011011': 3,
        '0111010': 4,
        '1101011': 5,
        '1101111': 6,
        '1010010': 7,
        '1111111': 8,
        '1111011': 9
    }
    test = i.split("|")[0].strip().split(" ")
    output = i.split("|")[1].strip().split(" ")
    possible = [''.join(p) for p in permutations('abcdefg')]
    for j in test:
        newpossible = copy.deepcopy(possible)
        for k in newpossible:
            t = [0] * 7
            for l in j:
                t[k.find(l)] += 1
            key = ''.join([str(p) for p in t])
            if key not in m:
                possible.remove(k)

    final = []
    for j in output:
        t = [0] * 7
        for l in j:
            t[possible[0].find(l)] += 1
        key = ''.join([str(p) for p in t])
        final.append(m[key])
    sum += int(''.join([str(p) for p in final]))

print(sum)