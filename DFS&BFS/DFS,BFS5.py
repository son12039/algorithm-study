import sys

data = sys.stdin.read().splitlines()
M,N = map(int, data[0].split())

graph = [list(map(int, i.split())) for i in data[1:]]
v = [[False for _ in range(M)] for _ in range(N)]
def find_point():
    global v,graph
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                DFS(j,i,0)
def DFS(x,y,z):
    global v,graph
    if 0 <= x < M and 0 <= y < N and not v[y][x] and graph[y][x] != -1 :
        v[y][x] = True
        if graph[y][x] >= 1 :
            graph[y][x] = min(graph[y][x],z + 1)
        else:
            graph[y][x] = z + 1
        DFS(x+1,y,z+1)
        DFS(x,y+1,z+1) 
        DFS(x-1,y,z+1) 
        DFS(x,y-1,z+1) 

         
find_point()
for i in graph:
    print(i)