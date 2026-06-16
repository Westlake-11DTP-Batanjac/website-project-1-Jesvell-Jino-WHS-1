import heapq

# import the node, and

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Remove if the graph is directed

start = 1

dist = [float('inf')] * (n + 1)
dist[start] = 0

pq = [(0, start)]  # (distance, node)

while pq:
    current_dist, u = heapq.heappop(pq)

    if current_dist > dist[u]:
        continue

    for v, weight in graph[u]:
        new_dist = current_dist + weight

        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

print(dist[n])  # shortest distance from node 1 to node n