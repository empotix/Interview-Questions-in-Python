'''
Created on Oct 16, 2015

@author: gaurav
'''

# Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once. 
# A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an edge (in graph) 
# from the last vertex to the first vertex of the Hamiltonian Path. Determine whether a given graph contains
# Hamiltonian Cycle or not. If it contains, then print the path. Following are the input and output of the required function.
# 
# Input:
# A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix 
# representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.
# 
# Output:
# An array path[V] that should contain the Hamiltonian Path. path[i] should represent the ith vertex in the Hamiltonian Path. 
# The code should also return false if there is no Hamiltonian Cycle in the graph.


def findHamiltonianCycle(adj):
    visited = [0]
    current = visited[-1]
    return trackHamiltonian(current, visited, adj)
    

def trackHamiltonian(current, visited, adj):
    
    #If the number of nodes visited has become equal to the number of nodes
    #we have our hamiltonian cycle
    if len(visited) == len(adj):
        visited.append(visited[0])
        return visited
    
    for i in range(0,len(adj[current])):
        
        #If there exists a neighbour of the current node that we have not visited
        #visit it and recursively call this method.
        if adj[current][i] == 1:
            if i not in visited:
                visited.append(i)
                current = i
                return trackHamiltonian(current, visited, adj)
    
    return False

def main():
    adj   = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]]
    print(findHamiltonianCycle(adj))
    
    #Solution Exists: Following is one Hamiltonian Cycle
    #0  1  2  4  3  0
    
    adj   = [[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 0],
             [0, 1, 1, 0, 0]]
    print(findHamiltonianCycle(adj))
    
    #Solution does not exist


if __name__ == '__main__':
    main()