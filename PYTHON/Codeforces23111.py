t = int(input())
cards = [[[] for i in range(t)] for i in range(t)]
for i in range(t):
    k = int(input())
    cards = map(int, input().split()) # a b c ...
    higherthantwo = 0
    passed = False
    for i in cards:
        if higherthantwo >= 2:
            print("YES")
            passed = True
            break
        elif i == 3:
            print("YES")
            passed = True
            break
        elif i >= 2:
            higherthantwo += 1
    if passed == False:
        print("NO")
