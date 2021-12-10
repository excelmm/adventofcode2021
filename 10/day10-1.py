with open("input.txt", "r") as f:
    a = f.read().splitlines()

count = 0
for i in a:
    s = []
    for j in i:
        if j in ['(', '[', '{', '<']:
            s.append(j)
        else:
            if j == ')' and s[-1] == '(':
                s.pop()
            elif j == ']' and s[-1] == '[':
                s.pop()
            elif j == '}' and s[-1] == '{':
                s.pop()
            elif j == '>' and s[-1] == '<':
                s.pop()
            else:
                if j == ')': count += 3
                elif j == ']': count += 57
                elif j == '}': count += 1197
                else: count += 25137
                break

print(count)