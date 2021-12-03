import re
with open("input.txt", "r") as f:
    a = f.read().splitlines()

count0a = [0] * 12
count0b = [0] * 12
count1a = [0] * 12
count1b = [0] * 12

founda = False
foundb = False

finala = ''
finalb = ''

rega = '(^'
regb = '(^'

for k in range(12):
    foundcounta = 0
    foundcountb = 0
    currStringa = ''
    currStringb = ''
    for i in a:
        if k == 0:
            if i[k] == '0':
                count0a[k] += 1
                count0b[k] += 1
            else: 
                count1a[k] += 1
                count1b[k] += 1
        else:
            if re.search(rega + '.*)', i) and not founda:
                foundcounta += 1
                if i[k] == '0':
                    count0a[k] += 1
                else: 
                    count1a[k] += 1
                if foundcounta == 1:
                    currStringa = i
            if re.search(regb + '.*)', i) and not foundb:
                foundcountb += 1
                if i[k] == '0':
                    count0b[k] += 1
                else: 
                    count1b[k] += 1
                if foundcountb == 1:
                    currStringb = i
                if k == 11: print(i)
    
    if foundcounta == 1:
        founda = True
        finala = re.search(rega + '.*)', currStringa).group(1)
        #print(finala)
    if foundcountb == 1:
        foundb = True
        finalb = re.search(regb + '.*)', currStringb).group(1)
        #print(finalb)

    if not founda:
        if count0a[k] > count1a[k]:
            finala += '0'
            rega += '0'
        else:
            finala += '1'
            rega += '1'

    if not foundb:         
        if count0b[k] <= count1b[k]:
            finalb += '0'
            regb += '0'
        else:
            finalb += '1'
            regb += '1'

finala = int(finala, 2)
finalb = int(finalb, 2)
print(finala * finalb)
