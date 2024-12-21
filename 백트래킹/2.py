import sys

def B_T(N,M,L):
    if len(L) == M:
        print(" ".join(map(str,L)))
        return
    for i in range(1,N+1):
        if not L or L[-1] < i:
            L.append(i)
            B_T(N,M,L)
            L.pop()

N,M = map(int,sys.stdin.read().split())
B_T(N,M,[])