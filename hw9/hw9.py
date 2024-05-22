from collections import deque

def ford_fulkerson(capacity, source, sink):
    n = len(capacity)
    max_flow = 0
    parent = [-1] * n

    def bfs(capacity, source, sink):
        visited = [False] * n
        queue = deque()
        queue.append(source)
        visited[source] = True
        while queue:
            u = queue.popleft()
            for ind, val in enumerate(capacity[u]):
                if not visited[ind] and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
        return visited[sink]

    while bfs(capacity, source, sink):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
    return max_flow

if __name__ == "__main__":
    num_instances = int(input())
    for _ in range(num_instances):
        n, m = map(int, input().split())
        capacity = [[0] * n for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            capacity[u-1][v-1] += w
        max_flow = ford_fulkerson(capacity, 0, n-1)
        print(f"{max_flow}")
