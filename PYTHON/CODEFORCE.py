n = int(input())
a = list(map(int, input().split()))
copylist = [[] for i in range(n)]

for i in range(n):
    ci, *d = map(int, input().split())
    copylist[ci] = d

q = int(input())

for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        k, l, r = line[1], line[2], line[3]
        print()
    elif line[0] == 2:
        i, x = line[1], line[2]
        print()

print(n, a, copylist)