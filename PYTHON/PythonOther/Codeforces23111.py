t = int(input())
for i in range(t):
    k = int(input())
    cards = list(map(int, input().split())) # a b c ...
    higherthantwo = 0
    higherthanthree = 0
    passed = "NO"
    cardavg = (sum(cards) / k)
    if int(cardavg) >= 2:
        passed = "YES"
    print(passed)
