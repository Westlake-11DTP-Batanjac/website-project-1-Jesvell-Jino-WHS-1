    n = int(input())
    a = list(map(int, input().split())) # A index is chef num, value is skill
    d = a.copy() # dish list
    copylist = [[] for i in range(n)]

    for i in range(n):
        ci, *cq = map(int, input().split()) # ci the chef chosen and cq the chefs chosen chef can copy
        copylist[i] = cq

    q = int(input())

    for i in range(q):
        line = list(map(int, input().split()))
        if line[0] == 1:
            s = d.copy() # simulation list
            sum = 0
            k, l, r = line[1], line[2], line[3] # kth day
            for i in range(k): #days
                for x in range(l - 1, r - 1): # per chefs
                    # MORNING
                    if (a[x] * s[x]) > s[x]:
                        s[x] = a[x] * s[x]
                    else:
                        pass
                    # AFTERNOON
                    for c in copylist[x]:
                        if (s[x] + s[c - 1] + 1) > s[x]:
                            s[x] = s[x] + s[c - 1]
            for x in range(l, r):
                sum += s[x]
            sum = sum % 1000000007
            print("sum", sum)
        elif line[0] == 2:
            i, x = line[1], line[2]
            i -= 1
            d[i] = d[i] + x