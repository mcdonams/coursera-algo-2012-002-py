'''
Created on Jul 25, 2012

@author: mmcdonald

Testing depth-first traversal and related algorithms from the Week 4 lectures.
'''
def depth_first_search(g, s):
    """
    Very simple depth-first search implementation for Week 4 lectures.

    g: simple graph representation using a dictionary where key = vertex label, value = [adjacent edges]
    s: root node to begin search from
    returns: list representing the order of vertex traversal
    """
    visited = [s]
    
    def dfs(g, s):
        """
        Depth-first search sub-function which calls itself recursively
        """
        for w in g[s]:
            if not w in visited:
                visited.append(w)
                dfs(g, w)
            
    dfs(g, s)    
            
    return visited

def depth_first_search_stack(g, s):
    """
    Simple depth-first search implementation using a stack opposed to recursive calls 
    """
    visited = []
    stack = [s]
    
    while (len(stack)) > 0:
        v = stack.pop()
        visited.append(v)
        
        for w in g[v]:
            if not w in visited:
                stack.append(w)
    
    return visited

def topological_sort(g):
    explored = []
    #current_ordinal = len(g)
    #order = {}
    
    def dfs(g, s):
        """
        Internal depth-first search sub-function which calls itself recursively
        """
        if s in g.keys():
            for w in g[s]:
                if not w in explored:
                    dfs(g, w)
            
        explored.insert(0, s)
        #explored.append(toAppend)
        #order[toAppend] = current_ordinal
        #current_ordinal -= 1
    
    for s in g.keys():
        if not s in explored:
            dfs(g, s)
            
    return explored

def test_topo():
    g = {}
    f = open("files//topo-sort.txt", "r")

    for line in f.readlines():
        split = line.rstrip("\n").rstrip(" ").split(" ")
        v = split[0]
        e = split[1]
        
        if not v in g:
            g[v] = [e]
        else:
            g[v].append(e)
        
    f.close()
    
    order = topological_sort(g)
    print(order)
    
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
    
    order = depth_first_search(g, s)
    print(order) 
    order = depth_first_search_stack(g, s)
    print(order)
    
if __name__ == '__main__':
    main()
    test_topo()