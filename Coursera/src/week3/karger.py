'''
Created on Jul 18, 2012

@author: mmcdonald

Implementation for Problem Set 3.
The task is to implement the Karger Min Cut algorithm, then run many times 
to determine the min cut for the given graph.
'''
import random
import copy

def karger(g):
    while (len(g) > 2):
        edge = get_random_edge(g)
        a = edge[0]
        b = edge[1]
        
        # Fold vertex a into b by...
        # 1) copy node a edges to b
        g[b].extend(g[a])
        
        # 2) delete node a
        del(g[a])
        
        # 3)update all references to node a to node b
        for key in g.keys():
            while a in g[key]:
                g[key].remove(a)
                g[key].append(b)                
                
        # 4) remove self-loops where b points to b
        while b in g[b]:
            g[b].remove(b)
    
    return len(g[min(g)])

def get_random_edge(g):
    v1 = random.choice(list(g.keys()))
    v2 = random.choice(g[v1])
    return v1, v2

def get_min_cut(g, loopCount):
    cuts = []
    
    while (loopCount > 0):
        g_copy = copy.deepcopy(g)
        cuts.append(karger(g_copy))
        loopCount -= 1
    
    return min(cuts)

def main():
    g = {}
    f = open("files//KargerMinCut.txt", "r")

    for line in f.readlines():
        split = line.rstrip("\n").rstrip("\t").split("\t")
        
        edges = []
        
        for i in split[1:]:
            edges.append((int(i)))
        
        g[int(split[0])] = edges

    f.close()
    
    print("Min cut = " + str(get_min_cut(g, 100)))

if __name__ == '__main__':
    main()