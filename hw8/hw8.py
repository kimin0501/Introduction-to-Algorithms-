def knapsack(W, weights, values, item_nums):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)

    for i in range(1, item_nums + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                curr[w] = max(prev[w], prev[w - weights[i - 1]] + values[i - 1])
            else:
                curr[w] = prev[w]
        prev, curr = curr, prev

    return prev[W]

if __name__ == "__main__":
    num_instances = int(input())
    for _ in range(num_instances):
        item_nums, W = map(int, input().split())
        items = []
        for _ in range(item_nums):
            weight, value = map(int, input().split())
            items.append((weight, value))
            
        weights, values = zip(*items) if items else ([], [])
        print(knapsack(W, weights, values, item_nums))