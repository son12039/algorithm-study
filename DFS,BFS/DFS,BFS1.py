def dfs(graph, v, visited):
    print("시작한다")
    visited[v] = True
    print(v)  # 방문한 노드 출력
    for neighbor in sorted(graph[v]):  # 작은 번호부터 탐색
        print(neighbor," 이걸로 검사")
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


# 입력 받기
N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}

# 간선 정보 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS 수행
visited = [False] * (N + 1)
dfs(graph, V, visited)
