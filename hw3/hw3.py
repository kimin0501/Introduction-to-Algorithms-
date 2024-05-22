from math import inf

def greedy(intervals):
    intervals.sort(key = lambda x : x[1])
    removed_intervals = 0
    
    k = -inf
    
    for start_time, end_time in intervals:
        if start_time >= k:
            k = end_time
        else:
            removed_intervals += 1
    
    return len(intervals) - removed_intervals
    

if __name__ == "__main__":
    num_cases = int(input().strip())
            
    for _ in range(num_cases):
        num_intervals = int(input().strip())
            
        intervals = []
        
        for _ in range(num_intervals):
            start_time, end_time = map(int, input().strip().split())
        
            intervals.append([start_time, end_time])
            
        print(greedy(intervals))