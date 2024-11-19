import heapq
import sys

input = sys.stdin.read
data = sys.stdin.read().splitlines()
min = []
n = int(data[0])
result = []
for i in range(1,n+1):
    nn = -int(data[i])
    if nn == 0:
        try:
            result.append(str(-heapq.heappop(heap)))
        except IndexError:
            result.append("0")
    else:
        heapq.heappush(heap, nn)
sys.stdout.write("\n".join(result) + "\n")
