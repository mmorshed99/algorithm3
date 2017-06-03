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
         #### if the node has outgoing connection and that node is already in stack..there is a cycle ####
         if(len(adj[i]) > 0):
             if adj[i][len(adj[i])-1] in stack:
                loop = 1
                visited = []
                break
             #### if that node isn't in stack, travelling will be continued ### 
             else:
                i = adj[i][len(adj[i])-1]
         ### if that node has no outbound connection...no cycle is detected yet and that node can be excluded from future explorations ###
         else:
             temp = stack.pop()
             total = total - 1
             for q in range(0,len(adj)):
                for r in range(0,len(adj[q])):
                   if adj[q][r] == temp:
                     adj[q].remove(temp)
                     break
             ### In case of no cycle...this will make sure that loop stops iterating..as there will be nothing in visited in the end ###
             visited.remove(temp)
             ### To resume explorations...a node from stack is selected  ###
             if len(stack)>0:
               i = stack.pop()
             ### or if stack is empty, any unvisited node is selected, if any ###
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
    print(acyclic(adj))
