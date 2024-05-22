def count_page_faults(cache_size, requests):
    cache_set = set()  
    page_dictionary = {} 
    page_faults = 0
    current_time = 0

    # Record the request time for each page
    for request in requests:
        page_dictionary[request] = page_dictionary.get(request, []) + [current_time]
        current_time += 1

    cache_list = [] 

    # Process each page request
    for request in requests:
        
        # Check if the page is already in the cache
        if request in cache_set:
            # Cache hit
            page_dictionary[request].pop(0)
        else:
            # Cache Miss
            page_faults += 1
            
            # Check if there is room in the cache
            if len(cache_set) < cache_size:
                cache_set.add(request)
                cache_list.append(request)
            else:
                furthest_time = -1
                furthest_page = None
                for page in cache_list:
                    # Check if a page has more requests, and track best candidate for replacement
                    if page_dictionary[page]:
                        next_use = page_dictionary[page][0]
                        if next_use > furthest_time:
                            furthest_time = next_use
                            furthest_page = page
                    else:
                        furthest_page = page
                        break
                
                # Remove the furthest page fron the cache and add the new one
                cache_set.remove(furthest_page)
                cache_list.remove(furthest_page)
                cache_set.add(request)
                cache_list.append(request)

            # update the request time for the current page
            if page_dictionary[request]:
                page_dictionary[request].pop(0)  

    return page_faults

if __name__ == "__main__":
    num_instances = int(input())
    results = []

    for _ in range(num_instances):
        cache_size = int(input())
        num_requests = int(input())
        requests = list(map(int, input().strip().split()))
        page_faults = count_page_faults(cache_size, requests)
        results.append(page_faults)
        print(f"{page_faults}")
