def merge(points, low, mid, high):
    merged_points = []
    count = 0
    i = low
    j = mid + 1
    
    # Merge the two halves while counting intersections
    while i <= mid and j <= high:
        if points[i][1] <= points[j][1]:
            merged_points.append(points[i])
            i += 1
        else:
            merged_points.append(points[j])
            count += mid - i + 1
            j += 1

    # Append remaining points from both halves
    merged_points.extend(points[i:mid+1])
    merged_points.extend(points[j:high+1])

    points[low:high+1] = merged_points

    return count

def count_intersections(points, low, high):
    # Base case
    if low >= high:
        return 0

    mid = (low + high) // 2
    
    # Recursively count intersections
    left_count = count_intersections(points, low, mid)
    right_count = count_intersections(points, mid + 1, high)
    
    # Count intersections between two halves
    merge_count = merge(points, low, mid, high)

    total_count = left_count + right_count + merge_count
    
    return total_count 



if __name__ == "__main__":
    num_instances = int(input())
    results = []

    for _ in range(num_instances):
        num_points = int(input())
        top_points = []
        bottom_points = []

        for _ in range(num_points):
            x = int(input())
            top_points.append(x)

        for _ in range(num_points):
            x = int(input())
            bottom_points.append(x)

        points = list(zip(top_points, bottom_points))
        
        points.sort(key=lambda point: point[0]) 

        count = count_intersections(points, 0, num_points - 1)
        print(count)