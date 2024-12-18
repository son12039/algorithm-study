from collections import deque
import sys
input = sys.stdin.read
data = input().splitlines()

N,M,V = map(int, data[0].split())

graph = [[] for _ in range(N+1)]
for i in range(1,M+1):
    x,y = map(int, data[i].split())
    graph[y].append(x)
    graph[x].append(y)

for g in graph:
    g.sort()

vizited = [False for _ in range(N+1)]
def DFS(idx):
    vizited[idx] = True
    result = [str(idx)]
    for i in range(len(graph[idx])):
        if not vizited[graph[idx][i]]:
            result += DFS(graph[idx][i])
    return result
print(" ".join(DFS(V)))

vizited = [False for _ in range(N+1)]
def BFS():
    q = deque([V])
    vizited[V] = True
    re = []     
    while q:
        c = q.popleft()
        re.append(str(c))
        for i in range(len(graph[c])):
            if not vizited[graph[c][i]]:          
                q.append(graph[c][i])
                vizited[graph[c][i]] = True
    return re
print(" ".join(BFS()))