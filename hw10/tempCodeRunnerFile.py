 while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[u]
    return max_flow

if __name__ == "__main__":
    num_instances = int(input("Enter the number of instances: ").strip())
    results = []

    for instance in range(num_instances):
        m, n, q = map(int, input(f"Enter m, n, and q for instance {instance + 1}: ").strip().split())
        print(f"Instance {instance + 1}: m={m}, n={n}, q={q}")
        capacity = [[0] * (m + n + 2) for _ in range(m + n + 2)]

        # Connecting source to set A and set B to sink
        for i in range(1, m + 1):
            capacity[0][i] = 1

        for j in range(1, n + 1):  # Adjusted indexing here
            capacity[m + j][m + n + 1] = 1

        # Adding edges between A and B
        for edge in range(q):
            a, b = map(int, input(f"Enter edge {edge + 1} of {q} for instance {instance + 1}: ").strip().split())
            print(f"Edge {edge + 1}: {a} -> {b}")
            capacity[a][m + b] = 1  # Verify this line, you might need to adjust indices

        max_flow = ford_fulkerson(capacity, 0, m + n + 1)
        is_perfect = 'Y' if max_flow == m else 'N'
        results.append(f"{max_flow} {is_perfect}")
        print(f"Instance {instance + 1} done\n")  # Added newline for clarity

    for result in results:
        print(result)