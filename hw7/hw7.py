def binary_search(jobs, current_index):
    low, high = 0, current_index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[current_index][0]:
            if jobs[mid + 1][1] <= jobs[current_index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1

def schedule_weighted_intervals(jobs):
    jobs.sort(key=lambda x: x[1])
    total_jobs = len(jobs)
    table = [0] * (total_jobs + 1)
    table[1] = jobs[0][2]

    for j in range(1, total_jobs):
        i = binary_search(jobs, j)
        temp_max_weight = jobs[j][2]
        if i != -1:
            temp_max_weight += table[i + 1]
        table[j + 1] = max(temp_max_weight, table[j])

    return table[total_jobs]

if __name__ == "__main__":
    num_instances = int(input())
    results = []

    for _ in range(num_instances):
        num_jobs = int(input())
        jobs = []
        for _ in range(num_jobs):
            start_time, end_time, weight = map(int, input().split())
            jobs.append((start_time, end_time, weight))
        results.append(schedule_weighted_intervals(jobs))

    for result in results:
        print(result)
