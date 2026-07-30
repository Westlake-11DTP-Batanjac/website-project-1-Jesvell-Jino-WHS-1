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
            # make beautiful
            pass