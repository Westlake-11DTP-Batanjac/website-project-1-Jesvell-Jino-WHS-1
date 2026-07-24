n = int(input())
a = list(map(int, input().split())) # A index is chef num, value is skill
d = a.copy() # dish list
copylist = [[] for i in range(n)]

for i in range(n):
    ci, *cq = map(int, input().split()) # ci the chef chosen and cq the chefs chosen chef can copy
    copylist[ci] = cq

q = int(input())

for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        s = d.copy() # simulation list
        sum = 0
        k, l, r = line[1], line[2], line[3] # kth day
        for i in range(k): #days
            for x in range(l, r): # per chefs
                chef = s[x]
                # MORNING
                if (a[x] * chef) > chef:
                    chef = a[x] * chef
                else:
                    pass
                # AFTERNOON
                for c in copylist[x]:
                    if (chef + c) > chef:
                        chef = chef + c
                s[x] = chef
        for x in range(l, r):
            sum += chef
        sum = sum % 10000000007
        print("sum", sum)
    elif line[0] == 2:
        i, x = line[1], line[2]
        i -= 1
        d[i] = d[i] + x