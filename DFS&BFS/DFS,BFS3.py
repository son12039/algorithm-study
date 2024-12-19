import sys
from collections import deque
data = sys.stdin.read().splitlines()
C = int(data[0])
N = int(data[1])
graph = [[] for _ in range(C+1)]
for p,c in (map(int, i.split()) for i in data[2:]):
    graph[p].append(c)
    graph[c].append(p)
q = deque([1])
vizited = [0 for _ in range(C+1)]
while q :
    c = q.popleft()
    vizited[c] = 1
    for i in graph[c]:
        if not vizited[i]:
            q.append(i)
print(sum(vizited)-1)