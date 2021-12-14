with open("input.txt", "r") as f:
    a = f.read().splitlines()

template = a[0]
charset = set()
for i in template:
    charset.add(i)
rules = {}

for i in a[2:]:
    j = i.split(" -> ")
    rules[j[0]] = j[1]
    charset.add(j[1])

for _ in range(10):
    new_template = template
    j = 1
    for i in range(len(template) - 1):
        new_template = new_template[:j] + rules[template[i:i+2]] + new_template[j:]
        j += 2
    template = new_template

final = [template.count(c) for c in charset]
print(max(final) - min(final))