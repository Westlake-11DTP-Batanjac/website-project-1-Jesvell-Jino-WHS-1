t = int(input())
cards = [[[] for i in range(t)] for i in range(t)]
for i in range(t):
    k = int(input())
    cards = map(int, input().split()) # a b c ...
    
