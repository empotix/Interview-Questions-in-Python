'''
Created on Oct 16, 2015

@author: gaurav
'''


def BreadthFirstTraversal(edge, adj):
    discovered = [edge]
    visited = []
    BFT(discovered, visited, adj)
    
def BFT(discovered, visited, adj):
    while len(discovered) != 0:
        current = discovered.pop(0)
        print(current)
        
        for i in range(len(adj[current])):
            if adj[current][i] == 1:
                if i not in discovered and i not in visited and i != current:
                    discovered.append(i)
        
        visited.append(current)
        
    
def main():
    adj   = [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1]]
    
    #Want to start the depth first search at node 2
    BreadthFirstTraversal(2, adj)


if __name__ == '__main__':
    main()