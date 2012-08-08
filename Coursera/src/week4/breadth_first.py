'''
Created on Jul 25, 2012

@author: mmcdonald

Testing breadth-first traversal and related algorithms from the Week 4 lectures.
'''
from collections import deque

def breadth_first_search(g, s):
    """
    Very simple breadth-first search implementation for Week 4 lectures.

    g: simple graph representation using a dictionary where key = vertex label, value = [adjacent edges]
    s: root node to begin search from
    returns: list representing the order of vertex traversal
    """
    visited = []

    # Enqueue first vertex, mark as visited
    queue = deque([s])
    visited.append(s)
    
    while (len(queue)) > 0:
        v = queue.popleft()
        
        for w in g[v]:
            if not w in visited:
                visited.append(w)
                queue.append(w)
            
    return visited

def shortest_paths(g, s):
    """
    Uses bfs to traverse graph from a given starting vertex, calculating shortest paths to each vertex reached

    g: simple graph representation using a dictionary where key = vertex label, value = [adjacent edges]
    s: root node to begin traversal from
    returns: dictionary where key = vertex, value = length of path from starting point s
    """
    paths = {}
    queue = deque([s])
    paths[s] = 0
    
    while (len(queue)) > 0:
        v = queue.popleft()
        
        for w in g[v]:
            if not w in paths:
                paths[w] = paths[v] + 1
                queue.append(w)
                
    return paths

def undirected_connected_components(g):
    """
    Uses bfs to calculate the connected components in an undirected graph. 

    g: simple graph representation using a dictionary where key = vertex label, value = [adjacent edges]
    returns: list of lists where each sub-list represents a set of connected vertices 
    """
    connected_components = []
    allVisited = []
    
    for vertex in g.keys():
        if not vertex in allVisited:
            visited = breadth_first_search(g, vertex)
            allVisited.extend(visited)
            connected_components.append(visited)
        
    return connected_components

def main():
    g = {}
    f = open("files//CC-undirected.txt", "r")

    for line in f.readlines():
        split = line.rstrip("\n").rstrip(" ").split(" ")
        v = int(split[0])
        e = int(split[1])
        
        if not v in g:
            g[v] = [e]
        else:
            g[v].append(e)
        
    f.close()
    
    s = 2
   
    order = breadth_first_search(g, s)
    print(order)
    
    sp = shortest_paths(g, s)
    print(sp)
    
    connected_components = undirected_connected_components(g)
    print(connected_components)
    
if __name__ == '__main__':
    main()    