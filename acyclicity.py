#Uses python3

import sys


def acyclic(adj):
    total = len(adj)
    i = total - 1
    j = 0
    loop = 0
    temp = -1
    stack = []
    visited = []
    for y in range(0,len(adj)):
       visited.append(y)
    while(len(visited) > 0):
         stack.append(i)
         #print(stack)
         #print(i)
         #print(adj)
         if(len(adj[i]) > 0):
           #for j in range(0,len(adj[i]):
             if adj[i][len(adj[i])-1] in stack:
                #print(stack)
                #print(adj[i][len(adj[i])-1])
                loop = 1
                visited = []
                break
             else:
                i = adj[i][len(adj[i])-1]
         else:
             temp = stack.pop()
             total = total - 1
             for q in range(0,len(adj)):
                for r in range(0,len(adj[q])):
                   if adj[q][r] == temp:
                     adj[q].remove(temp)
                     break
             #print(temp)
             #print(adj)
             visited.remove(temp)
             #del visited[temp]
             if len(stack)>0:
               i = stack.pop()
             elif len(visited)>0:
               i = visited[len(visited) - 1]        

    return loop

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print(adj)
    print(acyclic(adj))
