with open("input.txt", "r") as f:
    a = f.read().splitlines()

calls = [int(i) for i in a[0].split(",")]
boards = []

currBoard = []
for i in a[2:]:
    if i == '':
        boards.append(currBoard)
        currBoard = []
    else:
        currBoard.append([int(j) for j in i.strip().split()])

for i in calls:
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if i == boards[b][r][c]:
                    boards[b][r][c] = -1
        for r in range(len(boards[b])):
            if sum(boards[b][r]) == -5:
                sum = 0
                for r in range(len(boards[b])):
                    for c in range(len(boards[b][r])):
                        if boards[b][r][c] != -1:
                            sum += boards[b][r][c]
                print(sum * i)
                exit()
        for c in range(5):
            if boards[b][0][c] + boards[b][1][c] + boards[b][2][c] + boards[b][3][c] + boards[b][4][c] == -5:
                sum = 0
                for r in range(len(boards[b])):
                    for c in range(len(boards[b][r])):
                        if boards[b][r][c] != -1:
                            sum += boards[b][r][c]
                print(sum * i)
                exit()
