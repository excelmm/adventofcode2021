with open("input.txt", "r") as f:
    a = f.read().splitlines()

count0 = [0] * 12
count1 = [0] * 12

for i in a:
    for j in range(12):
        if i[j] == '0':
            count0[j] += 1
        else: count1[j] += 1

finala = ''
finalb = ''

for i in range(12):
    if count0[i] > count1[i]:
        finala += '0'
        finalb += '1'
    else:
        finala += '1'
        finalb += '0'

finala = int(finala, 2)
finalb = int(finalb, 2)
print(finala * finalb)
