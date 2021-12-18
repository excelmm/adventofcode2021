with open("input.txt", "r") as f:
    a = f.read().splitlines()

def main():
    p = ['[', ']', ',']
    mag = 0

    for i in a:
        for j in a:
            if i == j: continue
            n = '[' + i + ',' + j + ']'

            while True:
                # print(n)
                error = False

                # check nesting
                nestcount = 0
                for index, j in enumerate(n):
                    if j == '[': nestcount += 1
                    if j == ']': nestcount -= 1
                    if nestcount >= 5:
                        if n[index + 1] in p: continue

                        deepest = False
                        for k in n[index + 1:]:
                            if k == '[': break
                            if k == ']':
                                deepest = True
                                break
                        if not deepest: continue

                        error = True
                        endindex = None
                        endindex2 = None
                        for k in range(index + 1, len(n)):
                            if n[k] == ',': 
                                endindex = k
                                break
                        for k in range(index + 1, len(n)):
                            if n[k] == ']': 
                                endindex2 = k
                                break
                        left = int(n[index + 1:endindex])
                        right = int(n[endindex + 1:endindex2])
                        n = n[:index] + '0' + n[endindex2 + 1:]
                        for k in range(index - 1, 0, -1):
                            endindex = None
                            if n[k] not in p and n[k - 1] in p:
                                for l in range(k, len(n)):
                                    if n[l] in p:
                                        endindex = l
                                        break
                                index += len(str(left))
                                n = n[:k] + str(int(n[k:endindex]) + left) + n[endindex:]
                                break
                        for k in range(index + 1, len(n)):
                            endindex = None
                            if n[k] not in p:
                                for l in range(k, len(n)):
                                    if n[l] in p:
                                        endindex = l
                                        break
                                n = n[:k] + str(int(n[k:endindex]) + right) + n[endindex:]
                                break
                        break
                if error: continue
                
                # check splitting
                for index, j in enumerate(n):
                    if n[index] not in p and n[index + 1] not in p:
                        error = True
                        num = int(n[index:index + 2])
                        left = num // 2
                        right = num - left
                        newstr = '[' + str(left) + ',' + str(right) + ']'
                        n = n[:index] + newstr + n[index + 2:]
                        break

                if not error: break
            mag = max(mag, magnitude(n))

    print(mag)

# find magnitude
def magnitude(n):
    if ',' not in n:
        return int(n)
    n = n[1:len(n)-1]
    counter = 0
    final = 0
    if '[' not in n:
        first = int(n.split(",")[0])
        second = int(n.split(",")[1])
        final += 3 * first + 2 * second
    else:
        for index, i in enumerate(n):
            if i == '[': counter += 1
            if i == ']': counter -= 1
            if i == ',' and counter == 0:
                final += 3 * magnitude(n[:index]) + 2 * magnitude(n[index + 1:]) 
    return final

main()