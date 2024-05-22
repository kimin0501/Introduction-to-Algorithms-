from typing import Dict, List, Tuple

#Type Definition
Node = str
NodeList = List[Node]
AdjacencyList = Dict[Node, NodeList]

# traverse the graph with depth first search
def perform_dfs(adj_list: AdjacencyList, nodes: NodeList):
    
    # initialize empty set and list
    visited = set()  
    traversal = [] 

    # loop over all nodes
    for start_node in nodes:
        if start_node not in visited:
            stack = [start_node]

            # continue loop until there is no node in the stack to be visited 
            while stack:
                current = stack.pop()  

                # check if the current node has not been visited
                if current not in visited:
                    visited.add(current)  
                    traversal.append(current)                 
                    unvisited_neighbors = []
                    
                    # loop through each neighbor of the current node
                    for neighbor in adj_list[current]:
                        if neighbor not in visited:
                            unvisited_neighbors.append(neighbor)
                    # extend the stack with the reversed list
                    unvisited_neighbors.reverse()  
                    stack.extend(unvisited_neighbors)  

    return traversal  

# parse and construct data from user input 
def parse_dfs(nodes_num: int):
    
    # initialize dictionary and list
    adjacent_dictionary = {}
    node_list = []

    # loop once for each node
    for _ in range(nodes_num):

        # read and split the input
        node_input = input().split()
        node = node_input[0]
        neighbors = node_input[1:]
        
        # construct the data structure
        adjacent_dictionary[node] = neighbors
        node_list.append(node)

    return adjacent_dictionary, node_list


if __name__ == "__main__":
    instance_num = int(input())
    
    for instance in range(instance_num):
        node_num = int(input())
        adjacency_list, node_order = parse_dfs(node_num)
        
        traversal_order = perform_dfs(adjacency_list, node_order)
        print(" ".join(traversal_order))
