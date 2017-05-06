#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    track = []
    next_visit = []
    future_visit = []
    for i in range(0,len(adj)):
       track.append(1)
    if len(adj[s]) < 1:
      return -1

    for i in range(0,len(adj[s])):
       if adj[s][i] == t:
         return 1
       next_visit.append(adj[s][i])
       track[adj[s][i]] = 0
    curr_dist = 1
    while (len(next_visit)>0):
         curr_node = next_visit.pop()
         for i in range(0,len(adj[curr_node])):
            if track[adj[curr_node][i]]:
              future_visit.append(adj[curr_node][i])
              if adj[curr_node][i] == t:
                return curr_dist + 1
              else:
                track[adj[curr_node][i]] = 0
         if len(next_visit) == 0:
           curr_dist += 1
           next_visit = future_visit
           #for j in range(0,len(future_visit)):
              #track[j] =0
           future_visit = []
          
   


    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
