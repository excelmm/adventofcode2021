with open("input.txt", "r") as f:
    a = f.read().splitlines()

adjList = {}
paths = set()

def main():
    for i in a:
        l = i.split("-")
        if l[0] not in adjList: adjList[l[0]] = []
        adjList[l[0]].append(l[1])
        if l[1] not in adjList: adjList[l[1]] = []
        adjList[l[1]].append(l[0])

    search('start', '')
    print(len(paths))

def search(current, path):
    if current in path and current.islower(): return
    path += current
    if current == 'end':
        paths.add(path)
        return
    if current in adjList:
        for i in adjList[current]:
            search(i, path)
    
main()