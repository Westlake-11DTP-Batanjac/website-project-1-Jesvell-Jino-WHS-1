t = int(input()) # test cases
for i in range(t):
    x, y = map(int, input().split())
    z = x / y
    if int(z) == z:
        print("YES")
    else:
        print("NO")