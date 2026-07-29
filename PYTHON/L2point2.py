t = int(input())
n = []
s = []
for i in range(t):
    n.append(int(input()))
    s.append(input())

for i in range(t):
    silly = list(s[i])
    while True:
        old = i - 1
        if len(silly) == 1:
            break
        else:
            for i in range(n[i]):
                if silly[old] == silly[i]:
                    silly.pop(silly[old])
                    silly.pop(silly[i])
                    if silly[old] == "1":
                        new_char = "0"
                    elif silly[old] == "0":
                        new_char = "1"
                    silly.insert(old, new_char)
                old = silly[i]
