# A* Algorithm Implementation using Graph Search

from heapq import heappush, heappop

# Example graph (node: {neighbor: cost})
graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
}


heuristics = {
    'S': 7, 'A': 6, 'B': 4,
    'C': 2, 'D': 1, 'G': 0
}

def astar(graph, heuristics, start, goal):
    open_list = []  
    heappush(open_list, (heuristics[start], start, [start], 0)) 
    closed = set()

    while open_list:
        f, node, path, g = heappop(open_list)

        if node == goal:
            return path, g  

        if node in closed:
            continue
        closed.add(node)

        for neighbor, cost in graph[node].items():
            g_new = g + cost
            f_new = g_new + heuristics[neighbor]
            heappush(open_list, (f_new, neighbor, path + [neighbor], g_new))

    return None, float('inf') 


start, goal = 'S', 'G'
path, cost = astar(graph, heuristics, start, goal)
print("Shortest Path:", path)
print("Total Cost:", cost)
