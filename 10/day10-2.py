from statistics import median
with open("input.txt", "r") as f:
    a = f.read().splitlines()

scores = []
for i in a:
    score = 0
    s = []
    invalid = False
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
                invalid = True
                break
    if not invalid and len(s):
        s.reverse()
        for j in s:
            score *= 5
            if j == '(':
                score += 1
            elif j == '[':
                score += 2
            elif j == '{':
                score += 3
            else:
                score += 4
        scores.append(score)

print(median(sorted(scores)))