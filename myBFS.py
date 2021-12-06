# Personal BFS
graph={'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
"""
        # Differences from DFS:
        # 1) pop first instead of last
        # 2) add adjacent elements to stack and then explore them


- Create a graph.
- Initialize a starting node.
- Send the graph and initial node as parameters to the bfs function.
- Mark the initial node as visited and push it into the queue.

- Repeat this process until all the nodes in a graph are visited and the queue becomes empty:
    - Explore the initial node and add its neighbours to the queue and remove the initial node from the queue.
    - Check if the neighbours node of a neighbouring node is already visited.
    - If not, visit the neighbouring node neighbours and mark them as visited.

"""
def bfs(graph, start):
    visited=[]
    queue=[start]
    while queue:
        node=queue.pop(0)#initially the first node
        if node not in visited:
            visited.append(node)
            neighbors=graph[node]

            for neighbor in neighbors:
                queue.append(neighbor)

    return visited

print(bfs(graph, "A"))

