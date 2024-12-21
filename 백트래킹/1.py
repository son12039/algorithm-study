import sys

def backtrack(N,M, sequence,t):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    for i in range(1,N+1):
        if i not in sequence:
            sequence.append(i)
            backtrack(N,M,sequence,t+1)
            sequence.pop()
N,M = map(int,sys.stdin.read().split())
backtrack(N, M, [],0)
 