'''
Created on Oct 16, 2015

@author: gaurav
'''

def DepthFirstSearch(src, dest, adj):
    visited = [src]
    DFS(src, dest, adj, visited)
   
def DFS(src, dest, adj, visited):
    
    #If we have reached the destination, we print the nodes we have visited on the way to it
    if src == dest:
        print(visited)

    #If there is a neighbour of the current node that has not been visited yet, 
    #visit it and start looking for its neighbours
    for i in xrange(len(adj[src])):
        if adj[src][i] == 1:
            if i not in visited:
                visited.append(i)
                DFS(i, dest, adj, visited)
                
                #Need to remove the last element since the only reason we have come back
                #is that a path did not lead from it to the destination. Now we need to
                #try for another child. WOULD NOT REMOVE THIS IN DEPTH FIRST SEARCH.
                visited = visited[:-1]

def main():
    adj   = [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1]]
    
    #Want to start the depth first search at node 2 and look for node 1
    DepthFirstSearch(2, 1, adj)
    
    #Want to start the depth first search at node 2 and look for node 1
    DepthFirstSearch(2, 3, adj)

if __name__ == '__main__':
    main()