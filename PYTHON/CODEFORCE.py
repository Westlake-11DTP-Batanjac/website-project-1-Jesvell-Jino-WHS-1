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
                if (a[x] * s[x]) > chef:
                    chef = a[x] * chef
                else:
                    pass
                # AFTERNOON
                for i in a[x]:
                    if (chef + i) > chef:
                        chef = chef + i
            


        print((sum % ((10 ** 9) + 7)))
    elif line[0] == 2:
        i, x = line[1], line[2]
        print()

print(n, a, copylist)