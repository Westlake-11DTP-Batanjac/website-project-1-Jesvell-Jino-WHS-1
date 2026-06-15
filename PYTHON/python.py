n, m = map(int, input().split()) # n nodes, m vertices

graph = [[] for i in range(n)]

for i in range(m):
    u, v, w = map(int, input().split()) # u 1st node, v 2nd node, w weight

    graph[u - 1].append((v, w))

print(graph)
    