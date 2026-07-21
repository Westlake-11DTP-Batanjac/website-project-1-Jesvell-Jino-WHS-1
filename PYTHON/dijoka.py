colleon = {} # for connecitons
countleon = {} # counting
N = int(input())
for i in range(N):
    line = list(map(str, input().split()))
    operation = line[0]
    if operation == "SET":
            colleon[line[1]] = line[2]
            countleon[line[2]] = int(countleon[line[2]]) + 1
    elif operation == "COUNT":
        print(countleon.get(line[1]))
    elif operation == "GET":
        print(colleon.get(line[1]))
    elif operation == "REMOVE":
        countleon[colleon[line[1]]] = countleon[colleon[line[1]]] - 1
        colleon.pop(line[1])
    