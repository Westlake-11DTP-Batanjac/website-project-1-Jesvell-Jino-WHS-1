n = 6
roads = [
    [1, 2, 7],
    [1, 3, 9],
    [1, 6, 14],
    [2, 3, 10],
    [2, 4, 15],
    [3, 4, 11],
    [3, 6, 2],
    [4, 5, 6],
    [5, 6, 9]
]
start = 1
# INPUT ////////

connections = [[()] * (n + 1)]

for f, t, w in roads:
    connections[f] = (t, w)

print(connections)