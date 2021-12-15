import heapq
with open("input.txt", "r") as f:
    a = f.read().splitlines()

r = len(a)
c = len(a[0])

m = [[0 for _ in range(c * 5)] for _ in range(r * 5)]

for i in range(r * 5): 
    for j in range(c * 5):
        m[i][j] = int(a[i % r][j % c]) + i // r + j // c
        if m[i][j] > 9: m[i][j] -= 9

r *= 5
c *= 5
adj_list = {}

for i in range(c):
    for j in range(r):
        if (i, j) not in adj_list: adj_list[(i, j)] = []
        if i > 0: adj_list[(i, j)].append((i - 1, j))
        if i < r - 1: adj_list[(i, j)].append((i + 1, j))
        if j > 0: adj_list[(i, j)].append((i, j - 1))
        if j < c- 1: adj_list[(i, j)].append((i, j + 1))

visited = set()
distance = {}
for i in adj_list:
    distance[i] = 10000000000
distance[(0, 0)] = 0

queue = [(0, (0, 0))]
while queue:
    current = heapq.heappop(queue)[1]
    for i in adj_list[current]:
        if i in visited: continue
        if distance[i] > distance[current] + m[i[0]][i[1]]:
            distance[i] = distance[current] + m[i[0]][i[1]]
            heapq.heappush(queue, (distance[i], i))
    visited.add(current)
    
print(distance[(r - 1, c - 1)])