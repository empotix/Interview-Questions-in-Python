'''
I/P: N, k 
O/P: all subset of N with exactly K elements. 

eg: I/p: N = 5, K =3 
O/p: 
1 2 3 
1 2 4 
1 2 5 
1 3 4 
1 3 5 
2 3 4 
2 3 5 
3 4 5
'''

def permute(values, domain, visited):
    
    if(len(values) == k):
        print(values)
        return
    
    for i in range(len(domain)):
        
        #If it has not been used before, use it and mark it
        #as visited
        if visited[i] != 1:
            values.append(domain[i])
            visited[i] = 1
            permute(values, domain, visited)
            visited[i] = 0
            values = values[:-1]
           

n = 5
k = 3
domain = [i for i in xrange(1, n+1)]
visited = [0 for i in xrange(1, n+1)]
values = []
permute(values, domain, visited)
