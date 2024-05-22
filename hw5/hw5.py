def merge_sort(orig_array, temp_array, left, right):
    inversion_count = 0
    # checks whether the current subarray has more than one element
    if left < right:
        mid = (left + right) // 2
        # Divide & Conquer
        inversion_count += merge_sort(orig_array, temp_array, left, mid)
        inversion_count += merge_sort(orig_array, temp_array, mid + 1, right)
        inversion_count += merge(orig_array, temp_array, left, mid, right)
    
    return inversion_count

def merge(orig_array, temp_array, left_index, mid_index, right_index):
    # initialize variables to track current elements
    leftIdx, rightIdx, mergeIdx = left_index, mid_index + 1, left_index
    inversion_count = 0
    
    # merging and counting inversions
    while leftIdx <= mid_index and rightIdx <= right_index:
        if orig_array[leftIdx] <= orig_array[rightIdx]:
            temp_array[mergeIdx] = orig_array[leftIdx]
            mergeIdx += 1
            leftIdx += 1
        else:
            temp_array[mergeIdx] = orig_array[rightIdx]
            inversion_count += (mid_index - leftIdx + 1)
            mergeIdx += 1
            rightIdx += 1
    
    # copy remaining elements
    while leftIdx <= mid_index: 
        temp_array[mergeIdx] = orig_array[leftIdx]
        mergeIdx += 1
        leftIdx += 1
    
    while rightIdx <= right_index:
        temp_array[mergeIdx] = orig_array[rightIdx]
        mergeIdx += 1
        rightIdx += 1
    
    # copy back to original array
    for leftIdx in range(left_index, right_index + 1):
        orig_array[leftIdx] = temp_array[leftIdx]
        
    return inversion_count

if __name__ == "__main__":
    num_instances = int(input())
    inversion_results = []

    for _ in range(num_instances):
        array_size = int(input())
        orig_array = list(map(int, input().strip().split()))
        temp_array = [0] * len(orig_array)
        inversion_count = merge_sort(orig_array, temp_array, 0, len(orig_array) - 1)
        inversion_results.append(inversion_count)
        print(f"{inversion_count}")