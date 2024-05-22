from collections import deque

def bfs(rGraph, s, t, parent):
    visited = [False] * len(rGraph)
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.popleft()
        for ind, val in enumerate(rGraph[u]):
            if not visited[ind] and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]

def ford_fulkerson(graph, source, sink):
    rGraph = [row[:] for row in graph]  
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(rGraph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, rGraph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            rGraph[u][v] -= path_flow
            rGraph[v][u] += path_flow
            v = parent[v]

    return max_flow

if __name__ == "__main__":
    num_instances = int(input())
    results = []

    for _ in range(num_instances):
        m, n, q = map(int, input().split())
        capacity = [[0] * (m + n + 2) for _ in range(m + n + 2)]

        for i in range(1, m + 1):
            capacity[0][i] = 1

        for j in range(m + 1, m + n + 1):
            capacity[j][m + n + 1] = 1

        for _ in range(q):
            a, b = map(int, input().split())
            capacity[a][m + b] = 1

        # Debug: Print the capacity matrix
        print("Capacity matrix:")
        for row in capacity:
            print(' '.join(map(str, row)))

        max_flow = ford_fulkerson(capacity, 0, m + n + 1)

        # Debug: Print the max flow, m, n, and the condition for a perfect match
        print(f"max_flow: {max_flow}, m: {m}, n: {n}, condition for perfect match: {max_flow == min(m, n)}")

        is_perfect = 'Y' if max_flow == m and m == n else 'N'
        results.append(f"{max_flow} {is_perfect}")

    for result in results:
        print(result)
