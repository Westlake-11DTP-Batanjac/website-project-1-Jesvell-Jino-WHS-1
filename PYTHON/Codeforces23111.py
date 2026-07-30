t = int(input())
for i in range(t):
    k = int(input())
    cards = list(map(int, input().split())) # a b c ...
    higherthantwo = 0
    passed = "NO"
    for i in cards:
        if k == 1 and i >= 3:
            passed = "YES"
            break
        elif 
    print(passed)
