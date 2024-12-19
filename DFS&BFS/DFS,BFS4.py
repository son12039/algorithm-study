import sys
from collections import deque

data = sys.stdin.read().splitlines()
N = int(data[0])
graph = [list(map(int, i)) for i in data[1:]]

def find_point():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                return [i,j]
    return None

def BFS(s):
    q = deque([s])
    re = 0
    while q:
        y,x = q.popleft()
        if graph[y][x] == 1:
            re+=1
            graph[y][x] = 0
            if 0 < y:
                q.append([y-1,x])
            if 0 < x:
                q.append([y,x-1])
            if  y < N - 1 :
                q.append([y+1,x])
            if  x < N - 1 :
                q.append([y,x+1])
    return re
result = []
while True:
    p = find_point()
    if not p: 
        break
    result.append(BFS(p))

result.sort()
print(len(result))
for i in result:
    print(i)
