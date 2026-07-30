t = int(input())
n = []
s = []
for i in range(t):
    n.append(int(input()))
    s.append(input())

def substrings(n, s): # n is the lenght s is the string
    tsubstrings = (n * (n + 1)) / 2


for i in range(t):
    silly = list(s[i])
    while True:
        old = i - 1
        if n[i] == 1:
            print("a", i, n[i])
            break
        else:
            ap = [] # ap : adjacent pairs
            apcount = 0
            onecount = 0
            zerocount = 0
            for i in silly:
                adjacentpairs = []
                if i == "0":
                    zerocount += 1
                elif i == "1":
                    onecount += 1
                if silly[i - 1] == silly[i]:
                    apcount += 1
                    adjacentpairs.append((silly[i - 1], silly[i]))
                
            # There is at least one adjacent pair
            # 00100 B, 10101 U, 10100 B, 01101 B, 00100 B, 00000 B, 11111 B