'''
Created on Oct 16, 2015

@author: gaurav
'''

def isCyclic(adj):
    visited = [0]
    return isCyclicUtil(visited, adj)

def isCyclicUtil(visited, adj):
    
    #Stack implementation. Append to the end and remove from the end.
    current = visited[-1]
    
    for i in xrange(len(adj[current])):
        if adj[current][i] == 1:
            
            #If there consists of an edge where the destination node has already
            #been visited from somewhere else, then we have a cycle
            if i in visited:
                return True
            
            else:
                visited.append(i)
                return isCyclicUtil(visited, adj)
    
    #We only get here if every node completely checks its children without returning True
    #at any point of time
    return False

def main():
    adj   = [[0, 1, 1, 0],
             [0, 0, 1, 0],
             [1, 0, 0, 1],
             [0, 0, 0, 1]]
    print(isCyclic(adj))
    
    adj   = [[0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1],
             [0, 0, 0, 0]]
    print(isCyclic(adj))

if __name__ == '__main__':
    main()