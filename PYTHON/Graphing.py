
m, n = map(int, input().split())

graph = []
new = [[0] * n for _ in range(m)]
visited = []

for i in range(m):
    graph.append(list(map(int, input().split())))

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)] # directions

def search(source, old):
    mines = 0

    for dy, dx in dirs:

        y = source[0] + dy
        x = source[1] + dx

        if 0 <= x < n and 0 <= y < m and old[y][x] == 1:
            mines += 1
    new[source[0]][source[1]] = mines

    visited.append((source[0], source[1]))

for y in range(len(graph)):
    for x in range(len(graph[y])):
        search((y, x), graph)

print(new)