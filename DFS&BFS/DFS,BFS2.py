import sys 
from collections import deque
data = sys.stdin.read().strip().splitlines()
N,M = map(int, data[0].split())
maze = [list(map(int, data[i])) for i in range(1,N+1)]
q = deque([[0,0,1]])

def BFS():
    global q
    while q:
        y,x,z = q.popleft()
        if maze[y][x] == 1:
            maze[y][x] = z
            if 0 < y:
                q.append([y-1,x,z+1])
            if 0 < x:
                q.append([y,x-1,z+1])
            if  y < N - 1 :
                q.append([y+1,x,z+1])
            if  x < M - 1 :
                q.append([y,x+1,z+1])
BFS()
print(maze[N-1][M-1])