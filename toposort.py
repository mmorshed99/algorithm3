#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here
    stack = []
    #not_visited = []
    a = []
    track_child = []
    temp = []
   
    for j in range(0,len(adj)):
       a.append(0)
       track_child.append(0)  # use this to track number of child left to visit
 
    for j in range(0,len(adj)):
       if a[j]:               # use this to track previously visited nodes
        
         continue 

       stack.append(j)
       current_element = j
       k = 0
       revisit = 0
       while(len(stack) > 0):
            if revisit == 0:  # as long as revisit = 0, will keep penetrating 
               
               if (len(adj[current_element])) == 0 or (a[current_element] == 1): # if there is no child beyond the current, will print and go back to previous
                 revisit = 1                                                     # this can happen either if no child left or reach at previously visited node
                 if (a[current_element] == 0):
                    temp.append(current_element) # 'temp' is used to print the final output 
                    a[current_element] = 1
         
                 stack.pop()                     # stack was used to have a list of nodes to visit afterwards...once finished visiting the node, it is removed
               if revisit ==0:
                 track_child[current_element] = len(adj[current_element]) - 1
                 current_element = adj[current_element][0]
                 stack.append(current_element)
            if revisit == 1 and len(stack)> 0:
               current_element = stack.pop()
               if track_child[current_element] > 0: # if still children left for a node...it will be tried 
                 revisit = 0
                 stack.append(current_element)
                 track_child[current_element] -= 1
                 current_element = adj[current_element][track_child[current_element]+1]
                 stack.append(current_element)
             
               if revisit == 1:                     # if no child left...that node is printed
                 temp.append(current_element)
                 a[current_element] = 1
                 
                 
               
                     
                    
            
    temp.reverse()             
    
    return temp

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    
    for x in range(0,len(order)):
       order[x] = order[x] + 1
    
    print(' '.join(map(str,order)))
    #for x in order:
    #    print(x + 1, end=' ')

