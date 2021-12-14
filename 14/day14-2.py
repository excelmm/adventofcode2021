with open("input.txt", "r") as f:
    a = f.read().splitlines()

template = a[0]
final = {}
final[template[-1]] = 1
charset = {}

for i in range(len(template) - 1):
    pair = template[i] + template[i + 1]
    if pair not in charset: charset[pair] = 0
    charset[pair] += 1

rules = {}

for i in a[2:]:
    j = i.split(" -> ")
    rules[j[0]] = j[1]

for _ in range(40):
    newcharset = {}
    for i in charset:
        new = (i[0] + rules[i], rules[i] + i[1])
        if new[0] not in newcharset: newcharset[new[0]] = 0
        if new[1] not in newcharset: newcharset[new[1]] = 0
        newcharset[new[0]] += charset[i]
        newcharset[new[1]] += charset[i]
    charset = newcharset
  
for i in charset:
    if i[0] not in final: final[i[0]] = 0
    final[i[0]] += charset[i]

vals = [v for v in final.values()]
print(max(vals) - min(vals))