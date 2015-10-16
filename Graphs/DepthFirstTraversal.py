'''
Created on Oct 16, 2015

@author: gaurav
'''


def DepthFirstTraversal(edge, adj):
    visited = [edge]
    DFT(visited, adj)

def DFT(visited, adj):
    
    #If the number of visited nodes has become equal to the number of total nodes
    #we have completely traversed the graph
    if len(visited) == len(adj):
        print(visited)
    
    #Make the last visited node the node we need to go ahead from
    current = visited[-1]
    
    #If there is a neighbour of the current node that has not been visited yet, 
    #visit it and start looking for its neighbours
    for i in xrange(len(adj[current])):
        if adj[current][i] == 1:
            if i not in visited:
                visited.append(i)
                
                #If there comes a time where we hit a dead end from a particular vertice,
                #we will recurse back and call DFS on another neighbour of the node
                DFT(visited, adj)
    

def main():
    adj   = [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1]]
    
    #Want to start the depth first search at node 2
    print(DepthFirstTraversal(2, adj))


if __name__ == '__main__':
    main()